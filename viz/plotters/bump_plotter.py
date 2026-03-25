from __future__ import annotations
import abc
from typing import Literal
from collections import defaultdict

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# ------------- helpers -------------
def validate_df(df: pd.DataFrame):
    required = {"year", "name", "rank"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {required - set(df.columns)}")


def get_title_statement(gender, page_name):
    if page_name == "names_surnames" and st.session_state["name_surname_rb"] == "Surname":
        title_statement = "Surnames"
    else:
        title_statement = "Names"

    if page_name == "baby_names":
        title_statement = "Baby " + title_statement

    if len(gender) == 1 and title_statement != "Surnames":
        gender = gender[0]
        title_statement = " " + gender.capitalize() + " " + title_statement

    return title_statement


# ------------- base -------------
class BumpPlotter(abc.ABC):
    ENGINE: str

    def __init__(self, gender: str, page_name: str):
        self.gender = gender
        self.page_name = page_name
        self.title = self._build_title()

    def _build_title(self) -> str:
        return f"Rank Evolution of {get_title_statement(self.gender, self.page_name)} Over Years"

    @abc.abstractmethod
    def plot(
        self,
        df: pd.DataFrame,
        col_plot: st.delta_generator.DeltaGenerator,
    ) -> None:
        pass


# ------------- matplotlib implementation -------------
class MatplotlibBumpPlotter(BumpPlotter):
    ENGINE = "matplotlib"

    def plot(self, df: pd.DataFrame, col_plot):

        df_pivot = pd.pivot_table(
            df,
            values="rank",
            index="year",
            columns="name",
            aggfunc=lambda x: x,
            dropna=False
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        cmap = plt.cm.get_cmap("tab20", 20)
        colors = [cmap(i) for i in range(20)]

        # --- draw segmented lines ---
        for i, name in enumerate(df_pivot.columns):
            color = colors[i % len(colors)]
            series = df_pivot[name]
            # Identify all non-NaN segments, including single points
            not_nan = series.notna()
            segments = []
            current_segment = []

            for year, valid in zip(series.index, not_nan):
                if valid:
                    current_segment.append((year, series.loc[year]))
                else:
                    if current_segment:
                        segments.append(current_segment)
                    current_segment = []
            if current_segment:
                segments.append(current_segment)

            for j, segment in enumerate(segments):
                years, ranks = zip(*segment)
                ax.plot(
                    years,
                    ranks,
                    marker="o",
                    markersize=8,
                    linewidth=2,
                    alpha=0.7,
                    color=color,
                    label=name if j == 0 else None
                )

        # --- axis formatting ---
        max_rank = int(df["rank"].max())

        ax.invert_yaxis()
        ax.set_yticks(range(1, min(51, max_rank + 1)))
        ax.set_ylim(min(51, max_rank + 1), 0)

        ax.set_xticks(df_pivot.index)
        ax.margins(x=0.15, y=0.1)

        fig.tight_layout(pad=2.0)

        ax.set_title(self.title, fontsize=20, pad=20)
        ax.set_xlabel("Year")
        ax.set_ylabel("Rank")
        ax.grid(True, alpha=0.3)

        ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

        # --- endpoint labels ---
        y_offset_first = defaultdict(int)
        y_offset_last = defaultdict(int)

        for name in df_pivot.columns:
            first_rank = df_pivot[name].iloc[0]
            last_rank = df_pivot[name].iloc[-1]

            first_year = df_pivot.index[0]
            last_year = df_pivot.index[-1]

            offset_f = y_offset_first[first_rank] * 0.2
            offset_l = y_offset_last[last_rank] * 0.2

            ax.text(first_year - 0.1, first_rank + offset_f, name,
                    ha="right", va="center", fontsize=9, alpha=0.7)

            ax.text(last_year + 0.1, last_rank + offset_l, name,
                    ha="left", va="center", fontsize=9, alpha=0.7)

            y_offset_first[first_rank] += 1
            y_offset_last[last_rank] += 1

        col_plot.pyplot(fig)
        plt.close(fig)


# ------------- factory -------------
ENGINES: dict[str, type[BumpPlotter]] = {
    cls.ENGINE: cls
    for cls in (
        MatplotlibBumpPlotter,
    )
}


def get_bump_plotter(
    engine: Literal["matplotlib"],
    gender: str,
    page_name: str,
) -> BumpPlotter:
    return ENGINES[engine](gender, page_name)