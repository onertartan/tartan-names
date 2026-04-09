from modules.base_page_names import PageNames
import streamlit as st
import pandas as pd
import polars as pl
import geopandas as gpd

class PageBabyNamesByState(PageNames):
    page_name = "baby_names_by_state"
    geo_level= "state"
    country = "usa"
    @staticmethod
    @st.cache_data
    def get_data():
        df = pl.read_parquet("data/preprocessed/usa/names_usa_states.parquet")
        df_data = {"name":df }
        return df_data

    @st.cache_data
    def load_geo_data(_self):
        gdf = {"state": gpd.read_parquet("data/preprocessed/usa/usa_states_geo.parquet")}
        return gdf
PageBabyNamesByState().run()