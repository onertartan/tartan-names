from typing import List

import polars as pl
import geopandas as gpd

import streamlit as st
def preprocess_for_nth_most_common_tab(df: pl.DataFrame, gdf_borders:gpd.GeoDataFrame,year: int, target_rank: int, include_top_n: bool,geo_column:str) -> pl.DataFrame:
    # Helper for Tab 2.1
    # (2.1.1:Select names and filter if they are in top-n  & 2.1.2:Nth most common)
    # filter by year (replaces df.loc[year])
    df_year = df.filter(pl.col("year") == year)
    # filter by rank
    if include_top_n:# Limits the rank limit to 5, since range-30 results in many names
        df_year_rank = df_year.filter(pl.col("rank") <= target_rank)
    else:
        df_year_rank = df_year.filter(pl.col("rank") == target_rank)
    # if no sex column or only one gender — no combinations needed

    if "gender" not in df_year_rank.columns or df_year_rank["gender"].n_unique() == 1:
        return df_year_rank.to_pandas()
    # generate male-female combinations per province
    results = []
    for province in df_year_rank[geo_column].unique().to_list():
        province_data = df_year_rank.filter(pl.col(geo_column) == province)
        male_names = province_data.filter(pl.col("gender") == "male")["name"].to_list()
        female_names = province_data.filter(pl.col("gender") == "female")["name"].to_list()
        combinations = "\n".join(
            f"{male}-{female}"
            for male in male_names
            for female in female_names
        )
        results.append({geo_column: province, "name": combinations})
    df_year_rank=pl.DataFrame(results).to_pandas()
    # convert to pandas only at GeoPandas boundary
    df_result = gdf_borders.merge(df_year_rank, left_on=geo_column, right_on=geo_column)
    # sort before groupby to ensure consistent combination order (e.g. always "Asel-Defne" not "Defne-Asel")
    df_result = df_result.sort_values(by=[geo_column, "name"], ascending=[True, True])
    df_result = df_result.groupby(["geometry", geo_column])["name"].apply(
        lambda x: "\n".join(x)).to_frame().reset_index()

    return df_result

def process_for_select_rank_tab(df,gdf_borders,names_from_multi_select,year,rank,geo_column):
    # Helper for Tab 2.1.1
    df_year = df.filter(pl.col("year") == year)
    if names_from_multi_select:
        # filter by name and rank
        df_result = df_year.filter(pl.col("name").is_in(names_from_multi_select) & (pl.col("rank") <= rank))
        # group by province and join names with newline (replaces groupby + apply lambda)
        df_result_grouped = df_result.group_by(geo_column).agg(pl.col("name").sort()).with_columns(
            pl.col("name").list.join("\n "))  # joins the list into a single string
        # merge with geodataframe borders (Polars → Pandas for GeoPandas compatibility)
        print("çççö",gdf_borders)
        df_result_not_null = gdf_borders.merge(df_result_grouped.to_pandas(), left_on=geo_column, right_on=geo_column)
        # left join to keep all provinces including those with no match (#df_result_with_nulls)
        df_result = gdf_borders.merge(df_result_not_null[[geo_column, "name"]], left_on=geo_column, right_on=geo_column,
                                      how="left")
        return df_result, df_result_not_null
    return None,None

def preprocess_for_rank_bar_tabs( df: pl.DataFrame,is_rank_tab:bool,include_all_years_option:bool,selected_names:List,top_n:int) -> pl.DataFrame:
    # Tabs 2.2,2.3,2.4
    # drop province by aggregating count over year + name (replaces droplevel + groupby)
    df = df.group_by(["year", "name"]).agg(pl.col("count").sum()).sort(["year", "count"], descending=[False, True])
    if df.is_empty():
        return df.to_pandas()
    if is_rank_tab:
        # vectorized rank per year (replaces row-by-row loop)
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
