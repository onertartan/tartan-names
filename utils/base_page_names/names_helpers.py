from typing import List

import pandas as pd
import polars as pl
import geopandas as gpd

import streamlit as st


def rank_again(df: pl.DataFrame, geo_column: str) -> pl.DataFrame:
    accumulated = (
        df.group_by([geo_column, "name", "gender"])
        .agg(pl.col("count").sum().alias("count"))
        .with_columns(
            pl.col("count")
            .rank(method="min", descending=True)
            .over([geo_column, "gender"])
            .alias("rank")
        )
        .sort([geo_column, "rank", "count", "name"], descending=[False, False, True, False])
    )

    if "total_count" in df.columns:
        total_counts = (
            df.select(["year", geo_column, "total_count"])
            .unique()
            .group_by(geo_column)
            .agg(pl.col("total_count").sum().alias("total_count"))
        )
        accumulated = accumulated.join(total_counts, on=geo_column, how="left")

    return accumulated


def preprocess_for_nth_most_common_tab(df: pl.DataFrame, gdf_borders:gpd.GeoDataFrame,year: int, target_rank: int, include_top_n: bool,geo_column:str) -> gpd.GeoDataFrame:
    # Helper for Tab 2.1
    # (2.1.1:Select names and filter if they are in top-n  & 2.1.2:Nth most common)
    # Step 1: filter by year
    # If 'year' is a single value, wrap it in a list; otherwise use it as is
    year_list = year if isinstance(year, list) else [year]
    # Filter rows where the 'year' column is in year_list
    df_year = df if ("year" not in df.columns or year is None) else df.filter(pl.col("year").is_in(year_list))


    # Step 2: filter by rank
    if include_top_n:# Limits the rank limit to 5, since range-30 results in many names
        df_year_rank = df_year.filter(pl.col("rank") <= target_rank)
    else:
        df_year_rank = df_year.filter(pl.col("rank") == target_rank)
    df_year_rank=df_year_rank.to_pandas()
    # Step 3: aggregate names cleanly
    df_year_rank = df_year_rank.sort_values(["rank","gender"]).groupby(geo_column).apply(lambda g: "\n".join("-".join(rank_group["name"].tolist())
            for _, rank_group in g.groupby("rank", sort=False))).reset_index(name="name")
    # Step 4: attach geometry
    gdf_result = gdf_borders.merge(df_year_rank, on=geo_column)
    return gdf_result

def process_for_subtabs_211_212(df, gdf_borders, names_from_multi_select, year, rank, geo_column):
    # Helper for Tab 2.1.1 (under 2.1 plot map tab)
    # If 'year' is a single value, wrap it in a list; otherwise use it as is
    year_list = year if isinstance(year, list) else [year]
    # Filter rows where the 'year' column is in year_list
    df_year = df if ("year" not in df.columns or year is None) else df.filter(pl.col("year").is_in(year_list))
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

def preprocess_for_rank_bar_tabs(df: pl.DataFrame, use_rank_filtering:bool, include_all_years_option:bool, selected_names:List, top_n:int, show_column:str, secondary_top_k_filter:str, always_or_appeared_in_top_k:bool) -> pl.DataFrame:
    # Tabs 2.2,2.3,2.4
    # Drop geography by aggregating counts over year + name.
    df = df.group_by(["year", "name"]).agg(pl.col("count").sum()).sort(["year", "count"], descending=[False, True])
    if show_column=="ratio":
        df_year_totals = df.group_by("year").agg(pl.col("count").sum().alias("year_total"))
        df = df.join(df_year_totals, on="year").with_columns((pl.col("count") / pl.col("year_total")).alias("ratio")).sort(["year", "count"], descending=[False, True])

    if df.is_empty():
        return df.to_pandas()

    # vectorized rank per year
    df = df.with_columns(pl.col("count").rank(method="min", descending=True).over("year").alias("rank"))
    if use_rank_filtering:

        if include_all_years_option == "Include All Years for Names Ever in Top-n":

            apply_filter_for_years_appearing=True
            ever_top_n = df.filter(pl.col("rank") <= top_n)["name"].unique()
            df = df.filter(pl.col("name").is_in(ever_top_n))

            if secondary_top_k_filter and secondary_top_k_filter != "No second filter":
                threshold = int(secondary_top_k_filter.split("top-")[1])
                n_years = df.select(pl.col("year").n_unique()).item()

                # Her ismin veri setinde toplam kaç yıl göründüğünü hesapla
                name_stats = (
                    df.group_by("name")
                    .agg([
                        pl.col("year").n_unique().alias("total_appeared_years"),
                        pl.col("year").filter(pl.col("rank") <= threshold).n_unique().alias("years_in_threshold")
                    ])
                )
                if always_or_appeared_in_top_k:
                    # True: Sadece veri setindeki TÜM yıllarda (n_years) kesintisiz görünen
                    # ve her yıl belirlenen threshold içinde kalan isimler.
                    always_top_names = name_stats.filter(
                        pl.col("years_in_threshold") == n_years
                    ).select("name")
                else:
                    # False: Her yıl görünmeyen (total_appeared_years < n_years), yani NaN içeren
                    # ancak fiilen göründüğü tüm yıllarda threshold içinde kalan isimler.
                    always_top_names = name_stats.filter(
                        (pl.col("years_in_threshold") == pl.col("total_appeared_years")) &
                        (pl.col("total_appeared_years") < n_years)
                    ).select("name")

                df = df.filter(pl.col("name").is_in(always_top_names["name"]))

        else:
            df = df.filter(pl.col("rank") <= top_n)

    if selected_names:
        df = df.filter(pl.col("name").is_in(selected_names))

    return df.to_pandas()


def validate_df(df: pd.DataFrame):
    # not used currently
    required = {"year", "count", "name"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {required - set(df.columns)}")
