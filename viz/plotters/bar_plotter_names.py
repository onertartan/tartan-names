from __future__ import annotations
import abc
from typing import Literal

import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import matplotlib.ticker as ticker
from viz.gui_helpers.base_page_names.plot_helpers import get_title_statement
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from viz.gui_helpers.base_page_names.validate_df import validate_df

_BAR_PALETTE = (
    "#4C78A8",  # blue
    "#F58518",  # orange
    "#E45756",  # red
    "#72B7B2",  # teal
    "#54A24B",  # green
    "#EECA3B",  # yellow
    "#B279A2",  # purple
    "#FF9DA6",  # pink
    "#9D755D",  # brown
    "#BAB0AC",  # gray
)


def _build_year_ticks(years: list[int], max_ticks: int = 12) -> list[int]:
    if len(years) <= max_ticks:
        return years

    step = max(1, (len(years) - 1) // (max_ticks - 1))
    ticks = years[::step]

    if ticks[0] != years[0]:
        ticks.insert(0, years[0])
    if ticks[-1] != years[-1]:
        ticks.append(years[-1])

    return ticks


def _panel_colors(n_panels: int) -> list[str]:
    return [_BAR_PALETTE[i % len(_BAR_PALETTE)] for i in range(n_panels)]


def _prepare_panel_matrix(df: pd.DataFrame, show_column: str) -> tuple[list[int], list[str], pd.DataFrame]:
    chart_df = df.loc[:, ["year", "name", show_column]].copy()
    chart_df["year"] = pd.to_numeric(chart_df["year"], errors="coerce")
    chart_df = chart_df.dropna(subset=["year", "name", show_column])
    chart_df["year"] = chart_df["year"].astype(int)

    years = sorted(chart_df["year"].unique().tolist())
    names = chart_df["name"].drop_duplicates().tolist()

    matrix = (
        chart_df.pivot_table(
            index="year",
            columns="name",
            values=show_column,
            aggfunc="sum",
            fill_value=0,
        )
        .reindex(index=years, columns=names, fill_value=0)
    )
    return years, names, matrix

class BarPlotter(abc.ABC):
    ENGINE: str

    def __init__(self, gender: str, page_name: str):
        self.gender = gender
        self.page_name = page_name
        self.title = self._build_title()

    def _build_title(self) -> str:
        return f"Frequency of {get_title_statement(self.gender, self.page_name)} by Year"

    def _prepare_df(self, df: pd.DataFrame) -> pd.DataFrame:
        validate_df(df)
        return df.sort_values(["name", "year"])

    @abc.abstractmethod
    def plot(
        self,
        df: pd.DataFrame,
        col_plot: st.delta_generator.DeltaGenerator,
        show_column: str
    ) -> None:
        pass

# ------------- matplotlib -------------
class MatplotlibPlotter(BarPlotter):
    ENGINE = "Matplotlib"

    def plot(self, df, col_plot, show_column="count"):
        df = self._prepare_df(df)

        if df.empty:
            col_plot.warning("No data available for the selected filters.")
            return

        if show_column not in df.columns:
            col_plot.error(f"Column '{show_column}' is not available in the dataframe.")
            return

        years, names, matrix = _prepare_panel_matrix(df, show_column)
        if matrix.empty or not names:
            col_plot.warning("No data available for the selected filters.")
            return

        colors = _panel_colors(len(names))
        fig_width = max(12, 2.35 * len(names))
        max_y = float(matrix.to_numpy().max())
        y_upper = max(1000, int(np.ceil(max_y / 1000.0) * 1000)) if show_column != "ratio" else None
        fig, axes = plt.subplots(
            1,
            len(names),
            figsize=(fig_width, 5.6),
            sharey=True,
        )
        axes = np.atleast_1d(axes).ravel()

        tick_years = _build_year_ticks(years)
        y_label = show_column.replace("_", " ").title()

        for idx, (ax, name) in enumerate(zip(axes, names)):
            values = matrix[name].to_numpy()
            ax.bar(years, values, color=colors[idx], width=0.85)
            ax.set_title(str(name), fontsize=12, pad=12)
            ax.set_xlabel("Year", fontsize=11, fontweight="bold")

            if idx == 0:
                ax.set_ylabel(y_label, fontsize=11, fontweight="bold")
                if show_column == "ratio":
                    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1.0))
                else:
                    ax.yaxis.set_major_locator(ticker.MultipleLocator(1000))
                    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
            else:
                ax.tick_params(axis="y", left=False, labelleft=False)

            ax.set_xticks(tick_years)
            ax.set_xticklabels([str(year) for year in tick_years], rotation=90)
            ax.tick_params(axis="x", labelsize=10)
            ax.grid(axis="y", alpha=0.18, linewidth=0.8)
            ax.set_axisbelow(True)
            ax.margins(x=0.02)
            for spine_name in ("left", "right", "top", "bottom"):
                spine = ax.spines[spine_name]
                spine.set_visible(True)
                spine.set_color("#B0B0B0")
                spine.set_alpha(0.35)
                spine.set_linewidth(0.8)

            if y_upper is not None:
                ax.set_ylim(0, y_upper)

        fig.suptitle(self.title, fontsize=24, fontweight="bold", y=0.98)
        fig.tight_layout(rect=(0, 0.02, 1, 0.92))

        col_plot.pyplot(fig)
        fig.savefig("temp/eps/Figure5b.pdf", format="pdf",dpi=300, bbox_inches="tight")

        plt.close(fig)



class SeabornPlotter(BarPlotter):
    ENGINE = "Seaborn"

    def plot(self, df, col_plot, show_column="count"):
        df = self._prepare_df(df)

        if df.empty:
            col_plot.warning("No data available for the selected filters.")
            return

        if show_column not in df.columns:
            col_plot.error(f"Column '{show_column}' is not available in the dataframe.")
            return

        years, names, matrix = _prepare_panel_matrix(df, show_column)
        if matrix.empty or not names:
            col_plot.warning("No data available for the selected filters.")
            return

        colors = _panel_colors(len(names))
        fig_width = max(12, 2.35 * len(names))
        max_y = float(matrix.to_numpy().max())
        y_upper = max(1000, int(np.ceil(max_y / 1000.0) * 1000)) if show_column != "ratio" else None
        fig, axes = plt.subplots(
            1,
            len(names),
            figsize=(fig_width, 5.6),
            sharey=True,
        )
        axes = np.atleast_1d(axes).ravel()

        tick_years = _build_year_ticks(years)
        tick_positions = [years.index(year) for year in tick_years]
        y_label = show_column.replace("_", " ").title()

        for idx, (ax, name) in enumerate(zip(axes, names)):
            name_df = df[df["name"] == name]
            barplot_kwargs = dict(
                data=name_df,
                x="year",
                y=show_column,
                order=years,
                estimator=np.sum,
                color=colors[idx],
                ax=ax,
            )
            try:
                sns.barplot(**barplot_kwargs, errorbar=None)
            except TypeError:
                sns.barplot(**barplot_kwargs, ci=None)

            ax.set_title(str(name), fontsize=12, pad=12)
            ax.set_xlabel("Year", fontsize=11, fontweight="bold")
            if idx == 0:
                ax.set_ylabel(y_label, fontsize=11, fontweight="bold")
                if show_column == "ratio":
                    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1.0))
                else:
                    ax.yaxis.set_major_locator(ticker.MultipleLocator(1000))
                    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
            else:
                ax.tick_params(axis="y", left=False, labelleft=False)

            ax.set_xticks(tick_positions)
            ax.set_xticklabels([str(year) for year in tick_years], rotation=90)
            ax.tick_params(axis="x", labelsize=10)
            ax.grid(axis="y", alpha=0.18, linewidth=0.8)
            ax.set_axisbelow(True)
            ax.margins(x=0.02)
            for spine_name in ("left", "right", "top", "bottom"):
                spine = ax.spines[spine_name]
                spine.set_visible(True)
                spine.set_color("#B0B0B0")
                spine.set_alpha(0.35)
                spine.set_linewidth(0.8)

            if y_upper is not None:
                ax.set_ylim(0, y_upper)

        fig.suptitle(self.title, fontsize=24, fontweight="bold", y=0.98)
        fig.tight_layout(rect=(0, 0.02, 1, 0.92))

        col_plot.pyplot(fig)
        plt.close(fig)
# Plotly
class PlotlyPlotter(BarPlotter):
    ENGINE = "Plotly"

    def plot(self, df: pd.DataFrame, col_plot: st.delta_generator.DeltaGenerator, show_column: str) -> None:
        df = self._prepare_df(df)

        names = df["name"].unique().tolist()
        n_cols = len(names)

        fig = make_subplots(
            rows=1,
            cols=n_cols,
            subplot_titles=names,
        )

        for i, name in enumerate(names, start=1):
            name_df = df[df["name"] == name]
            fig.add_trace(
                go.Bar(
                    x=name_df["year"],
                    y=name_df[show_column],
                    name=name,
                ),
                row=1,
                col=i,
            )

        fig.update_layout(
            title=dict(
                text=self.title,
                x=0.5,
                xanchor="center",
                font=dict(size=20),
            ),
            showlegend=False,
            xaxis_title="Year",
            yaxis_title=show_column.title(),
        )

        # Apply "Year" and "Count" axis labels to every subplot
        for i in range(1, n_cols + 1):
            x_key = "xaxis" if i == 1 else f"xaxis{i}"
            y_key = "yaxis" if i == 1 else f"yaxis{i}"
            fig.layout[x_key].update(title=dict(text="Year", font=dict(size=14)), tickfont=dict(size=12))
            if i==1:
                fig.layout[y_key].update(title=dict(text=show_column.title(), font=dict(size=14)), tickfont=dict(size=12))

        col_plot.plotly_chart(fig, use_container_width=True)
# ------------- altair -------------
class AltairPlotter(BarPlotter):
    ENGINE = "Altair"
    def plot(self,df,col_plot, show_column="count"):
        df = df.reset_index()
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('year:O', title='Year'),
            y=alt.Y('count:Q', title='Count'),
            color=alt.Color('name:N', legend=None),  # Remove legend
            column=alt.Column('name:N', title=None)
        ).properties(
            width=150,
        title = {  # Add title configuration
            "text": f"{show_column.title()} by Year",  # Title text
            "anchor": "middle",  # Center the title
            "dy": 4,  # Adjust vertical spacing (positive = move down)
            "fontSize": 28  # Adjust font size
        }
        ).configure_header(labelFontSize=16,
            titleFontSize=24,  # Increase font size for column titles (names)
        ).configure_axisX(labelFontSize=16, titleFontSize=16).configure_axisY(labelFontSize=16, titleFontSize=16)
        col_plot.altair_chart(chart)
    def plot_old(self, df, col_plot, show_column="count", height=600):
        df = self._prepare_df(df)

        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('year:O', title='Year'),
            y=alt.Y(f'{show_column}:Q', title=show_column.title()),
            column=alt.Column('name:N', title=None)
        ).properties(
            width=150,
            title=self.title
        )

        col_plot.altair_chart(chart)
# ------------- factory -------------
ENGINES: dict[str, type[BarPlotter]] = {
    cls.ENGINE: cls
    for cls in (
        MatplotlibPlotter,
        SeabornPlotter,
        PlotlyPlotter,
        AltairPlotter,
    )
}


def get_bar_plotter(
    engine: Literal["Matplotlib", "Seaborn", "Plotly", "Altair"],
    gender: str,
    page_name: str,
) -> BarPlotter:
    return ENGINES[engine](gender, page_name)
