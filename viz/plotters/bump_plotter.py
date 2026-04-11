from __future__ import annotations
import abc
from typing import Literal
from collections import defaultdict
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import altair as alt
from viz.gui_helpers.base_page_names.render_helpers import get_title_statement
from utils.base_page_names.names_helpers import validate_df


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
            *args
    ) -> None:
        pass


# ------------- matplotlib implementation -------------
class MatplotlibBumpPlotter(BumpPlotter):
    ENGINE = "Matplotlib"
    # show_column is not used (added for compatibility with bar plotters which accept 3 parameters)

    def plot(self, df: pd.DataFrame, col_plot: st.delta_generator.DeltaGenerator,show_column:str):
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

        for i, name in enumerate(df_pivot.columns):
            color = colors[i % len(colors)]
            series = df_pivot[name]
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
                    years, ranks,
                    marker="o", markersize=8, linewidth=2,
                    alpha=0.7, color=color,
                    label=name if j == 0 else None
                )

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

# ------------- plotly implementation -------------
class PlotlyBumpPlotter(BumpPlotter):
    ENGINE = "Plotly"

    def plot(self, df: pd.DataFrame, col_plot: st.delta_generator.DeltaGenerator,show_column:str) -> None:
        # show_column is not used (added for compatibility with bar plotters which accept 3 parameters)
        validate_df(df)
        max_rank = int(df["rank"].max())
        df_reset = df.reset_index() if isinstance(df.index, pd.MultiIndex) else df.copy()

        fig = px.line(
            df_reset,
            x="year",
            y="rank",
            color="name",
            markers=True,
        ).update_layout(
            width=1500,
            height=800,
            xaxis_title="Year",
            yaxis_title="Rank",
            margin=dict(l=120, r=120, t=80, b=50),  # wider margins for endpoint labels
            legend=dict(orientation="v", yanchor="top", y=1.02, xanchor="right", x=1.15),
            title=dict(
                text=self.title,
                font=dict(size=20),          # 50 → 20
                automargin=True,
                yref="paper"
            ),
            yaxis_title_font=dict(size=14),  # 32 → 14
            xaxis_title_font=dict(size=14),  # 32 → 14
        ).update_yaxes(
            tickvals=list(range(1, max_rank + 1)),
            range=[max_rank + 0.5, 0.5],
            autorange="reversed",
            dtick=1,
            tickfont=dict(size=12),          # 32 → 12
        ).update_xaxes(
            showline=True,
            tickfont=dict(size=12),          # 32 → 12
        ).update_traces(
            line=dict(width=2),              # 5.5 → 2
            marker=dict(size=8),             # 30 → 8
        )

        # --- endpoint annotations ---
        years = df_reset["year"].unique()
        first_year = years.min()
        last_year = years.max()

        for name in df_reset["name"].unique():
            first_row = df_reset[(df_reset["name"] == name) & (df_reset["year"] == first_year)]
            if not first_row.empty:
                fig.add_annotation(
                    x=first_year,
                    y=first_row["rank"].iloc[0],
                    text=name,
                    showarrow=False,
                    xshift=-40,              # -20 → -40 to clear wider margin
                    font=dict(size=11),      # 20 → 11
                    xanchor="right",
                )
                # Data for the last year
            last_year_data = df_reset[(df_reset["name"] == name) & (df_reset["year"] == last_year)]
            if not last_year_data.empty:
                fig.add_annotation(
                    x=last_year,
                    y=last_year_data["rank"].iloc[0],
                    text=name,
                    showarrow=False,
                    xshift=40,               # 20 → 40
                    font=dict(size=11),      # 20 → 11
                    xanchor="left",
                )

        col_plot.plotly_chart(fig, use_container_width=True)

# ------------- seaborn implementation -------------
class SeabornBumpPlotter(BumpPlotter):
    ENGINE = "Seaborn"

    def plot(self, df: pd.DataFrame, col_plot: st.delta_generator.DeltaGenerator, show_column:str) -> None:
        # show_column is not used (added for compatibility with bar plotters which accept 3 parameters)
        validate_df(df)
        df_pivot = pd.pivot_table(
            df, values="rank", index="year", columns="name",
            aggfunc=lambda x: x, dropna=False
        )

        fig, ax = plt.subplots(figsize=(10, 6))
        palette = sns.color_palette("tab20", len(df_pivot.columns))

        for i, name in enumerate(df_pivot.columns):
            series = df_pivot[name].dropna()
            sns.lineplot(
                x=series.index, y=series.values,
                ax=ax, color=palette[i], marker="o",
                markersize=8, linewidth=2, label=name
            )

        max_rank = int(df["rank"].max())
        ax.invert_yaxis()
        ax.set_yticks(range(1, min(51, max_rank + 1)))
        ax.set_ylim(min(51, max_rank + 1), 0)
        ax.set_xticks(df_pivot.index)
        ax.margins(x=0.15, y=0.1)
        ax.set_title(self.title, fontsize=20, pad=20)
        ax.set_xlabel("Year")
        ax.set_ylabel("Rank")
        ax.grid(True, alpha=0.3)
        ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

        # --- endpoint labels ---
        y_offset_first = defaultdict(int)
        y_offset_last = defaultdict(int)

        for name in df_pivot.columns:
            series = df_pivot[name].dropna()
            if series.empty:
                continue
            first_year, last_year = series.index[0], series.index[-1]
            first_rank, last_rank = series.iloc[0], series.iloc[-1]

            ax.text(first_year - 0.1, first_rank + y_offset_first[first_rank] * 0.2,
                    name, ha="right", va="center", fontsize=9, alpha=0.7)
            ax.text(last_year + 0.1, last_rank + y_offset_last[last_rank] * 0.2,
                    name, ha="left", va="center", fontsize=9, alpha=0.7)

            y_offset_first[first_rank] += 1
            y_offset_last[last_rank] += 1

        fig.tight_layout(pad=2.0)
        col_plot.pyplot(fig)
        plt.close(fig)

# ------------- altair implementation -------------
class AltairBumpPlotter(BumpPlotter):
    ENGINE = "Altair"

    def plot(self, df: pd.DataFrame, col_plot: st.delta_generator.DeltaGenerator,show_column:str) -> None:
        # show_column is not used (added for compatibility with bar plotters which accept 3 parameters)
        validate_df(df)
        max_rank = int(df["rank"].max())

        base = alt.Chart(df).encode(
            x=alt.X("year:O", title="Year", axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
            y=alt.Y("rank:Q", title="Rank",
                    scale=alt.Scale(domain=[max_rank + 0.3, 0.3]),
                    axis=alt.Axis(tickCount=max_rank, labelFontSize=12, titleFontSize=14)),
            color=alt.Color("name:N", legend=alt.Legend(title="Name")),
        )

        lines = base.mark_line(strokeWidth=2)
        points = base.mark_point(filled=True, size=60)

        # endpoint labels — first year
        first_year = df["year"].min()
        last_year = df["year"].max()

        first_labels = alt.Chart(df[df["year"] == first_year]).mark_text(
            align="right", dx=-8, dy=-12,fontSize=11
        ).encode(
            x=alt.X("year:O"),
            y=alt.Y("rank:Q"),
            text=alt.Text("name:N"),
            color=alt.Color("name:N", legend=None),
        )

        last_labels = alt.Chart(df[df["year"] == last_year]).mark_text(
            align="left", dx=8, fontSize=11
        ).encode(
            x=alt.X("year:O"),
            y=alt.Y("rank:Q"),
            text=alt.Text("name:N"),
            color=alt.Color("name:N", legend=None),
        )

        chart = (lines + points + first_labels + last_labels).properties(
            width=1000, height=500,
            title=alt.TitleParams(text=self.title, fontSize=20, anchor="middle")
        ).configure_legend(padding=10)
        col_plot.altair_chart(chart, use_container_width=True)

# ------------- factory -------------
ENGINES: dict[str, type[BumpPlotter]] = {
    cls.ENGINE: cls
    for cls in (
        MatplotlibBumpPlotter,
        SeabornBumpPlotter,
        PlotlyBumpPlotter,
        AltairBumpPlotter,
    )
}

def get_bump_plotter(
        engine: Literal["Matplotlib", "Seaborn", "Plotly", "Altair"],
        gender: str,
        page_name: str,
) -> BumpPlotter:
    return ENGINES[engine](gender, page_name)