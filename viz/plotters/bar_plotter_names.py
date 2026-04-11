from __future__ import annotations
import abc
from typing import Literal

import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import matplotlib.ticker as ticker
from viz.gui_helpers.base_page_names.render_helpers import get_title_statement
from utils.base_page_names.names_helpers import validate_df


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

        names = df["name"].unique()
        n = len(names)

        fig, axes = plt.subplots(nrows=n, ncols=1, figsize=(10, 3*n), sharex=True)
        if n == 1:
            axes = [axes]

        years = sorted(df["year"].unique())
        start, end = years[0], years[-1]

        for ax, name in zip(axes, names):
            sub = df[df["name"] == name]
            ax.bar(sub["year"], sub[show_column])
            ax.set_title(name, fontsize=10)

            # ✅ key part
            ax.set_xticks([start, end])
            ax.set_xticklabels([str(start), str(end)])

        axes[-1].set_xlabel("Year")
        fig.suptitle(self.title)
        fig.tight_layout()

        col_plot.pyplot(fig)
        plt.close(fig)



class SeabornPlotter(BarPlotter):
    ENGINE = "Seaborn"

    def plot(self, df, col_plot, show_column):
        df = self._prepare_df(df)

        g = sns.FacetGrid(
            df,
            col="name",
            col_wrap=4,
            sharey=False,
            height=3.5
        )

        g.map_dataframe(
            sns.barplot,
            x="year",
            y=show_column,
            color="steelblue"
        )

        # Tick thinning
        for ax in g.axes.flat:
            labels = ax.get_xticklabels()
            n = len(labels)

            if n > 10:
                step = max(1, n // 6)
                for i, label in enumerate(labels):
                    if i % step != 0:
                        label.set_visible(False)

            ax.tick_params(axis='x', rotation=45)

        for ax in g.axes.flat:
            ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=5))
        g.set_titles("{col_name}")
        g.set_axis_labels("Year", show_column.title())

        g.figure.suptitle(self.title, y=1.02)

        col_plot.pyplot(g.figure)
        plt.close(g.figure)
# Plotly
class PlotlyPlotter(BarPlotter):
    ENGINE = "Plotly"

    def plot(self, df, col_plot, show_column):
        df = self._prepare_df(df)

        fig = px.bar(
            df,
            x="year",
            y=show_column,
            facet_col="name",
            facet_col_wrap=4,
            facet_col_spacing=0.04,
            title=self.title
        )
        years = sorted(list(df["year"].unique()))
        start, end = years[0], years[-1]

        n_ticks = 6  # configurable
        ticks = np.linspace(start, end, n_ticks)
        selected_years = [int(tick) for tick in ticks]

        if years[0] not in selected_years:
            selected_years.insert(0, years[0])
        if years[-1] not in selected_years:
            selected_years.append(years[-1])

        fig.update_xaxes(
            tickmode="array",
            tickvals=selected_years,
            ticktext=[str(y) for y in selected_years]
        )
        fig.update_layout(showlegend=False)

        col_plot.plotly_chart(fig, use_container_width=True)
# ------------- altair -------------
class AltairPlotter(BarPlotter):
    ENGINE = "Altair"

    def plot(self, df, col_plot, show_column="count", height=600):
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