from __future__ import annotations

from typing import Sequence

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def line_plotter_name_clusters(
    pivot_df: pd.DataFrame,
    clusters_df: pd.DataFrame,
    col_plot=None,
    title: str = "Name Clusters Over Time",
) -> None:
    """
    Plot each cluster in a separate panel.

    Each name is drawn as a faint line, while the cluster mean is emphasized.
    """
    if pivot_df.empty or clusters_df.empty:
        st.info("No cluster line plot can be drawn for the current data.")
        return

    year_index = pivot_df.index
    cluster_ids = clusters_df["cluster"].dropna().sort_values().unique().tolist()
    if not cluster_ids:
        st.info("No clusters available for line plotting.")
        return

    n_clusters = len(cluster_ids)
    fig, axes = plt.subplots(
        n_clusters,
        1,
        figsize=(12, max(3, 2.8 * n_clusters)),
        sharex=True,
    )
    if n_clusters == 1:
        axes = [axes]

    fig.suptitle(title, fontsize=14, y=0.995)

    for ax, cluster_id in zip(axes, cluster_ids):
        cluster_names = clusters_df.loc[clusters_df["cluster"] == cluster_id, "name"].tolist()
        cluster_data = pivot_df[cluster_names]

        for name in cluster_names:
            ax.plot(
                year_index,
                pivot_df[name],
                color="steelblue",
                alpha=0.25,
                linewidth=1.2,
                zorder=1,
            )

        cluster_mean = cluster_data.mean(axis=1)
        ax.plot(
            year_index,
            cluster_mean,
            color="black",
            linewidth=3,
            label="Cluster mean",
            zorder=3,
        )

        ax.set_title(f"Cluster {cluster_id} ({len(cluster_names)} names)")
        ax.set_ylabel("Ratio")
        ax.grid(True, alpha=0.2)
        ax.legend(loc="upper left")

    axes[-1].set_xlabel("Year")
    fig.tight_layout(rect=[0, 0, 1, 0.98])

    if col_plot is not None:
        col_plot.pyplot(fig, use_container_width=True)
    else:
        st.pyplot(fig, use_container_width=True)
    plt.close(fig)
