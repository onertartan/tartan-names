from matplotlib import pyplot as plt
import streamlit as st
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st
from scipy.cluster.hierarchy import dendrogram

def plot_dendrogram(linkage_matrix, n_cluster, labels):
    col1, _ = st.columns([8, 2])
    with col1:
        n_names = len(labels)
        if n_cluster <= 1 or n_cluster >= n_names:
            st.warning(
                f"n_cluster must be between 2 and {n_names - 1}"
            )
            return None
        # Guard against edge cases
        merge_heights = linkage_matrix[:, 2]
        cutoff_idx = np.clip(n_names - n_cluster, 1, len(merge_heights) - 1)
        lower = merge_heights[cutoff_idx - 1]
        upper = merge_heights[cutoff_idx]
        cluster_cutoff = (lower + upper) / 2

        fig, ax = plt.subplots(figsize=(12, 5))
        dendrogram(
            linkage_matrix,
            labels=labels,
            color_threshold=cluster_cutoff,
            leaf_rotation=90,
            ax=ax,
        )
        ax.axhline(cluster_cutoff, color="red", linestyle="--", linewidth=1)
        ax.text(
            0.99, 0.98,
            f"k = {n_cluster}  |  cut = {cluster_cutoff:.3f}",
            transform=ax.transAxes,
            ha="right", va="top", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
        )
        ax.set_title("Hierarchical Clustering Dendrogram")
        ax.set_xlabel("Name")
        ax.set_ylabel("Distance")
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

