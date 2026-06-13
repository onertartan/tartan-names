from matplotlib import pyplot as plt
import streamlit as st
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list


def plot_dendrogram(linkage_matrix,max_val_slider,labels):
    fig, ax = plt.subplots(figsize=(12, 5))
    cluster_cutoff = st.slider(
        "Dendrogram cut distance",
        min_value=0.0,
        max_value=max_val_slider,
        value=max_val_slider / 2,
        step=0.05,
    )
    # Dendrogram uses ORIGINAL order — correct
    dendrogram(
        linkage_matrix,
        labels=labels,
        color_threshold=cluster_cutoff,
        leaf_rotation=90,
        ax=ax,
    )
    ax.axhline(cluster_cutoff, color="red", linestyle="--", linewidth=1)
    ax.text(
        0.99,
        0.98,
        f"cut = {cluster_cutoff:.3f}",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )
    ax.set_title("Hierarchical Clustering Dendrogram")
    ax.set_xlabel("Name")
    ax.set_ylabel("Distance")
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    return cluster_cutoff