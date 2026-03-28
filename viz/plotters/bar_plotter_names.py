from __future__ import annotations
import abc
from typing import Literal
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
from viz.gui_helpers.base_page_names.render_helpers import get_title_statement, validate_df


# ------------- base -------------
class BarPlotter(abc.ABC):
    ENGINE: str

    def __init__(self, gender: str, page_name: str):
        self.gender = gender
        self.page_name = page_name
        self.title = self._build_title()

    def _build_title(self) -> str:
        return f"Frequency of {get_title_statement(self.gender, self.page_name)} by Year"

    @abc.abstractmethod
    def plot(
        self,
        df: pd.DataFrame,
        col_plot: st.delta_generator.DeltaGenerator,
    ) -> None:
        """Draw the chart inside the supplied Streamlit column."""


# ------------- matplotlib -------------
class MatplotlibPlotter(BarPlotter):
    ENGINE = "Matplotlib"

    def plot(self, df, col_plot):

        validate_df(df)

        pivot_df = df.pivot(index="year", columns="name", values="count")

        fig, ax = plt.subplots(figsize=(15, 9))
        pivot_df.plot(kind="bar", ax=ax)

        ax.set_title(self.title)
        ax.set_xlabel("Year")
        ax.set_ylabel("Count")
        ax.tick_params(axis="x", rotation=0)

        for container in ax.containers:
            ax.bar_label(container, fontsize=8)

        col_plot.pyplot(fig)
        plt.close(fig)


# ------------- seaborn -------------
class SeabornPlotter(BarPlotter):
    ENGINE = "Seaborn"

    def plot(self, df, col_plot):

        validate_df(df)

        fig, ax = plt.subplots(figsize=(15, 9))
        palette = sns.color_palette("tab20", n_colors=df["name"].nunique())

        sns.barplot(
            data=df,
            x="year",
            y="count",
            hue="name",
            palette=palette,
            ax=ax
        )
        ax.set_title(self.title)
        ax.set_xlabel("Year")
        ax.set_ylabel("Count")
        ax.legend(loc="best")
        col_plot.pyplot(fig)
        plt.close(fig)


# ------------- plotly -------------
class PlotlyPlotter(BarPlotter):
    ENGINE = "Plotly"

    def plot(self, df, col_plot):

        validate_df(df)

        fig = px.bar(
            df,
            x="year",
            y="count",
            color="name",
            barmode="group",
            text="count",
            title=self.title
        )

        fig.update_traces(textposition="outside")

        col_plot.plotly_chart(fig, use_container_width=True)


# ------------- pandas -------------
class PandasPlotter(BarPlotter):
    ENGINE = "Pandas"

    def plot(self, df, col_plot):

        validate_df(df)

        pivot_df = df.pivot(index="year", columns="name", values="count")

        fig, ax = plt.subplots(figsize=(10, 6))
        pivot_df.plot(kind="bar", ax=ax)

        ax.set_title(self.title)
        ax.set_xlabel("Year")
        ax.set_ylabel("Count")

        col_plot.pyplot(fig)
        plt.close(fig)


# ------------- altair -------------
class AltairPlotter(BarPlotter):
    ENGINE = "Altair"

    def plot(
        self,
        df: pd.DataFrame,
        col_plot: st.delta_generator.DeltaGenerator,
        height: int = 600,
    ) -> None:

        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('year:O', title='Year'),
            y=alt.Y('count:Q', title='Count'),
            color=alt.Color('name:N', legend=None),
            column=alt.Column('name:N', title=None)
        ).properties(
            width=150,
            title={
                "text": self.title,
                "anchor": "middle",
                "dy": 4,
                "fontSize": 28
            }
        ).configure_header(
            labelFontSize=16,
            titleFontSize=24
        ).configure_axisX(
            labelFontSize=16,
            titleFontSize=16
        ).configure_axisY(
            labelFontSize=16,
            titleFontSize=16
        )

    #    chart.save("temp/rank_bar.png", scale_factor=3)
        col_plot.altair_chart(chart )


# ------------- factory -------------
ENGINES: dict[str, type[BarPlotter]] = {
    cls.ENGINE: cls
    for cls in (
        MatplotlibPlotter,
        SeabornPlotter,
        PlotlyPlotter,
        PandasPlotter,
        AltairPlotter,
    )
}


def get_bar_plotter(
    engine: Literal["Matplotlib", "Seaborn", "Plotly", "Pandas", "Altair"],
    gender: str,
    page_name: str,
) -> BarPlotter:
    return ENGINES[engine](gender, page_name)