import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


class SyntheticDataPlotter:
    def plot(self, df_pivot: pd.DataFrame):
        col1, _ = st.columns([7,3])
        feature_columns = [column for column in df_pivot.columns if column != "clusters"]
        if len(feature_columns) < 2:
            st.warning("Synthetic data plot requires at least two feature columns.")
            return

        x_col, y_col = feature_columns[:2]
        fig, ax = plt.subplots(figsize=(8, 6))
        scatter = ax.scatter(
            df_pivot[x_col],
            df_pivot[y_col],
            c=df_pivot["clusters"],
            cmap="tab10",
            alpha=0.8,
            edgecolors="white",
            linewidths=0.4,
        )
        ax.set_title("Synthetic Blob Clusters")
        ax.set_xlabel(str(x_col))
        ax.set_ylabel(str(y_col))
        ax.grid(True, alpha=0.25)
        legend = ax.legend(*scatter.legend_elements(), title="Clusters", loc="best")
        ax.add_artist(legend)
        col1.pyplot(fig)
