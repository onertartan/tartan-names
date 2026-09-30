from adjustText import adjust_text
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import streamlit as st
import numpy as np
import pandas as pd


class PCAPlotter:
    def apply_clr(self, df: pd.DataFrame, pseudocount: float = 1e-10) -> pd.DataFrame:
        """
        Apply centered log-ratio (CLR) transformation row-wise.

        Assumptions:
        - Rows = names
        - Columns = provinces
        - Values are non-negative frequencies or proportions
        - Each row represents a compositional profile over provinces
        """
        if (df < 0).any().any():
            raise ValueError("CLR requires non-negative values.")

        x = df + pseudocount
        log_x = np.log(x)
        row_means = log_x.mean(axis=1)
        clr_values = log_x.sub(row_means, axis=0)
        return clr_values

    def plot_pca(
        self,
        df_pivot: pd.DataFrame,
        df_clusters: pd.Series,
        dense_threshold: int,
        mid_threshold: int,
        colors,
        title: str = "",
        raw_label: str = "Share-normalized",
        clr_label: str = "CLR-transformed",
        annotate: bool = True,
        show_loadings: bool = True,
        n_loadings: int = 5,
        point_alpha: float = 0.90,
        same_axis_limits: bool = False,
        n_components: int = 2,
    ):
        """
        Flexible PCA visualization: 2D or 3D scatter.

        When n_components == 3: shows a single 3D plot.
        When n_components == 2:
        - if df_pivot has no negative values, shows raw and CLR side by side
        - if df_pivot has negative values, shows only the raw PCA panel
        """
        if n_components not in (2, 3):
            st.warning(f"n_components={n_components} not supported; falling back to 2D")
            n_components = 2

        if not df_clusters.index.equals(df_pivot.index):
            df_clusters = df_clusters.reindex(df_pivot.index)

        has_negative_values = (df_pivot < 0).any().any()
        x_raw = df_pivot
        x_clr = self.apply_clr(df_pivot) if n_components == 2 and not has_negative_values else None

        unique_clusters = sorted(df_clusters.dropna().unique())
        cluster_to_color = {cid: colors[i % len(colors)] for i, cid in enumerate(unique_clusters)}
        point_colors = df_clusters.map(cluster_to_color).fillna("gray")

        legend_handles = [
            plt.Line2D(
                [],
                [],
                marker="o",
                linestyle="",
                color=cluster_to_color[cid],
                markersize=8,
                label=f"Cluster {cid}",
            )
            for cid in unique_clusters
        ]

        if n_components == 2:
            n_panels = 1 if has_negative_values else 2
            fig_width = 7 if n_panels == 1 else 14
            fig, axes = plt.subplots(1, n_panels, figsize=(fig_width, 6), constrained_layout=True)
            axes = np.atleast_1d(axes)

            def _plot_2d_panel(ax, x, panel_title, x_label="", y_label=""):
                pca = PCA(n_components=2)
                scores = pca.fit_transform(x)
                pc1, pc2 = pca.explained_variance_ratio_[:2]

                ax.scatter(
                    scores[:, 0],
                    scores[:, 1],
                    c=point_colors,
                    edgecolors="w",
                    linewidths=0.5,
                    alpha=point_alpha,
                    s=60,
                )
                if x_label == "":
                    ax.set_xlabel(f"PC1 ({pc1:.2%})")
                    ax.set_ylabel(f"PC2 ({pc2:.2%})")
                else:
                    ax.set_xlabel(x_label, fontsize=9)
                    ax.set_ylabel(y_label, fontsize=9)
                ax.set_title(f"{panel_title} | PC1+PC2 = {(pc1 + pc2):.2%}", fontsize=11)
                ax.grid(True, alpha=0.3)

                if annotate:
                    texts = []
                    cluster_counts = df_clusters.value_counts()
                    for i, name in enumerate(df_pivot.index):
                        cid = df_clusters.loc[name]
                        size = cluster_counts.get(cid, 0)
                        if size >= dense_threshold:
                            continue
                        if size >= mid_threshold and i % 5 != 0:
                            continue
                        texts.append(
                            ax.annotate(
                                name,
                                (scores[i, 0], scores[i, 1]),
                                fontsize=8,
                                alpha=0.7,
                            )
                        )
                    if texts:
                        adjust_text(texts, ax=ax)

                if show_loadings:
                    load = pd.DataFrame(
                        pca.components_.T,
                        columns=["PC1", "PC2"],
                        index=x.columns,
                    )
                    for pc in ["PC1", "PC2"]:
                        top = load[pc].abs().nlargest(n_loadings)
                        print(f"\n[{panel_title}] Top |{pc}| loadings:")
                        for feat, val in top.items():
                            print(f"  {feat:20} {val:.3f}")

                return scores, pca

            x_label = ""
            y_label = ""
            scores_raw, pca_raw = _plot_2d_panel(axes[0], x_raw, raw_label, x_label, y_label)

            scores_clr = None
            pca_clr = None
            if not has_negative_values:
                scores_clr, pca_clr = _plot_2d_panel(axes[1], x_clr, clr_label)

            display_pca_loadings(x_raw, n_components=2, top_n=10)
            axes[-1].legend(handles=legend_handles, title="Clusters", loc="best")

            if same_axis_limits and scores_clr is not None:
                all_x = np.concatenate([scores_raw[:, 0], scores_clr[:, 0]])
                all_y = np.concatenate([scores_raw[:, 1], scores_clr[:, 1]])
                xpad = 0.05 * (all_x.ptp() + 1e-12)
                ypad = 0.05 * (all_y.ptp() + 1e-12)
                xlim = (all_x.min() - xpad, all_x.max() + xpad)
                ylim = (all_y.min() - ypad, all_y.max() + ypad)
                for ax in axes:
                    ax.set_xlim(xlim)
                    ax.set_ylim(ylim)
        else:
            fig = plt.figure(figsize=(12, 10))
            ax = fig.add_subplot(111, projection="3d")

            pca = PCA(n_components=3)
            scores = pca.fit_transform(x_raw)

            pc_var = pca.explained_variance_ratio_
            total_var = pc_var.sum()

            ax.scatter(
                scores[:, 0],
                scores[:, 1],
                scores[:, 2],
                c=point_colors,
                edgecolors="w",
                linewidths=0.6,
                alpha=point_alpha,
                s=70,
            )

            ax.set_xlabel(f"PC1 ({pc_var[0]:.2%})")
            ax.set_ylabel(f"PC2 ({pc_var[1]:.2%})")
            ax.set_zlabel(f"PC3 ({pc_var[2]:.2%})")
            ax.set_title(
                f"3D PCA - {title or 'Provinces'}\nExplained variance: {total_var:.2%}",
                fontsize=13,
            )
            ax.view_init(elev=20, azim=75)

            if annotate:
                cluster_counts = df_clusters.value_counts()
                for i, name in enumerate(df_pivot.index):
                    cid = df_clusters.loc[name]
                    size = cluster_counts.get(cid, 0)
                    if size >= dense_threshold * 1.3:
                        continue
                    if size >= mid_threshold and i % 4 != 0:
                        continue
                    ax.text(
                        scores[i, 0],
                        scores[i, 1],
                        scores[i, 2],
                        name,
                        fontsize=8,
                        alpha=0.65,
                    )

            ax.legend(handles=legend_handles, title="Clusters", loc="upper right", bbox_to_anchor=(1.15, 1))
            ax.grid(True, alpha=0.25)

            pca_raw = pca
            pca_clr = None

        if title:
            fig.suptitle(title, fontsize=14, y=1.05)

        pca_full = PCA().fit(df_pivot)
        per_var = np.round(pca_full.explained_variance_ratio_ * 100, 1)
        cum_var = per_var.cumsum()

        fig_scree, ax_scree = plt.subplots(figsize=(8, 4))
        ax_scree.plot(range(1, len(per_var) + 1), cum_var, marker="o", linestyle="--", color="teal")
        ax_scree.set_xlabel("Number of Components")
        ax_scree.set_ylabel("Cumulative Explained Variance (%)")
        ax_scree.set_title("Explained Variance by Number of Components")
        ax_scree.grid(True, alpha=0.3)
        ax_scree.legend()
        fig_scree.savefig("temp/pca2.png", dpi=300, bbox_inches="tight")
        st.pyplot(fig_scree)
        fig.savefig("temp/pca1.png", dpi=300, bbox_inches="tight")
        st.pyplot(fig)

        return fig, (pca_raw, pca_clr)


def display_pca_loadings(df_features, n_components=2, top_n=10):
    """
    Fit PCA, extract feature loadings, and display top positive/negative
    contributors per component as side-by-side Streamlit dataframes.
    """
    pca = PCA(n_components=n_components)
    pca.fit(df_features)

    component_labels = [f"PC{i + 1}" for i in range(n_components)]
    loadings = pd.DataFrame(
        pca.components_.T,
        index=df_features.columns,
        columns=component_labels,
    )

    variance_ratios = pca.explained_variance_ratio_

    for pc in component_labels:
        st.subheader(f"{pc} - explained variance: {variance_ratios[component_labels.index(pc)] * 100:.1f}%")
        col_name = loadings[pc].index.name or "feature"

        top_pos = (
            loadings[pc]
            .nlargest(top_n)
            .reset_index()
            .rename(columns={loadings[pc].index.name or "index": col_name, pc: "loading"})
        )
        top_pos["rank"] = range(1, len(top_pos) + 1)
        top_pos["loading"] = top_pos["loading"].round(4)

        top_neg = (
            loadings[pc]
            .nsmallest(top_n)
            .reset_index()
            .rename(columns={loadings[pc].index.name or "index": col_name, pc: "loading"})
        )
        top_neg["rank"] = range(1, len(top_neg) + 1)
        top_neg["loading"] = top_neg["loading"].round(4)

        top_combined = pd.concat(
            [top_pos.add_suffix("_pos"), top_neg.add_suffix("_neg")],
            axis=1,
        )[["rank_pos", col_name + "_pos", "loading_pos", col_name + "_neg", "loading_neg"]]

        top_combined = top_combined.rename(
            columns={
                "rank_pos": "rank",
                col_name + "_pos": col_name + " (+)",
                "loading_pos": "loading (+)",
                col_name + "_neg": col_name + " (-)",
                "loading_neg": "loading (-)",
            }
        )

        st.dataframe(top_combined, hide_index=True, use_container_width=True)

    return loadings, variance_ratios
