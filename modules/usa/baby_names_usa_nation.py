from modules.base_page_names import PageNames
import streamlit as st
import pandas as pd
import polars as pl
import geopandas as gpd

from viz.gui_helpers.base_page.helpers import sidebar_controls_basic_setup
from viz.gui_helpers.base_page_names.helpers import  render_gender_name_surname_filters, render_tab_selection


class PageBabyNamesNation(PageNames):
    page_name = "baby_names_nation"
    geo_level= "state"
    country = "usa"
    @staticmethod
    @st.cache_data
    def get_data():
        df = pl.read_parquet("data/preprocessed/usa/names_usa_nation.parquet")
        df_data = {"name":df }
        return df_data

    def render(self):
        page_name = self.page_name
        header ="Nationwide Baby Names Analysis"
        st.header(header)
        start_year, end_year = self.data["name"].select(pl.col("year")).min().item(),  self.data["name"].select(pl.col("year")).max().item()
        sidebar_controls_basic_setup(start_year, end_year)
        cols = st.columns([1, 1, 3, 2])

        name_surname_selection, selected_years, gender_list_state_key = render_gender_name_surname_filters(page_name,cols)

        df = self.data["name"]
        # 4. Filter according to the selected year(s)
        df = df.filter( pl.col("year").is_in(selected_years) )
        # 5. Filter according to the gender
        # If surname is not selected there is a gender column (the line below is sufficent)  if name_surname_selection != "surname":
        if "gender" in df.columns:
                df = df.filter( pl.col("gender").is_in(st.session_state[gender_list_state_key]) )

        tab_selected = render_tab_selection(page_name)
        if  tab_selected=="tab_name_trend_analysis":
            self.maintab1_subtab_1(df, page_name, tab_selected)
        else:
            # since the page relies on nation-level data instead of state-level, there is not map plotting (only line, rank bump etc.)
            self.maintab2_subtab_1_2(df, page_name, tab_selected)

PageBabyNamesNation().run()