from __future__ import annotations
import abc
from typing import Literal

import pandas as pd
import geopandas as gpd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import plotly.express as px
import altair as alt
import folium
from folium.features import GeoJsonTooltip
from streamlit_folium import st_folium

from viz.plotters.names_helpers import build_legend_entries, create_title_for_plot, prepare_df


# ------------- base -------------
class MapPlotter(abc.ABC):
    ENGINE: str

    def __init__(self, ha_positions: dict, va_positions: dict, cluster_color_mapping: dict):
        self.ha_positions = ha_positions
        self.va_positions = va_positions
        self.cluster_color_mapping = cluster_color_mapping

    @abc.abstractmethod
    def plot(
        self,
        df_result: gpd.GeoDataFrame,
        rank: int,
        year: int,
        display_option: str,
        page_name: str,
        col_plot: st.delta_generator.DeltaGenerator,
    ) -> None:
        pass


# ------------- matplotlib -------------
class MatplotlibMapPlotter(MapPlotter):
    ENGINE = "Matplotlib"

    def plot(
        self,
        df_result: gpd.GeoDataFrame,
        rank: int,
        year: int,
        display_option: str,
        page_name: str,
        col_plot: st.delta_generator.DeltaGenerator,
    ) -> None:
        title, _ = create_title_for_plot(rank, year, display_option, page_name)
        df_result = prepare_df(df_result, self.cluster_color_mapping)

        fig, ax = plt.subplots(figsize=(10, 8))

        df_result.plot(
            ax=ax, color=df_result["color"],
            edgecolor="black", linewidth=0.2
        )

        bbox = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.6)
        df_result.apply(lambda x: ax.annotate(
            text=x["province"].upper() + "\n" + x["name"].title()
                 if isinstance(x["name"], str) else x["province"],
            size=4,
            xy=x.geometry.centroid.coords[0],
            ha=self.ha_positions.get(x["province"], "center"),
            va=self.va_positions.get(x["province"], "center"),
            bbox=bbox,
        ), axis=1)

        ax.axis("off")
        ax.margins(x=0)

        legend_entries = build_legend_entries(df_result)
        handles = [Patch(color="none", label=entry, linewidth=0) for entry in legend_entries]
        ncols = 1 + len(legend_entries) // 9
        ax.legend(
            handles=handles,
            loc="upper right",
            bbox_to_anchor=(1, 0.165 if ncols > 2 else 0.21),
            fontsize=4,
            ncols=ncols,
            handlelength=0,
            handletextpad=0,
            alignment="left",
        )
        ax.set_title(title)

        col_plot.pyplot(fig)
        plt.close(fig)


# ------------- plotly -------------
class PlotlyMapPlotter(MapPlotter):
    ENGINE = "plotly"

    def plot(
        self,
        df_result: gpd.GeoDataFrame,
        rank: int,
        year: int,
        display_option: str,
        page_name: str,
        col_plot: st.delta_generator.DeltaGenerator,
    ) -> None:
        title, _ = create_title_for_plot(rank, year, display_option, page_name)
        df_result = prepare_df(df_result, self.cluster_color_mapping)
        df_result["id"] = df_result["province"]
        geojson = df_result.__geo_interface__

        fig = px.choropleth(
            df_result,
            geojson=geojson,
            locations="id",
            color="name",
            color_discrete_map=dict(zip(df_result["name"], df_result["color"])),
            hover_data={"province": True, "name": True, "id": False},
            title=title,
        )
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(
            title_font_size=16,
            title_x=0.5,
            legend_title_text="Name",
            margin=dict(l=0, r=0, t=50, b=0),
        )
        col_plot.plotly_chart(fig, use_container_width=True)


# ------------- altair -------------
class AltairMapPlotter(MapPlotter):
    ENGINE = "altair"

    def plot(
        self,
        df_result: gpd.GeoDataFrame,
        rank: int,
        year: int,
        display_option: str,
        page_name: str,
        col_plot: st.delta_generator.DeltaGenerator,
    ) -> None:
        title, _ = create_title_for_plot(rank, year, display_option, page_name)
        df_result = prepare_df(df_result, self.cluster_color_mapping)

        geojson_data = alt.Data(values=df_result.__geo_interface__["features"])
        color_lookup = dict(zip(df_result["name"], df_result["color"]))
        domain = list(color_lookup.keys())
        range_ = list(color_lookup.values())

        chart = alt.Chart(geojson_data).mark_geoshape(
            stroke="black", strokeWidth=0.2
        ).encode(
            color=alt.Color(
                "properties.name:N",
                scale=alt.Scale(domain=domain, range=range_),
                legend=alt.Legend(title="Name"),
            ),
            tooltip=[
                alt.Tooltip("properties.province:N", title="Province"),
                alt.Tooltip("properties.name:N", title="Name"),
            ],
        ).project(
            type="mercator"
        ).properties(
            width=700,
            height=500,
            title=alt.TitleParams(text=title, fontSize=16, anchor="middle"),
        )

        col_plot.altair_chart(chart, use_container_width=True)


# ------------- folium -------------
class FoliumMapPlotter(MapPlotter):
    ENGINE = "folium"

    def plot(
        self,
        df_result: gpd.GeoDataFrame,
        rank: int,
        year: int,
        display_option: str,
        page_name: str,
        col_plot: st.delta_generator.DeltaGenerator,
    ) -> None:
        title, _ = create_title_for_plot(rank, year, display_option, page_name)
        df_result = prepare_df(df_result, self.cluster_color_mapping)

        centroid = df_result.geometry.union_all().centroid
        m = folium.Map(
            location=[centroid.y, centroid.x],
            zoom_start=6,
            tiles="CartoDB positron",
        )

        # floating title
        title_html = f"""
            <div style="position: fixed; top: 10px; left: 50%; transform: translateX(-50%);
                        z-index: 1000; background: white; padding: 6px 14px;
                        border-radius: 6px; font-size: 15px; font-weight: bold;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.2);">
                {title}
            </div>
        """
        m.get_root().html.add_child(folium.Element(title_html))

        # one layer per name for LayerControl toggle support
        for name, group in df_result.groupby("name"):
            color = group["color"].iloc[0]
            folium.GeoJson(
                data=group.__geo_interface__,
                name=name,
                style_function=lambda _, c=color: {
                    "fillColor": c,
                    "color": "black",
                    "weight": 0.4,
                    "fillOpacity": 0.7,
                },
                tooltip=GeoJsonTooltip(
                    fields=["province", "name"],
                    aliases=["Province:", "Name:"],
                    localize=True,
                ),
            ).add_to(m)

        # province + name labels as div markers
        for _, row in df_result.iterrows():
            centroid_pt = row.geometry.centroid
            label = f"{row['province'].upper()}\n{row['name'].title()}" \
                    if isinstance(row["name"], str) else row["province"].upper()
            folium.Marker(
                location=[centroid_pt.y, centroid_pt.x],
                icon=folium.DivIcon(
                    html=f"""<div style="font-size:7px; font-weight:bold;
                                        text-align:center; white-space:pre-line;
                                        background:rgba(255,255,255,0.6);
                                        border-radius:3px; padding:1px 3px;">
                                {label}
                             </div>""",
                    icon_size=(60, 30),
                    icon_anchor=(30, 15),
                ),
            ).add_to(m)

        folium.LayerControl(collapsed=False).add_to(m)

        # floating legend
        legend_entries = build_legend_entries(df_result)
        legend_items_html = "".join(
            f"""<div style="display:flex; align-items:center; gap:6px; margin:2px 0;">
                    <div style="width:12px; height:12px; border-radius:2px;
                                background:{
                                    df_result[df_result['name'] == e.split(':')[0].strip()]['color'].iloc[0]
                                    if e.split(':')[0].strip() in df_result['name'].values else 'gray'
                                };
                                flex-shrink:0;"></div>
                    <span style="font-size:11px;">{e}</span>
                </div>"""
            for e in legend_entries
        )
        legend_html = f"""
            <div style="position: fixed; bottom: 30px; right: 10px; z-index: 1000;
                        background: white; padding: 10px; border-radius: 6px;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.2); max-height: 300px;
                        overflow-y: auto; min-width: 140px;">
                <b style="font-size:12px;">Names</b>
                {legend_items_html}
            </div>
        """
        m.get_root().html.add_child(folium.Element(legend_html))

        with col_plot:
            st_folium(m, use_container_width=True, height=600, returned_objects=[])


# ------------- factory -------------
ENGINES: dict[str, type[MapPlotter]] = {
    cls.ENGINE: cls
    for cls in (
        MatplotlibMapPlotter,
        PlotlyMapPlotter,
        AltairMapPlotter,
        FoliumMapPlotter,
    )
}


def get_map_plotter(
    engine: Literal["Matplotlib", "plotly", "altair", "folium"],
    ha_positions: dict,
    va_positions: dict,
    cluster_color_mapping: dict,
) -> MapPlotter:
    return ENGINES[engine](ha_positions, va_positions, cluster_color_mapping)