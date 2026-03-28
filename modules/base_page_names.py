from clustering.scaling import scale
from modules.base_page import BasePage
import pandas as pd
import streamlit as st
import locale
from utils.base_page_names.names_helpers import process_for_select_rank_tab, preprocess_for_nth_most_common_tab
from viz.config import CLUSTER_COLOR_MAPPING, VA_POSITIONS, HA_POSITIONS
from viz.gui_helpers.ui_base_page import province_selector, sidebar_controls_basic_setup
from viz.gui_helpers.base_page_names.ui_base_page_names import render_tab_selection, render_gender_name_surname_filters, \
 sidebar_controls_plot_options_setup, render_data_coverage_if_rank_available
from viz.gui_helpers.base_page_names.render_plots_tab import render_rank_plot_sub_tabs, render_custom_bar_plot_sub_tab, \
    render_plot_map_sub_tab
from viz.plotters.bar_plotter_names import get_bar_plotter
from viz.plotters.bump_plotter import get_bump_plotter
from viz.plotters.geo_names_plotter import get_map_plotter
from viz.plotters.network_plotter import plot_umap_tsne, plot_mds_provinces
import polars as pl

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

class PageNames(BasePage):

    def preprocessing_initial_filtering(self,name_surname_selection,selected_years,gender_list_state_key,cols):
        # ---   Apply Filter ---
        # Only filter by gender if we are looking at names
        df = self.data[name_surname_selection.lower()]
        # 1. Get unique province(state) names
        with cols[2]:
            selected_provinces = province_selector(
                df.select(pl.col("province")).unique().to_series().to_list(),
                key_prefix=f"{self.page_name}_province")
        # 2. Filter according to the selected year and province
        df = df.filter( (pl.col("year").is_in(selected_years)) & (pl.col("province").is_in(selected_provinces)) )
        # 3. Filter according to the gender
        if name_surname_selection != "surname":
            # If surname is not selected there is a gender column
            if "gender" in df.columns:
                df = df.filter( pl.col("gender").is_in(st.session_state[gender_list_state_key]) )
        return df

    def preprocess_clustering(self, df):
        """"
        returns:df_pivot
        """
        year = df.index.get_level_values(0).unique() # year(s)
        page_name = self.page_name
        df_year = df.loc[year]
        if page_name == "names_surnames" and "name_surname_rb" in st.session_state and st.session_state["name_surname_rb"] == "surname":
            df_year = df.loc[year]
        elif st.session_state["sex_" + page_name] == ["male", "female"]:  # if both sexes are selected
            df_year_male, df_year_female = df[df["gender"] == "male"].loc[year], df[df["gender"] == "female"].loc[year]
            overlapping_names = set(df_year_male["name"]) & set(df_year_female["name"])
            df_year_male['name'] = df_year_male.apply(
                lambda x: f"{x['name']}_female" if x['name'] in overlapping_names else x['name'], axis=1)
            df_year_female['name'] = df_year_female.apply(
                lambda x: f"{x['name']}_male" if x['name'] in overlapping_names else x['name'], axis=1)
            df_year = pd.concat([df_year_male, df_year_female])
     #   else:  # single gender selected for names  # gender selection handled in preprocessing_initial now
     #       sex = st.session_state["sex_" + page_name]
     #       df_year = df[df["sex"].isin(sex)].loc[year]
        if isinstance(df_year.index, pd.MultiIndex):  # If applying temporal clustering (multiple years given as year)
             df_year = df_year.droplevel(0)  # Drop the first level year(position 0)

          # Get unique cumulative total counts over years(for each province)
        total_counts = df[["total_count"]].groupby(level=["year", "province"]).first()
        total_counts = total_counts.groupby("province").sum()

        df_year = df_year.groupby([df_year.index, 'name']).agg({'count': 'sum'})
        # Merge
        df_year = df_year.merge(total_counts, left_index=True, right_index=True, how="outer")
        df_year = df_year.reset_index().set_index("province")
        df_pivot = pd.pivot_table(df_year, values='count', index=df_year.index, columns=['name'], aggfunc=lambda x: x,
                                  dropna=False, fill_value=0)
        total_counts = df_year.loc[:, "total_count"]
        scaler_method = st.session_state["scaler"]
        df_pivot = scale(scaler_method, df_pivot, total_counts)
        if st.session_state["selected_tab_" + self.page_name] == "tab_name_clustering":  # transpose_for_name_clustering:
            df_pivot = df_pivot.T
        return df_pivot

    def preprocess_for_rank_bar_tabs(self, df):

        df.index = df.index.droplevel(1)  # drop provinces from multiindex
        df = df.groupby([df.index, "name"]).aggregate({"count": "sum"}).reset_index(level="name")
        df = df.sort_values(by=["year", "count"], ascending=False)
        if  "rank" in st.session_state["selected_tab_"+self.page_name]:  # rank tabs work for cumulative results
            # Create rank column
            for year in df.index:
                df.loc[year, 'rank'] = df.loc[year, 'count'].rank(axis=0, method='min', ascending=False)

            # preprocess rank
            if st.session_state["include_all_years"] == "Include All Years for Names Ever in Top-n":
                selected_names = df[df['rank'] <= st.session_state["rank_" + self.page_name]]["name"]
                df = df[df["name"].isin(selected_names)]
            else:
                df = df[df['rank'] <= st.session_state["rank_" + self.page_name]]
        else:  # st.session_state["selected_tab" + cls.page_name] == "custom_bar":
            selected_names = st.session_state["names_" + self.page_name]
            df = df[df["name"].isin(selected_names)]
        df.reset_index(inplace=True)
        return df

    def render(self):
        # Apply CSS to all radio groups except the first
        st.session_state["geo_scale"] = "province"
        header = "Names & Surnames Analysis" if self.page_name == "names_surnames" else "Baby Names Analysis"
        st.header(header)

        start_year, end_year = self.data["name"].select(pl.col("year")).min().item(),  self.data["name"].select(pl.col("year")).max().item()
        sidebar_controls_basic_setup(start_year, end_year)
        sidebar_controls_plot_options_setup(self.page_name)
        cols = st.columns([1, 1, 3, 2])

        name_surname_selection, selected_years, gender_list_state_key = render_gender_name_surname_filters(self.page_name,cols)
        df = self.preprocessing_initial_filtering(name_surname_selection, selected_years, gender_list_state_key, cols)

        tab_selected = render_tab_selection(self.page_name)
        col_plot, col_df = st.columns([5, 1])
        if tab_selected == "tab_geo_clustering" or tab_selected == "tab_name_clustering":  # Main Tab-1
            # 0. Render UI
            if "rank" in df.columns:
               max_rank = df.select(pl.col("rank")).max().item()  # .item() tek bir değeri Python tipine çevirir
               use_data_option, top_n_names=render_data_coverage_if_rank_available(max_rank)
               if "top-n" in use_data_option:
                   df = df.filter(pl.col("rank") <= top_n_names)
            # 5. Polars DataFrame'i Pandas'a dönüştür
            # Not: Bunun için 'pyarrow' kütüphanesinin yüklü olması gerekir.
            df = df.to_pandas()
            # 6. Pandas üzerinde MultiIndex oluştur
            df = df.set_index(['year', 'province']).sort_index()

            df_pivot = self.tab_clustering(df=df,save_sub_folder=st.session_state["gender_radio_widget_" + self.page_name].lower())
            if tab_selected=="tab_geo_clustering":
                if df_pivot is not None:
                    plot_umap_tsne(df_pivot.copy(), CLUSTER_COLOR_MAPPING)
                    plot_mds_provinces(df_pivot)
        elif tab_selected == "tab_map":  # Main Tab-2: Tab-1
            self.tab2_subtab1_plot_map(df)
        elif tab_selected in ["rank_bump", "rank_bar", "custom_bar"]:  # Main Tab-2: Sub-tabs: 2-3-4
            self.tab2_subtab_2_3_4(df, col_plot, col_df)

    def tab2_subtab1_plot_map(self, df):
        names = sorted(df["name"].unique(), key=locale.strxfrm)
        rank, display_option,include_top_n = render_plot_map_sub_tab(names,self.page_name)
        # --- Plot map ---
        col_plot, col_df = st.columns([5, 1])
        # Display results on map if a button is clicked
        if display_option:
            #self.plot_map(col_plot, col_df, df, rank, display_option, include_top_n)
            st.session_state["visualization_option"] = "matplotlib"
            page_name = st.session_state["page_name"]
            gdf_borders = self.gdf["province"]
            df_results = []  # for animation?
            year_1, year_2 = st.session_state["year_1"], st.session_state["year_2"]
            for i, year in enumerate(sorted({year_1, year_2})):
                # Display option 1: Show the nth most common baby names
                if display_option == "nth most common":
                    df_result = preprocess_for_nth_most_common_tab(df, gdf_borders, year, rank, include_top_n)
                    df_results.append(df_result)
                elif display_option == "top-n to filter":  # Display option 2: Select single year, name(s) and top-n number to filter
                    names_from_multi_select = st.session_state["names_" + self.page_name]
                    df_result, df_result_not_null = process_for_select_rank_tab(df, gdf_borders,
                                                                                names_from_multi_select, year, rank)
                    if df_result_not_null is not None:
                        df_results.append(df_result_not_null)
                if df_result is not None:
                    map_plotter = get_map_plotter("Matplotlib", HA_POSITIONS, VA_POSITIONS, CLUSTER_COLOR_MAPPING)
                    map_plotter.plot(df_result,rank, year, display_option, page_name, col_plot)

    def tab2_subtab_2_3_4(self, df, col_plot, col_df):
        page_name = self.page_name
        clusters = []
        if "n_clusters_" + page_name in st.session_state:
            clusters = range(1, st.session_state["n_clusters_" + page_name] + 1)
        gender = st.session_state["gender_radio_widget_"+page_name]
        if "rank" in st.session_state["selected_tab_"+self.page_name]:
            use_province_or_cluster, selected_n_cluster, show_provinces_separately, plotter_engine = render_rank_plot_sub_tabs(page_name, clusters)
        else:
            names = sorted(df["name"].unique(), key=locale.strxfrm)
            use_province_or_cluster, selected_n_cluster, show_provinces_separately, plotter_engine = render_custom_bar_plot_sub_tab(page_name, clusters, names)

        if "bump" in st.session_state["selected_tab_"+page_name]:
            plotter_object = get_bump_plotter(plotter_engine,gender,page_name)
        elif "bar" in st.session_state["selected_tab_"+page_name]:
            plotter_object = get_bar_plotter(plotter_engine,gender,page_name)
        if df.empty:
            st.error("You haven't selected any data (provinces)")
            return
        col_plot.title("Counts by Name and Year")
        idx = pd.IndexSlice
        if use_province_or_cluster == "use provinces":
            if show_provinces_separately:
                for province in df.index.get_level_values(1).unique():
                    df_province = df.loc[idx[:, province], :]
                    col_plot.subheader(province)
                    plotter_object.plot(self.preprocess_for_rank_bar_tabs(df_province), col_plot)
            else:
                plotter_object.plot(self.preprocess_for_rank_bar_tabs(df), col_plot)
            col_df.dataframe(df)
        elif use_province_or_cluster == "Use clusters" and selected_n_cluster:
            df_pivot = self.preprocess_clustering(df)
            df_pivot, _ = self.kmeans(df_pivot) # _ --> closest indices ( not used here)

            df_clusters = df_pivot["clusters"]
            df['clusters'] = df.index.get_level_values("province").map(df_clusters)
            if st.session_state["aggregate_totals_" + self.page_name]:
                df = df[df["clusters"].isin(selected_n_cluster)]
                plotter_object.plot(self.preprocess_for_rank_bar_tabs(df), col_plot)
            else:
                for cluster in selected_n_cluster:
                    df_cluster = df[df["clusters"] == cluster]
                    col_plot.subheader(f"Cluster {cluster}")
                    plotter_object.plot(self.preprocess_for_rank_bar_tabs(df_cluster), col_plot)
            col_df.dataframe(df)
        else:  # if not any selected, select all provinces
            plotter_object.plot(self.preprocess_for_rank_bar_tabs(df), col_plot)