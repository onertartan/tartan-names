import io

from PIL.Image import Image

from modules.base_page_names import PageNames
import pandas as pd
import geopandas as gpd
import streamlit as st
import polars as pl

class PageNamesSurnames(PageNames):
    page_name = "names_surnames"
    geo_level= "province"

    @classmethod
    @st.cache_data
    def get_data(cls, geo_scale=None):
        df_data = {"name": pl.read_parquet("data/preprocessed/population/names_turkiye.parquet"),
                   "surname": pl.read_parquet("data/preprocessed/population/surnames_turkiye.parquet")
                   }
        return df_data

PageNamesSurnames().run()
