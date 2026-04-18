"""
Gaussian Mixture Model (GMM) clustering engine.
Independent from UI and Streamlit. Designed for testability and modularity.
"""
from typing import Tuple, List
import numpy as np
import pandas as pd
import pygad
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.mixture import GaussianMixture

from clustering.base_clustering import BaseClustering
from clustering.evaluation.stability import stability_and_consensus
import streamlit as st
import time
def make_fitness_function(data):
    data = np.array(data)  # capture once

    def fitness_function(ga_instance, solution, solution_idx):
        labels = np.array(solution, dtype=int)
        n_unique = len(np.unique(labels))
        if n_unique < 2 or n_unique == len(labels):
            return -1.0
        return silhouette_score(data, labels)

    return fitness_function


class GAEngine(BaseClustering):
    """
    A Genetic Algorithm based clustering engine for tabular data.
    Each gene represents the cluster label for one data point (row).
    The GA maximizes the silhouette score over generations.
    """

    def __init__(self, data, n_clusters: int, num_generations=100, sol_per_pop=20):
        """
        Parameters
        ----------
        data : np.ndarray or pd.DataFrame, shape (N, M)
            Input feature matrix — N samples, M features.
        n_clusters : int
            Number of target clusters K.
        num_generations : int
            Number of GA generations to run.
        sol_per_pop : int
            Number of candidate solutions (chromosomes) per generation.
        """
        self.data = data#np.array(data)
        self.n_clusters = n_clusters
        self.num_generations = num_generations
        self.sol_per_pop = sol_per_pop
        self.labels_ = None

        # Each gene = cluster label for one row; values in {1, 2, ..., K}
        gene_space = list(range(1, n_clusters + 1))

        self.model = pygad.GA(
            num_generations=num_generations,
            sol_per_pop=sol_per_pop,
            num_genes=len(self.data),  # One gene per data point
            gene_space=gene_space,  # Valid cluster labels
            gene_type=int,
            mutation_percent_genes=10,
            fitness_func=make_fitness_function(data),
            # Keep best solutions across generations
            keep_elitism=2,
            # Stop early if fitness plateaus
            stop_criteria="saturate_15",
        )

    def fit(self, data=None):
        """
        Run the GA and store best cluster labels.

        Returns
        -------
        self
        """
        self.model.run()
        best_solution, best_fitness, _ = self.model.best_solution()
        # Convert from 1-indexed labels to 0-indexed
        self.labels_ = np.array(best_solution, dtype=int) - 1
        return self

    def predict(self, data=None):
        """Return cluster labels from the best solution found."""
        if self.labels_ is None:
            raise RuntimeError("Call fit() before predict().")
        return self.labels_

    def plot_fitness(self):
        """Plot fitness (silhouette score) progression across generations."""
        self.model.plot_fitness(title="Silhouette Score per Generation")
