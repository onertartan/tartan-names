from typing import List

import pandas as pd
import polars as pl
import geopandas as gpd

import streamlit as st
def preprocess_for_nth_most_common_tab(df: pl.DataFrame, gdf_borders:gpd.GeoDataFrame,year: int, target_rank: int, include_top_n: bool,geo_column:str) -> gpd.GeoDataFrame:
    # Helper for Tab 2.1
    # (2.1.1:Select names and filter if they are in top-n  & 2.1.2:Nth most common)
    # filter by year
    df_year = df.filter(pl.col("year") == year)
    # filter by rank
    if include_top_n:# Limits the rank limit to 5, since range-30 results in many names
        df_year_rank = df_year.filter(pl.col("rank") <= target_rank)
    else:
        df_year_rank = df_year.filter(pl.col("rank") == target_rank)
    df_year_rank=df_year_rank.to_pandas()
    # Step 3: aggregate names cleanly
    df_year_rank = df_year_rank.sort_values("rank").groupby(geo_column).apply(lambda g: "\n".join("-".join(rank_group["name"].tolist())
            for _, rank_group in g.groupby("rank", sort=False))).reset_index(name="name")
    # Step 4: attach geometry
    gdf_result = gdf_borders.merge(df_year_rank, on=geo_column)
    return gdf_result

def process_for_select_rank_tab(df,gdf_borders,names_from_multi_select,year,rank,geo_column):
    # Helper for Tab 2.1.1
    df_year = df.filter(pl.col("year") == year)
    if names_from_multi_select:
        # filter by name and rank
        df_result = df_year.filter(pl.col("name").is_in(names_from_multi_select) & (pl.col("rank") <= rank))
        # group by province and join names with newline (replaces groupby + apply lambda)
        df_result_grouped = df_result.group_by(geo_column).agg(pl.col("name").sort()).with_columns( pl.col("name").list.join("\n "))  # joins the list into a single string
        # merge with geodataframe borders (Polars → Pandas for GeoPandas compatibility)
        df_result_not_null = gdf_borders.merge(df_result_grouped.to_pandas(), left_on=geo_column, right_on=geo_column)
        # left join to keep all provinces including those with no match (#df_result_with_nulls)
        df_result = gdf_borders.merge(df_result_not_null[[geo_column, "name"]], left_on=geo_column, right_on=geo_column,how="left")
        return df_result, df_result_not_null
    return None,None

def preprocess_for_rank_bar_tabs( df: pl.DataFrame,is_rank_tab:bool,include_all_years_option:bool,selected_names:List,top_n:int,show_column:str) -> pl.DataFrame:
    # Tabs 2.2,2.3,2.4
    # Drop geography by aggregating counts over year + name.
    df = df.group_by(["year", "name"]).agg(pl.col("count").sum()).sort(["year", "count"], descending=[False, True])
    if show_column=="ratio":
        df_year_totals = df.group_by("year").agg(pl.col("count").sum().alias("year_total"))
        df = df.join(df_year_totals, on="year").with_columns((pl.col("count") / pl.col("year_total")).alias("ratio")).sort(["year", "count"], descending=[False, True])

    if df.is_empty():
        return df.to_pandas()
    if is_rank_tab:
        # vectorized rank per year
        df = df.with_columns(pl.col("count").rank(method="min", descending=True).over("year").alias("rank"))
        if include_all_years_option == "Include All Years for Names Ever in Top-n":
            # names that were ever in top-n across any year
            ever_top_n = df.filter(pl.col("rank") <= top_n)["name"].unique()
            df = df.filter(pl.col("name").is_in(ever_top_n))
        else:
            df = df.filter(pl.col("rank") <= top_n)
    else:
        df = df.filter(pl.col("name").is_in(selected_names))

    return df.to_pandas()


def validate_df(df: pd.DataFrame):
    # not used currently
    required = {"year", "count", "name"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {required - set(df.columns)}")
