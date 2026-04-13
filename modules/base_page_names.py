from clustering.scaling import scale
from modules.base_page import BasePage
import pandas as pd
import streamlit as st
import locale
from utils.base_page_names.names_helpers import process_for_select_rank_tab, preprocess_for_nth_most_common_tab, \
    preprocess_for_rank_bar_tabs
from viz.config import CLUSTER_COLOR_MAPPING, VA_POSITIONS, HA_POSITIONS
from viz.gui_helpers.base_page_names.render_helpers import create_title_for_plot
from viz.gui_helpers.ui_base_page import province_selector, sidebar_controls_basic_setup
from viz.gui_helpers.base_page_names.ui_base_page_names import render_tab_selection, render_gender_name_surname_filters, \
 sidebar_controls_plot_options_setup, render_data_coverage_if_rank_available
from viz.gui_helpers.base_page_names.render_plots_tab import render_rank_plot_sub_tabs, render_custom_bar_plot_sub_tab, \
    render_plot_map_sub_tab
from viz.plotters.bar_plotter_names import get_bar_plotter
from viz.plotters.bump_plotter import get_bump_plotter
from viz.plotters.geo_names_plotter import get_map_plotter
from viz.plotters.line_plotter_names import get_line_plotter
from viz.plotters.network_plotter import plot_umap_tsne, plot_mds_provinces
import polars as pl
import geopandas as gpd
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

class PageNames(BasePage):
    geo_level=None
    country = "turkiye"
    def preprocessing_initial_filtering(self, name_surname_selection, selected_years, gender_list_state_key, cols, geo_column="province"):
        """
        Load the selected names/surnames dataset and apply the initial UI filters.

        The method selects the appropriate dataframe from ``self.data``, renders the
        geography selector, then filters rows by the chosen years, selected
        geographic units, and gender selection when a ``gender`` column is present.

        Parameters
        ----------
        name_surname_selection(str) : Dataset key chosen in the UI, such as ``"name"`` or ``"surname"``.
        selected_years (list)       : Years selected by the user.
        gender_list_state_key (str) : Session-state key that stores the selected genders.
        cols (list)                 : Streamlit columns used to place the geography selector.
        geo_column (str)            : Geography column to filter on, for example ``"province"`` or ``"state"``.

        Returns
        df (pl.DataFrame)          : Filtered dataframe matching the current UI selections.
        """
        # 1. data is a dictionary with the key "names" (it can have another key "surnames")
        df = self.data[name_surname_selection.lower()]
        # 2. Get unique province(state) names
        with cols[2]:
            selected_provinces = province_selector(
                df.select(pl.col(geo_column)).unique().to_series().to_list(),
                key_prefix=f"{self.page_name}{geo_column}")
        # 3. Filter according to the selected year and selected provinces
        df = df.filter((pl.col("year").is_in(selected_years)) & (pl.col(geo_column).is_in(selected_provinces)))
        # 4. Filter according to the gender
        # If surname is not selected there is a gender column (the line below is sufficent)  if name_surname_selection != "surname":
        if "gender" in df.columns:
                df = df.filter( pl.col("gender").is_in(st.session_state[gender_list_state_key]) )
        return df

    def preprocess_clustering(self, df):
        year = df.index.get_level_values(0).unique() # year(s)
        page_name = self.page_name
        geo_column = self.geo_level
        df_year = df.loc[year]
        if page_name == "names_surnames" and "name_surname_rb" in st.session_state and st.session_state["name_surname_rb"] == "surname":
            df_year = df.loc[year]
        elif st.session_state["sex_" + page_name] == ["male", "female"]:  # if both sexes are selected
            df_year_male, df_year_female = df[df["gender"] == "male"].loc[year], df[df["gender"] == "female"].loc[year]
            overlapping_names = set(df_year_male["name"]) & set(df_year_female["name"])
            nonoverlapping_names =set(df_year_male["name"]) - set(df_year_female["name"])
            nonoverlapping_names2 =set(df_year_female["name"]) - set(df_year_male["name"])

            st.header("Size overlapping:"+str(len(overlapping_names))+", Size nonoverlapping:"+str(len(nonoverlapping_names))+", Size nonoverlapping2:"+str(len(nonoverlapping_names2)))
            df_year_male['name'] = df_year_male.apply(
                lambda x: f"{x['name']}_female" if x['name'] in overlapping_names else x['name'], axis=1)
            df_year_female['name'] = df_year_female.apply(
                lambda x: f"{x['name']}_male" if x['name'] in overlapping_names else x['name'], axis=1)
            df_year = pd.concat([df_year_male, df_year_female])
     #   else:  # single gender selected for names  # gender selection handled in preprocessing_initial now
     #       sex = st.session_state["sex_" + page_name]
     #       df_year = df[df["sex"].isin(sex)].loc[year]
        st.dataframe(df_year.head(35))
        st.header("df_year shape:"+str(df_year.shape))
        if st.session_state["selected_tab_" + page_name] == "tab_temporal_clustering":
            total_counts = df[["total_count"]].groupby(level=["year", geo_column]).first()
       # else: # Use top-30 names for clustering otherwise, pivot table becomes a very high-dimensional sparse matrix
       #     df=df.filter((pl.col("rank") <= 30))
        # Get unique cumulative total counts over years(for each province)
        total_counts = df[["total_count"]].groupby(level=["year", geo_column]).first()
        st.write("after groupby year and state")
        st.dataframe(total_counts)
        # INSTEAD OF AGGREGATING PROVINCE/STATE COUNTS OVER YEARS, KEEP YEAR COLUMN
        pivot_df = df.pivot_table(index=['year', 'state'],
            columns='name',
            values='count',
            fill_value=0  # optional: replaces NaN with 0
        )
        st.dataframe(pivot_df.head())
        st.write(pivot_df.shape)
        total_counts = total_counts.groupby(geo_column).sum()
        if isinstance(df_year.index, pd.MultiIndex):  # If applying temporal clustering (multiple years given as year)
            df_year = df_year.droplevel(0)  # Drop the first level year(position 0), if so index becomes province/state
        st.dataframe(df_year.sample(12))

        df_year = df_year.groupby([df_year.index, 'name']).agg({'count': 'sum'})
        # Merge
        df_year = df_year.merge(total_counts, left_index=True, right_index=True, how="outer")
        df_year = df_year.reset_index().set_index(geo_column)
        df_pivot = pd.pivot_table(df_year, values='count', index=df_year.index, columns=['name'], aggfunc=lambda x: x, dropna=False, fill_value=0)
        total_counts = df_year.loc[:, "total_count"]
        total_counts_unique=total_counts.groupby(level=0).first()
        scaler_method = st.session_state["scaler"]
        df_pivot = scale(scaler_method, df_pivot, total_counts_unique)
        st.dataframe(df_pivot.head())
        st.header("df_pivot shape:"+str(df_pivot.shape))

        if st.session_state["selected_tab_" + page_name] == "tab_name_clustering":  # transpose_for_name_clustering:
            df_pivot = df_pivot.T
        return df_pivot

    def render(self):
        # Apply CSS to all radio groups except the first
        st.session_state["geo_scale"] = "state" if "usa" in self.page_name else "province"
        header = "Names & Surnames Analysis" if self.page_name == "names_surnames" else "Baby Names Analysis"
        st.header(header)
        start_year, end_year = self.data["name"].select(pl.col("year")).min().item(),  self.data["name"].select(pl.col("year")).max().item()
        sidebar_controls_basic_setup(start_year, end_year)
        sidebar_controls_plot_options_setup(self.page_name)
        cols = st.columns([1, 1, 3, 2])

        name_surname_selection, selected_years, gender_list_state_key = render_gender_name_surname_filters(self.page_name,cols)
        df = self.preprocessing_initial_filtering(name_surname_selection, selected_years, gender_list_state_key, cols, self.geo_level)

        page_name, geo_level= self.page_name, self.geo_level
        gdf_borders = self.gdf[geo_level]

        tab_selected = render_tab_selection(page_name)
        if "clustering" in tab_selected:  # Main Tab-1
            self.maintab1(df, geo_level, tab_selected) # clustering tab
        elif tab_selected == "tab_map":  # Main Tab-2: Tab-1
            self.maintab2_subtab1_plot_map(df, gdf_borders, page_name, geo_level)
        else : # elif tab_selected in ["rank_bump", "rank_line_bar", "custom_line_bar"]:  # Main Tab-2: Sub-tabs: 2-3-4
            self.maintab2_subtab_2_3_4(df, page_name, tab_selected, geo_level)

    def maintab1(self, df, geo_level, tab_selected):
        # 0. Render UI
        if "rank" in df.columns:
            max_rank = df.select(pl.col("rank")).max().item()  # .item() tek bir değeri Python tipine çevirir
            use_data_option, top_n_names = render_data_coverage_if_rank_available(max_rank)
            if "top-n" in use_data_option:
                df = df.filter(pl.col("rank") <= top_n_names)

        # 5. Polars DataFrame'i Pandas'a dönüştür
        df = df.to_pandas().set_index(['year', geo_level]).sort_index()
        df_pivot = self.tab_clustering(df, geo_level, save_sub_folder=st.session_state["gender_radio_widget_" + self.page_name].lower())
        if tab_selected == "tab_geo_clustering":
            if df_pivot is not None:
                plot_umap_tsne(df_pivot.copy(), CLUSTER_COLOR_MAPPING)
                plot_mds_provinces(df_pivot)
        elif tab_selected =="tab_temporal_clustering":
            pass

    def maintab2_subtab1_plot_map(self, df:pl.DataFrame, gdf_borders:gpd.GeoDataFrame, page_name:str,geo_level:str):
        # Tab 2.1 Map Plot (2.1.1.Select Baby Names if they are in top-n , 2.1.2. Nth Most Common)
        names = sorted(df["name"].unique(), key=locale.strxfrm)
        rank, display_option,include_top_n = render_plot_map_sub_tab(names,page_name)
        # --- Plot map ---
        col_plot, _ = st.columns([9, 1])
        # Display results on map if a button is clicked
        if display_option:
            st.session_state["visualization_option"] = "matplotlib"
            df_results = []  # for animation?
            year_1, year_2 = st.session_state["year_1"], st.session_state["year_2"]
            for i, year in enumerate(sorted({year_1, year_2})):
                title, _ = create_title_for_plot(rank, year, display_option, page_name)
                # Display option 1: Show the nth most common baby names
                if display_option == "top-n to filter":  # Display option 2: Select single year, name(s) and top-n number to filter
                    names_from_multi_select = st.session_state["names_" + page_name]
                    df_result, df_result_not_null = process_for_select_rank_tab(df, gdf_borders,
                                                                                names_from_multi_select, year, rank,geo_level)
                elif display_option == "nth most common":
                    df_result = preprocess_for_nth_most_common_tab(df, gdf_borders, year, rank, include_top_n,geo_level)
                    df_results.append(df_result)
              #      if df_result_not_null is not None:
               #         df_results.append(df_result_not_null)
                if df_result is not None:
                    map_plotter = get_map_plotter("Matplotlib", HA_POSITIONS, VA_POSITIONS, CLUSTER_COLOR_MAPPING)
                    map_plotter.plot(df_result,title, col_plot,geo_level)


    def maintab2_subtab_2_3_4(self, df,page_name, tab_selected, geo_level):
        clusters = []
        if "n_clusters_" + page_name in st.session_state:
            clusters = range(1, st.session_state["n_clusters_" + page_name] + 1)
        gender = st.session_state["gender_radio_widget_"+page_name]
        if "rank" in tab_selected:
            use_province_or_cluster, selected_n_cluster, show_provinces_separately, plotter_engine, show_column, plot_style = render_rank_plot_sub_tabs(page_name, clusters,geo_level, tab_selected)
        else:
            names = sorted(df["name"].unique(), key=locale.strxfrm)
            use_province_or_cluster, selected_n_cluster, show_provinces_separately, plotter_engine, show_column, plot_style = render_custom_bar_plot_sub_tab(page_name, clusters, names,geo_level, tab_selected)

        if "bump" in tab_selected:
            plotter_object = get_bump_plotter(plotter_engine,gender,page_name)
        else:  # "rank_bar_line_bar" or "custom_bar_line_bar"  (sub-tab 2.3 or 2.4)
            if "bar" in plot_style:
                plotter_object = get_bar_plotter(plotter_engine,gender,page_name)
            else: # elif "line
                plotter_object = get_line_plotter (plotter_engine,gender,page_name)

        if df.is_empty():
            st.error("You have not selected any data (provinces)")
            return
        col_plot, _ = st.columns([9, 1])
        col_plot.title("Counts by Name and Year")
        params = {"is_rank_tab": "rank" in st.session_state["selected_tab_"+page_name],
            "include_all_years_option": st.session_state.get("include_all_years","Show Only Years When Names Are in Top-n"),
            "selected_names":  st.session_state.get("names_" + page_name,[]),
            "top_n": st.session_state.get("rank_" + page_name,-1),
            "show_column":show_column}
        if tab_selected == "custom_bar" and params["selected_names"] == []:
            st.error("You have not selected any names/surnames)")
            return

        if use_province_or_cluster == f"use {geo_level}s":
            if show_provinces_separately:
                for province in df[geo_level].unique(maintain_order=True).to_list():
                    df_province = df.filter(pl.col(geo_level) == province)
                    if not df_province.is_empty():
                        col_plot.subheader(province)
                        plotter_object.plot(preprocess_for_rank_bar_tabs(df_province,**params), col_plot,show_column)
            else:
                plotter_object.plot(preprocess_for_rank_bar_tabs(df,**params), col_plot,show_column)
        elif use_province_or_cluster == "Use clusters" and selected_n_cluster:
            df_pivot = self.preprocess_clustering(df)
            df_pivot, _ = self.kmeans(df_pivot) # _ --> closest indices ( not used here)

            df_clusters = df_pivot["clusters"]
            df['clusters'] = df.index.get_level_values("province").map(df_clusters)
            if st.session_state["aggregate_totals_" + self.page_name]:
                df = df[df["clusters"].isin(selected_n_cluster)]
                plotter_object.plot(preprocess_for_rank_bar_tabs(df,**params), col_plot,show_column)
            else:
                for cluster in selected_n_cluster:
                    df_cluster = df[df["clusters"] == cluster]
                    col_plot.subheader(f"Cluster {cluster}")
                    plotter_object.plot(preprocess_for_rank_bar_tabs(df_cluster,**params), col_plot)
       # else:  # if not any selected, select all provinces
        #    plotter_object.plot(preprocess_for_rank_bar_tabs(df,params), col_plot)