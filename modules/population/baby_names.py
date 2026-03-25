from modules.base_page_names import PageNames
import pandas as pd
import geopandas as gpd
import streamlit as st

import polars as pl
class PageBabyNames(PageNames):
    page_name = "baby_names"

    @staticmethod
    @st.cache_data
    def get_data():
        df = pl.read_parquet("data/preprocessed/population/names_baby_turkiye.parquet")
        df_data = {"name":df }
        return df_data

PageBabyNames().run()