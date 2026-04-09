from __future__ import annotations
import abc
from typing import Literal

import geopandas as gpd
import numpy as np
import streamlit as st
import plotly.express as px
import altair as alt
import folium
from folium.features import GeoJsonTooltip
from streamlit_folium import st_folium
from shapely.geometry import Polygon

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd
from adjustText import adjust_text
from viz.gui_helpers.base_page_names.render_helpers import build_legend_entries, create_title_for_plot, set_color_mapping
state_map_reversed = {
    'Alaska': 'AK', 'Alabama': 'AL', 'Arkansas': 'AR', 'Arizona': 'AZ',
    'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT',
    'District of Columbia': 'DC', 'Delaware': 'DE', 'Florida': 'FL',
    'Georgia': 'GA', 'Hawaii': 'HI', 'Iowa': 'IA', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Kansas': 'KS', 'Kentucky': 'KY',
    'Louisiana': 'LA', 'Massachusetts': 'MA', 'Maryland': 'MD',
    'Maine': 'ME', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Missouri': 'MO', 'Mississippi': 'MS', 'Montana': 'MT',
    'North Carolina': 'NC', 'North Dakota': 'ND', 'Nebraska': 'NE',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM',
    'Nevada': 'NV', 'New York': 'NY', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI',
    'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
    'Texas': 'TX', 'Utah': 'UT', 'Virginia': 'VA', 'Vermont': 'VT',
    'Washington': 'WA', 'Wisconsin': 'WI', 'West Virginia': 'WV',
    'Wyoming': 'WY'
}

def alaska_hawaii(gdf, fig, geo_level, ha_positions, va_positions):
    bbox = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.6)
    polygon = Polygon([(-170, 50), (-170, 72), (-140, 72), (-140, 50)])

    # Alaska inset
    akax = fig.add_axes([0.12, 0.19, 0.2, 0.2])
    akax.axis('off')
    alaska_gdf = gdf[gdf.state == 'Alaska']
    alaska_clipped = alaska_gdf.clip(polygon)
    alaska_clipped.plot(color=alaska_clipped["color"], linewidth=0.8, ax=akax, edgecolor='0.8')
    # Annotate Alaska regions inside the inset
    alaska_clipped.apply(lambda x: akax.annotate(
        text=x[geo_level].upper(),
        size=4,
        xy=x.geometry.centroid.coords[0],
        ha=ha_positions.get(x[geo_level], "center"),
        va=va_positions.get(x[geo_level], "center"),
        bbox=bbox,
    ), axis=1)

    # Hawaii inset
    hiax = fig.add_axes([.32, 0.22, 0.1, 0.15])
    hiax.axis('off')
    hipolygon = Polygon([(-160, 0), (-160, 90), (-120, 90), (-120, 0)])
    hawaii_gdf = gdf[gdf.state == 'Hawaii']
    hawaii_clipped = hawaii_gdf.clip(hipolygon)
    hawaii_clipped.plot(color=hawaii_clipped["color"], linewidth=0.8, ax=hiax, edgecolor='0.8')
    # Annotate Hawaii regions inside the inset
    hawaii_clipped.apply(lambda x: hiax.annotate(
        text=x[geo_level].upper(),
        size=4,
        xy=x.geometry.centroid.coords[0],
        ha=ha_positions.get(x[geo_level], "center"),
        va=va_positions.get(x[geo_level], "center"),
        bbox=bbox,
    ), axis=1)

import matplotlib.pyplot as plt
from shapely.geometry import Polygon

def _clip_and_plot(ax, gdf, polygon):
    clipped = gdf.clip(polygon)
    clipped.plot(
        ax=ax,
        color=clipped["color"],
        edgecolor="black",
        linewidth=0.2
    )
    return clipped
def _annotate(ax, gdf, geo_level):
    bbox = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.6)
    texts = []
    for _, row in gdf.iterrows():
        centroid = row.geometry.centroid
        texts.append(
            ax.text(
                centroid.x,
                centroid.y,
                row[geo_level].upper(),
                fontsize=4,
                ha="center",
                va="center",
                bbox=bbox
            )
        )
    adjust_text(
        texts,
        ax=ax,
        arrowprops=dict(arrowstyle="-", color="#888888", lw=0.4),
        expand_text=(1.1, 1.2),
        expand_points=(1.2, 1.2),
        force_text=(0.2, 0.4),
        force_points=(0.3, 0.5),
    )
def split_regions( df, geo_level):
    if geo_level != "state":
        return {"main": df}

    df_main = df[~df["state"].isin(["Alaska", "Hawaii"])]
    df_ak = df[df["state"] == "Alaska"]
    df_hi = df[df["state"] == "Hawaii"]

    return {
        "main": df_main,
        "alaska": df_ak,
        "hawaii": df_hi
    }
def draw_alaska_inset( fig, df_ak, geo_level):
    polygon = Polygon([(-170, 50), (-170, 72), (-140, 72), (-140, 50)])

    ax = fig.add_axes([0.12, 0.18, 0.2, 0.2])
    ax.axis("off")

    clipped = _clip_and_plot(ax, df_ak, polygon)
    _annotate(ax, clipped, geo_level)

def draw_hawaii_inset( fig, df_hi, geo_level):
    polygon = Polygon([(-160, 0), (-160, 90), (-120, 90), (-120, 0)])

    ax = fig.add_axes([0.32, 0.22, 0.1, 0.15])
    ax.axis("off")

    clipped = _clip_and_plot(ax, df_hi, polygon)
    _annotate(ax, clipped, geo_level)


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
        df_result: gpd.GeoDataFrame,title:str,
        col_plot: st.delta_generator.DeltaGenerator,
        geo_level:str
    ) -> None:
        pass


# ------------- matplotlib -------------

class MatplotlibMapPlotter(MapPlotter):
    ENGINE = "Matplotlib"

    def plot(self, gdf, title, col_plot, geo_level):
        df_view = set_color_mapping(gdf, self.cluster_color_mapping)
        regions = split_regions(df_view, geo_level)
        df_main = regions["main"]
        df_ak = regions.get("alaska")
        df_hi = regions.get("hawaii")

        # --- dynamic figure size ---
        bounds = df_main.total_bounds
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        aspect = width / height if height > 0 else 2.5

        fig, ax = plt.subplots(figsize=(10, max(8, 10 / aspect)))

        # --- MAINLAND ---
        df_main.plot(ax=ax, color=df_main["color"], edgecolor="black", linewidth=0.2)
        # --- INSETS ---
        if df_ak is not None and not df_ak.empty:
            draw_alaska_inset(fig, df_ak, geo_level)
        if df_hi is not None and not df_hi.empty:
            draw_hawaii_inset(fig, df_hi, geo_level)

        # --- LABELS (mainland only) ---
        bbox = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.6)
        texts = []
        for idx, row in df_main.iterrows():
            geom = row.geometry
            # Safety check for possible GeoSeries
            if isinstance(geom, gpd.GeoSeries):
                geom = geom.iloc[0]
            # Annotation text (as in the original second snippet)
            name = row["name"] if row["name"] is not np.nan else ""
            text = f"{state_map_reversed.get(row[geo_level],row[geo_level]).upper()}\n{name}"

            texts.append(
                ax.text(
                    geom.centroid.x,
                    geom.centroid.y,
                    text,
                    ha=self.ha_positions.get(row[geo_level], "center"),
                    va=self.va_positions.get(row[geo_level], "center"),
                    fontsize=4,
                    color="black",
                    bbox=bbox
                )
            )

        adjust_text(
            texts,
            ax=ax,
            arrowprops=dict(arrowstyle="-", color="#888888", lw=0.4),
            expand_text=(1.1, 1.2),
            expand_points=(1.2, 1.2),
            force_text=(0.2, 0.4),
            force_points=(0.3, 0.5),
        )

        ax.axis("off")
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
        geo_level: str
    ) -> None:
        title, _ = create_title_for_plot(rank, year, display_option, page_name)
        df_result = set_color_mapping(df_result, self.cluster_color_mapping)
        df_result["id"] = df_result[geo_level]
        geojson = df_result.__geo_interface__

        fig = px.choropleth(
            df_result,
            geojson=geojson,
            locations="id",
            color="name",
            color_discrete_map=dict(zip(df_result["name"], df_result["color"])),
            hover_data={geo_level: True, "name": True, "id": False},
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
        geo_level: str
    ) -> None:
        title, _ = create_title_for_plot(rank, year, display_option, page_name)
        df_result = set_color_mapping(df_result, self.cluster_color_mapping)

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
                alt.Tooltip(f"properties.{geo_level}:N", title=geo_level.title()),
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
        geo_level: str
    ) -> None:
        title, _ = create_title_for_plot(rank, year, display_option, page_name)
        df_result = set_color_mapping(df_result, self.cluster_color_mapping)

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
