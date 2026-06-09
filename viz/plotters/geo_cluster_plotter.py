import matplotlib.pyplot as plt
from adjustText import adjust_text
from matplotlib.patches import Patch
import pandas as pd
import geopandas as gpd
import streamlit as st

from viz.color_mapping import create_cluster_color_mapping
from viz.plotters.geo_names_plotter import split_regions, draw_alaska_inset, draw_hawaii_inset, state_map_reversed


class GeoClusterPlotter:
    def __init__(self, cluster_color_mapping_dict, ha_positions, va_positions):
        """
        Initialize with configuration data.
        """
        self.cluster_color_mapping_dict = cluster_color_mapping_dict
        self.ha_positions = ha_positions
        self.va_positions = va_positions

    def create_color_mapping(self, gdf: gpd.GeoDataFrame, n_clusters: int):
        """Generate cluster color mapping with province-based defaults."""
        color_map = {}
        used_colors = set()
        clusters = set(range(1, n_clusters + 1))

        for idx, color in self.cluster_color_mapping_dict.items():
            if idx in gdf.index:
                # Handle potential Series return for index lookup
                val = gdf.loc[idx, "clusters"]
                cluster = val[0] if isinstance(val, pd.Series) else val

                if cluster not in color_map and color not in used_colors:
                    color_map[cluster] = color
                    used_colors.add(color)

        # Assign remaining colors
        remaining_colors = [c for c in self.cluster_color_mapping_dict.values() if c not in used_colors]
        remaining_clusters = clusters - set(color_map.keys())

        for i, cluster in enumerate(remaining_clusters):
            if i < len(remaining_colors):
                color_map[cluster] = remaining_colors[i]
            else:
                color_map[cluster] = "grey"  # Fallback
        return color_map

    def plot_cluster_map(self, gdf_clusters, gdf_centroids, n_clusters, year_label,geo_level):
        """
        Plots the geographic clusters.
        """
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
        # 1. Create Colors
        ##  color_map = self.create_color_mapping(gdf_clusters, n_clusters)
        color_map = create_cluster_color_mapping(gdf_clusters, self.cluster_color_mapping_dict)
        # 2. Map colors and Plot
        # gdf_clusters = gdf_clusters.copy()
        gdf_clusters["color"] = gdf_clusters["clusters"].map(color_map)
        # 3. Split regions
        regions = split_regions(gdf_clusters.reset_index(), geo_level)
        df_main = regions["main"]
        df_ak = regions.get("alaska")
        df_hi = regions.get("hawaii")
        # --- dynamic figure size ---
        bounds = df_main.total_bounds
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        aspect = width / height if height > 0 else 2.5

        fig, ax = plt.subplots(figsize=(10, max(8, 10 / aspect)))
        #--- MAINLAND - --
        df_main.plot(ax=ax, color=df_main["color"], legend=True, edgecolor="black", linewidth=0.2)
        # --- INSETS ---
        if df_ak is not None and not df_ak.empty:
            draw_alaska_inset(fig, df_ak, geo_level)
        if df_hi is not None and not df_hi.empty:
            draw_hawaii_inset(fig, df_hi, geo_level)

        ax.axis("off")
        ax.margins(x=0)
        # 3. Annotations
        bbox = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.6)
        texts = []
        for idx, row in df_main.iterrows():
            geom = row.geometry
            # Safety check for possible GeoSeries
            if isinstance(geom, gpd.GeoSeries):
                geom = geom.iloc[0]
            # Annotation text (as in the original second snippet)
            add_name = f"\n{row['name']}" if "name" in row else ""
            if geo_level =="state": # use uppercase for state names otherwise do not change(province names)
                text = f"{state_map_reversed.get(row[geo_level], row[geo_level].upper())}{add_name}"
            else:
                text =row[geo_level]# f"{state_map_reversed.get(row[geo_level], row[geo_level])}{add_name}"

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
        adjust_text_with_arrows= False # for pca?
        if adjust_text_with_arrows:
            adjust_text(
                texts,
                ax=ax,
                arrowprops=dict(arrowstyle="-", color="#888888", lw=0.4),
                expand_text=(1.1, 1.2),
                expand_points=(1.2, 1.2),
                force_text=(0.2, 0.4),
                force_points=(0.3, 0.5),
            )
        # 4. Legend & Centroid Markers
        title = f"{n_clusters} Clusters Identified {year_label}"
        ax.set_title(title)
        if gdf_centroids is not None:
            closest_provinces_centroids = gdf_centroids.to_crs("EPSG:4326")#gdf_centroids.to_crs("EPSG:4326").copy()
            closest_provinces_centroids["centroid_geometry"] = closest_provinces_centroids.geometry.centroid
            closest_points = gpd.GeoDataFrame(
                closest_provinces_centroids,
                geometry="centroid_geometry",
                crs=gdf_clusters.crs
            )
            closest_points.plot(ax=ax, facecolor="none", markersize=90,
                                edgecolor="black", linewidth=1.5,
                                label="Cluster representatives")
            ax.legend(loc="upper right", fontsize=6)
        fig.savefig(f"temp/result.png", dpi=300, bbox_inches="tight")
        fig.savefig("temp/eps/X.pdf", format="pdf",dpi=300, bbox_inches="tight")
        st.pyplot(fig)

    def plot_elections(self, gdf_clusters,n_clusters):
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
        # Define a color map for the categories
        # Map the colors to the GeoDataFrame
        file_name = "elections2022.csv"
        gdf_clusters["clusters"] = pd.read_csv(file_name, index_col=0)["cluster"].tolist()  # elections1-->1.figure
        color_map = {1: "darkorange", 2: "red", 3: "purple", 4: "gold"}
        gdf_clusters["color"] = gdf_clusters["clusters"].map(color_map)
        nan_rows = gdf_clusters[gdf_clusters.isna().any(axis=1)]
        print("nan rows:", nan_rows, "n_clusters", n_clusters)
        print(gdf_clusters.index)
        gdf_clusters.plot(ax=ax, color=gdf_clusters['color'], legend=True, edgecolor="black",
                               linewidth=.2)
        ax.axis("off")
        ax.margins(x=0)

        # Add province names (from index) at centroids
        bbox = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.6)
        ha_positions, va_positions = self.ha_positions, self.va_positions
        for province in gdf_clusters.index:
            province_geometry = gdf_clusters.loc[province, "geometry"]
            ha_pos,va_pos =ha_positions.get(province, "center"), va_positions.get(province, "center")
            ax.annotate(text=province,  # Use index (province name) directly
                        xy=(province_geometry.centroid.x, province_geometry.centroid.y),
                        ha=ha_pos, va=va_pos, fontsize=5, color="black", bbox=bbox)


        if file_name == "elections2022.csv":
            legend_handles = [
                Patch(facecolor='darkorange', label='People’s Alliance'),
                Patch(facecolor='red', label="Nation's Alliance"),
                Patch(facecolor='purple', label="Labour's Alliance")
            ]
            title = "2023 Turkish Parliamentary Elections: Provincial Wins by Alliance Blocs"
        else:
            legend_handles = [
                Patch(facecolor='darkorange', label='People’s Alliance (AKP + MHP)'),
                Patch(facecolor='red', label='CHP'),
                Patch(facecolor='purple', label='DEM Party')
            ]
            title = "2024 Turkish Municipal Council Elections: Provincial Wins by Alliance Blocs and Competing Parties"
        ax.legend(
            handles=legend_handles,
            loc=[.55, .87],
            fontsize=6,
            title_fontsize=6,
            frameon=False  # Remove if you want a background
        )
        ax.set_title(title)
        fig.savefig("temp/eps/Figure12a.pdf", format="pdf",dpi=300, bbox_inches="tight")

        st.pyplot(fig)
