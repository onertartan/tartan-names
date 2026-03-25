from modules.base_page_names import PageNames
import streamlit as st
import pandas as pd
import polars as pl

class PageBabyNamesByState(PageNames):
    page_name = "baby_names_by_state"

    @staticmethod
    @st.cache_data
    def get_data():
        df = pl.read_parquet("data/preprocessed/usa/names_usa_states.parquet")
        df_data = {"name":df }
        return df_data

PageBabyNamesByState().run()