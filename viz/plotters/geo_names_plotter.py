from __future__ import annotations
import abc
import base64
import hashlib
import io
import json
from typing import Literal
import matplotlib.colors as mcolors
import geopandas as gpd
import numpy as np
import streamlit as st
import plotly.express as px
import altair as alt
import folium
from PIL import Image
from folium.features import GeoJsonTooltip
from matplotlib.patches import Patch
from streamlit_folium import st_folium
from shapely.geometry import Polygon, box
import vl_convert as vlc

import matplotlib.pyplot as plt
import pandas as pd
from adjustText import adjust_text
from viz.gui_helpers.base_page_names.plot_helpers import build_legend_entries, set_color_mapping
from turkish_string import upper_tr

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

def _adaptive_simplify(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Compute simplification tolerance relative to the data's bounding box.
    Targets ~200 vertices per feature on average, regardless of country or scale.
    0.1% of the shorter bounding box dimension is visually safe at screen resolution.
    """
    minx, miny, maxx, maxy = gdf.total_bounds
    span = min(maxx - minx, maxy - miny)   # shorter axis in degrees
    tolerance = span * 0.001               # 0.1% of span
    gdf = gdf.copy()
    gdf["geometry"] = gdf["geometry"].buffer(0)
    gdf["geometry"] = gdf["geometry"].simplify(
        tolerance=tolerance, preserve_topology=True
    )
    return gdf
def _clip_and_plot(ax, gdf, polygon):
    clipped = gdf.clip(polygon)
    clipped.plot(
        ax=ax,
        color=clipped["color"],
        edgecolor="black",
        linewidth=0.2
    )
    return clipped


def _build_label(row, geo_level):
    region_code = state_map_reversed.get(row[geo_level], row[geo_level])
    region_code=upper_tr(region_code)
    name = row.get("name")

    if isinstance(name, str) and name.strip():
        return f"{region_code}\n{name}"

    return region_code


def _plotly_map_height(gdf: gpd.GeoDataFrame, geo_level: str) -> int:
    if geo_level == "state":
        return 900#680

    minx, miny, maxx, maxy = gdf.total_bounds
    center_lat = (miny + maxy) / 2
    lon_span = max((maxx - minx) * np.cos(np.radians(center_lat)), 1e-9)
    lat_span = max(maxy - miny, 1e-9)
    aspect = lon_span / lat_span
    return int(max(900, min(760, 960 / aspect)))


def _configure_plotly_geos(fig, geo_level: str) -> None:
    if geo_level == "state":
        fig.update_geos(
            scope="usa",
            projection_type="albers usa",
            visible=False,
            showframe=False,
            showcoastlines=False,
        )
        # Keep the map vertically centered inside the figure.
        # Leave a little space for the title, but avoid a large top gap.
       # fig.update_geos(domain={"x": [0.0, 1.0], "y": [0.02, 0.94]})
        return

    fig.update_geos(
        fitbounds="locations",
        projection_type="mercator",
        visible=False,
        showframe=False,
        showcoastlines=False,
    )
    # Keep the map vertically centered inside the figure.
    # Leave a little space for the title, but avoid a large top gap.
    fig.update_geos(domain={"x": [0.0, 1.0], "y": [0.02, 0.94]})

def _annotate(ax, gdf, geo_level):
    bbox = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.6)
    texts = []
    for _, row in gdf.iterrows():
        centroid = row.geometry.centroid
        texts.append(
            ax.text(
                centroid.x,
                centroid.y,
                _build_label(row, geo_level),
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

    def __init__(self, ha_positions, va_positions, cluster_color_mapping):
        self.ha_positions        = ha_positions
        self.va_positions        = va_positions
        self.cluster_color_mapping = cluster_color_mapping
        self._figure             = None   # each subclass stores its rendered object here

    @abc.abstractmethod
    def plot(self, df_result, title, col_plot, geo_level) -> None:
        pass

    @abc.abstractmethod
    def to_jpeg_bytes(self) -> bytes:
        """Return 300 DPI JPEG bytes of the last rendered figure."""
        pass

    def render_download_button(self, title: str, col=None, data_hash: str = "") -> None:
        """
        Render a download button for the last plotted figure.
        Uses session_state cache so download clicks don't retrigger
        expensive re-renders.
        """
        raw = f"{self.ENGINE}_{title}_{data_hash}"
        cache_key = f"dl_{hashlib.md5(raw.encode()).hexdigest()}"
        if st.session_state.get(cache_key + "_engine") != self.ENGINE or \
           cache_key not in st.session_state:
            st.session_state[cache_key]            = self.to_jpeg_bytes()
            st.session_state[cache_key + "_engine"] = self.ENGINE

        target = col if col else st
        target.download_button(
            label=f"⬇ Download as JPEG (300 DPI)",
            data=st.session_state[cache_key],
            file_name=f"{title.replace(' ', '_')}.jpg",
            mime="image/jpeg",
        )

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
            text = _build_label(row, geo_level)

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
        if geo_level=="state":
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
        # # Add a table (positioned like a legend)
        df_count = (df_main['name'].str.split('\n')  # Split names by newline
                    .explode()  # Create separate row for each name
                    .value_counts()  # Count occurrences
                    .rename_axis('name')
                    .reset_index(name='count')
                    )
        # Format the DataFrame as a string for the legend
        legend_text = "\n".join(f"{row['name']}: {row['count']}" for _, row in df_count.iterrows())
        # Create list of text entries instead of single multi-line string
        legend_entries = [f"{row['name']}: {row['count']}" for _, row in df_count.iterrows()]
        # Add custom legend entry with text only (no line): Create invisible handles for each entry
        handles = [Patch(color='none', label=entry, linewidth=0) for entry in legend_entries]
        ax.plot([], [], label=legend_text)  # Invisible plot
        # Show legend
        ncols = 1 + len(legend_entries) // 9
        ax.legend(handles=handles, loc='upper right', bbox_to_anchor=(1, 0.165 if ncols > 2 else 0.21), fontsize=4,
                  ncols=ncols,  # Two columns
                  # Reduce left margin parameters:
                  handlelength=0,  # Remove space for legend handle (invisible line)
                  handletextpad=0,  # Remove padding between handle and text
                  alignment='left'  # Force left-aligned text
                  )
        # FIXED — store before closing
        self._figure = fig
        col_plot.pyplot(fig)
        fig.savefig("temp/eps/X.pdf", format="pdf",dpi=300, bbox_inches="tight")
        plt.close(fig)

    def to_jpeg_bytes(self) -> bytes:
        buf = io.BytesIO()
        self._figure.savefig(
            buf,
            format="jpeg",
            dpi=300,
            bbox_inches="tight",
            pil_kwargs={"quality": 95},
        )
        buf.seek(0)
        return buf.getvalue()

# ------------- plotly -------------
class PlotlyMapPlotter(MapPlotter):
    ENGINE = "Plotly"

    def plot(self, df_result, title, col_plot, geo_level):
        df_result = set_color_mapping(df_result, self.cluster_color_mapping).copy()
        if df_result.crs is not None and df_result.crs.to_epsg() != 4326:
            df_result = df_result.to_crs("EPSG:4326")
        df_result = _adaptive_simplify(df_result)

        cache_key = "plotly_fig_v2_" + hashlib.md5(
            (
                df_result[[geo_level, "name"]].to_csv()
                + title
                + geo_level
                + str(df_result.total_bounds.tolist())
            ).encode()
        ).hexdigest()

        if cache_key not in st.session_state:
            df_result["_plot_id"] = df_result.index.astype(str)
            geojson = df_result.__geo_interface__

            fig = px.choropleth(
                df_result,
                geojson=geojson,
                locations="_plot_id",
                featureidkey="properties._plot_id",
                color="name",
                color_discrete_map=dict(zip(df_result["name"], df_result["color"])),
                hover_data={geo_level: True, "name": True, "_plot_id": False},
                title=title,
            )
            #_configure_plotly_geos(fig, geo_level)
            fig.update_traces(marker_line_color="black", marker_line_width=0.6)
            fig.update_layout(
                height=1120
            )
            st.session_state[cache_key] = fig

        self._figure = st.session_state[cache_key]
        # Apply layout/projection tweaks even when the figure comes from cache.
        _configure_plotly_geos(self._figure, geo_level)


        col_plot.plotly_chart(self._figure, use_container_width=True)
    def to_jpeg_bytes(self) -> bytes:
        import plotly.io as pio
        # scale=3.125 → 300 DPI relative to 96 DPI screen baseline
        return pio.to_image(
            self._figure,
            format="jpg",
            scale=3.125,
            engine="kaleido",
        )
# ------------- altair -------------
class AltairMapPlotter(MapPlotter):
    ENGINE = "Altair"

    def plot(self, df_result, title, col_plot, geo_level):
        df_result = set_color_mapping(df_result, self.cluster_color_mapping).copy()

        if df_result.crs is not None and df_result.crs.to_epsg() != 4326:
            df_result = df_result.to_crs("EPSG:4326")

        # --- Geometry repairs ---
        df_result = _adaptive_simplify(df_result)

        # --- Clip outlying island chains ---
        if geo_level == "state":
            ak_box = box(-170, 50, -140, 72)
            hi_box = box(-161, 18, -154, 23)
            mask_ak = df_result["state"] == "Alaska"
            mask_hi = df_result["state"] == "Hawaii"
            df_result.loc[mask_ak, "geometry"] = (
                df_result.loc[mask_ak, "geometry"].intersection(ak_box)
            )
            df_result.loc[mask_hi, "geometry"] = (
                df_result.loc[mask_hi, "geometry"].intersection(hi_box)
            )
            df_result = df_result[~df_result["geometry"].is_empty]

        # --- Colors ---
        df_result["color"] = df_result["color"].apply(
            lambda c: mcolors.to_hex(c) if pd.notna(c) else "#cccccc"
        )

        chart_data = df_result[[geo_level, "name", "color", "geometry"]].copy()
        chart_data["display_name"] = (
            chart_data["name"]
            .fillna("No data")
            .astype(str)
            .str.replace("\n", " ", regex=False)
        )

        # --- Compute centroids for text labels (must be done before dropping geometry) ---
        # Use largest polygon centroid for MultiPolygon states (avoids centroid
        # falling in the ocean for states like Michigan or Hawaii)
        def safe_centroid(geom):
            if geom.geom_type == "MultiPolygon":
                largest = max(geom.geoms, key=lambda p: p.area)
                return largest.centroid
            return geom.centroid

        chart_data["centroid_lon"] = chart_data["geometry"].apply(
            lambda g: safe_centroid(g).x
        )
        chart_data["centroid_lat"] = chart_data["geometry"].apply(
            lambda g: safe_centroid(g).y
        )

        # Two-line label: abbreviation on top, name below
        chart_data["label"] = chart_data.apply(
            lambda row: (
                    state_map_reversed.get(row[geo_level], row[geo_level])
                    + "\n"
                    + row["display_name"]
            ),
            axis=1,
        )

        # --- GeoJSON for choropleth layer ---
        geojson_bytes = chart_data.to_json().encode("utf-8")
        geojson_url = "data:application/json;base64," + base64.b64encode(
            geojson_bytes
        ).decode("ascii")
        geojson_data = alt.Data(
            url=geojson_url,
            format=alt.DataFormat(type="json", property="features"),
        )

        proj_type = "albersUsa" if geo_level == "state" else "mercator"

        # --- Layer 1: choropleth shapes ---
        map_chart = (
            alt.Chart(geojson_data)
            .mark_geoshape(stroke="white", strokeWidth=0.6)
            .encode(
                fill=alt.Fill("properties.color:N", scale=None),
                tooltip=[
                    alt.Tooltip(f"properties.{geo_level}:N", title=geo_level.title()),
                    alt.Tooltip("properties.display_name:N", title="Name"),
                ],
            )
            .properties(
               width=1050,
                 height=700,
                title=alt.TitleParams(text=title, fontSize=16, anchor="middle"),
            )
            .project(type=proj_type)
        )

        # --- Layer 2: text annotations ---
        # Use a plain DataFrame (not GeoDataFrame) — geometry column must be absent
        # so Vega-Lite doesn't try to render it as a shape.
        text_df = pd.DataFrame(chart_data[[geo_level, "label", "centroid_lon", "centroid_lat"]])

        text_layer = (
            alt.Chart(text_df)
            .mark_text(
                fontSize=8,
                fontWeight="bold",
                lineBreak="\n",  # enables two-line labels
                color="black",
                baseline="middle",
                align="center",
                # Semi-transparent white halo so text stays readable over dark fills
                font="sans-serif",
            )
            .encode(
                longitude="centroid_lon:Q",  # Altair projects these through proj_type
                latitude="centroid_lat:Q",
                text="label:N",
                tooltip=[
                    alt.Tooltip(f"{geo_level}:N", title=geo_level.title()),
                    alt.Tooltip("label:N", title="Name"),
                ],
            )
            .project(type=proj_type)
        )

        # --- Layer both charts ---
        layered = (map_chart + text_layer).resolve_scale(color="independent")

        # --- Manual legend ---
        color_lookup = (
            chart_data.drop_duplicates("display_name")
            .set_index("display_name")["color"]
            .to_dict()
        )
        legend_df = pd.DataFrame(
            [{"Name": k, "color": v} for k, v in color_lookup.items()]
        )
        legend = (
            alt.Chart(legend_df)
            .mark_square(size=120)
            .encode(
                x=alt.value(10),
                y=alt.Y("Name:N", axis=alt.Axis(labelLimit=200, title=None)),
                color=alt.Color("color:N", scale=None),
            )
            .properties(title="Legend", width=40)
        )

        combined = (
            (layered | legend)
            .configure_view(strokeWidth=0)
        )

        # --- Cache the spec to avoid re-serializing on every Streamlit re-run ---
        # Key: hash of the underlying data + title so we recompute only when data changes
        cache_key = hashlib.md5(
            (chart_data[["display_name", "color"]].to_csv() + title).encode()
        ).hexdigest()

        if st.session_state.get("altair_spec_key") != cache_key:
            st.session_state["altair_spec_key"] = cache_key
            st.session_state["altair_spec_json"] = combined.to_json()


        self._figure = combined  # ← store before rendering

        col_plot.vega_lite_chart(
            json.loads(st.session_state["altair_spec_json"]),
            use_container_width=True,
        )

    def to_jpeg_bytes(self) -> bytes:
        """
                Render an Altair chart to a 300 DPI JPEG byte string.

                Scale factor math:
                  - Vega-Lite renders at 96 DPI (standard screen resolution)
                  - To reach 300 DPI: scale = 300 / 96 ≈ 3.125
                  - A 900px-wide chart becomes 900 * 3.125 = 2812px at 300 DPI
        """
        scale= 3.125
        quality = 95
        # 1. Render to PNG (vl-convert's most stable format)
        png_bytes = vlc.vegalite_to_png(self._figure.to_dict(), scale=scale)

        # 2. Open with Pillow and flatten transparency
        #    JPEG does not support alpha channel — paste onto white background
        img = Image.open(io.BytesIO(png_bytes))
        if img.mode in ("RGBA", "LA", "P"):
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = background
        else:
            img = img.convert("RGB")

        # 3. Save as JPEG with DPI metadata embedded
        output = io.BytesIO()
        img.save(output, format="JPEG", quality=quality, dpi=(300, 300))
        return output.getvalue()

# ------------- folium -------------
class FoliumMapPlotter(MapPlotter):
    ENGINE = "Folium"

    def plot(
        self,
        df_result: gpd.GeoDataFrame,
        title: str,
        col_plot: st.delta_generator.DeltaGenerator,
        geo_level: str
    ) -> None:
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
                    fields=[geo_level, "name"],
                    aliases=[f"{geo_level.title()}:", "Name:"],
                    localize=True,
                ),
            ).add_to(m)

        # region + name labels as div markers
        for _, row in df_result.iterrows():
            centroid_pt = row.geometry.centroid
            region_code = state_map_reversed.get(row[geo_level], row[geo_level]).upper()
            label = f"{region_code}\n{row['name'].title()}" \
                    if isinstance(row["name"], str) else region_code
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
        self._figure = m
        with col_plot:
            st_folium(m, use_container_width=True, height=600, returned_objects=[])

    def to_jpeg_bytes(self) -> bytes:
        # Folium has no server-side raster renderer.
        # Callers should use render_download_button(as_html=True) instead.
        raise NotImplementedError("Use to_html_bytes() for Folium maps.")

    def to_html_bytes(self) -> bytes:
        return self._figure.get_root().render().encode("utf-8")

    def render_download_button(self, title: str, col=None, data_hash: str = "") -> None:
        """Override: Folium downloads as interactive HTML, not JPEG."""
        raw = f"folium_{title}_{data_hash}"
        cache_key = f"dl_{hashlib.md5(raw.encode()).hexdigest()}"
        if cache_key not in st.session_state:
            st.session_state[cache_key] = self.to_html_bytes()

        target = col if col else st
        target.download_button(
            label="⬇ Download as Interactive HTML",
            data=st.session_state[cache_key],
            file_name=f"{title.replace(' ', '_')}.html",
            mime="text/html",
        )


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
