from abc import ABC, abstractmethod

import pandas as pd
from pandas import DataFrame
from sklearn.datasets import make_blobs


class SyntheticDataGenerator(ABC):
    def __init__(self, kwargs):
        self.kwargs = kwargs
        self.ground_truth_labels = None

    @abstractmethod
    def generate(self) -> pd.DataFrame:
        pass


class BlobsSyntheticDataGenerator(SyntheticDataGenerator):
    def generate(self) -> tuple[DataFrame, DataFrame]:
        x_values, ground_truth_values = make_blobs(**self.kwargs)
        self.ground_truth_labels = ground_truth_values
        return pd.DataFrame(x_values), ground_truth_values
