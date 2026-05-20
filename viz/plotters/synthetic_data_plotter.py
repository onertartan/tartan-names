import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from scipy.optimize import linear_sum_assignment


class SyntheticDataPlotter:
    @staticmethod
    def _match_labels(predicted_labels, ground_truth_labels):
        predicted_labels = np.asarray(predicted_labels)
        ground_truth_labels = np.asarray(ground_truth_labels)

        unique_true = np.unique(ground_truth_labels)
        unique_pred = np.unique(predicted_labels)
        confusion = np.zeros((len(unique_true), len(unique_pred)), dtype=int)
        for row, true_label in enumerate(unique_true):
            for col, pred_label in enumerate(unique_pred):
                confusion[row, col] = np.sum(
                    (ground_truth_labels == true_label) & (predicted_labels == pred_label)
                )

        cost_matrix = confusion.max() - confusion
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        label_mapping = {unique_pred[col]: unique_true[row] for row, col in zip(row_ind, col_ind)}
        aligned_predicted = np.array([label_mapping.get(label, label) for label in predicted_labels])
        return aligned_predicted, label_mapping

    def plot_synthetic_data(self, df_pivot: pd.DataFrame, ground_truth_values: pd.Series = None, plot_comparison_with_ground_truth: bool = False ):
        feature_columns = [column for column in df_pivot.columns if column != "clusters"]
        if len(feature_columns) < 2:
            st.warning("Synthetic data plot requires at least two feature columns.")
            return

        x_col, y_col = feature_columns[:2]
        predicted_labels = df_pivot["clusters"].to_numpy()
        ground_truth_array = None if ground_truth_values is None else np.asarray(ground_truth_values)
        show_ground_truth_comparison = plot_comparison_with_ground_truth and ground_truth_array is not None

        aligned_predicted = predicted_labels
        if show_ground_truth_comparison:
            aligned_predicted, _ = self._match_labels(predicted_labels, ground_truth_array)

        fig_pred, ax_pred = plt.subplots(figsize=(8, 6))
        scatter_pred = ax_pred.scatter(df_pivot[x_col], df_pivot[y_col], c=aligned_predicted, cmap="tab10", alpha=0.8, edgecolors="white",linewidths=0.4)
        ax_pred.set_title("Predicted Clusters")
        ax_pred.set_xlabel(str(x_col))
        ax_pred.set_ylabel(str(y_col))
        ax_pred.grid(True, alpha=0.25)
        legend_pred = ax_pred.legend(
            *scatter_pred.legend_elements(),
            title="Clusters",
            loc="upper left",
            bbox_to_anchor=(1.02, 1.0),
            borderaxespad=0.0,
        )
        ax_pred.add_artist(legend_pred)

        if show_ground_truth_comparison:
            matches = aligned_predicted == ground_truth_array
            mismatches = ~matches
            matching_count = int(matches.sum())
            mismatching_count = int(mismatches.sum())

            ax_pred.scatter(
                df_pivot.loc[mismatches, x_col],
                df_pivot.loc[mismatches, y_col],
                marker="x",
                c="black",
                s=40,
                linewidths=1.2,
                label="Mismatch",
            )
            summary_text = (
                f"Matches: {matching_count}\n"
                f"x Mismatches: {mismatching_count}"
            )
            ax_pred.text(
                0.02,
                0.98,
                summary_text,
                transform=ax_pred.transAxes,
                va="top",
                ha="left",
                fontsize=9,
                bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.85},
            )
        if show_ground_truth_comparison:
            col1, col2 = st.columns(2)
            col1.pyplot(fig_pred)
        else:
            col1, col2 = st.columns([7,3])

            col1.pyplot(fig_pred)

        if not show_ground_truth_comparison:
            return

        fig_gt, ax_gt = plt.subplots(figsize=(8, 6))
        scatter_gt = ax_gt.scatter(
            df_pivot[x_col],
            df_pivot[y_col],
            c=ground_truth_values,
            cmap="tab10",
            alpha=0.8,
            edgecolors="white",
            linewidths=0.4,
        )
        ax_gt.set_title("Ground Truth Labels")
        ax_gt.set_xlabel(str(x_col))
        ax_gt.set_ylabel(str(y_col))
        ax_gt.grid(True, alpha=0.25)
        legend_gt = ax_gt.legend(*scatter_gt.legend_elements(), title="Labels", loc="best")
        ax_gt.add_artist(legend_gt)
        col2.pyplot(fig_gt)
