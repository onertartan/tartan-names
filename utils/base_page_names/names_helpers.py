import polars as pl
import geopandas as gpd

import streamlit as st
def preprocess_for_nth_most_common_tab(df: pl.DataFrame, gdf_borders:gpd.GeoDataFrame,year: int, target_rank: int, include_top_n: bool) -> pl.DataFrame:
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
    for province in df_year_rank["province"].unique().to_list():
        province_data = df_year_rank.filter(pl.col("province") == province)
        male_names = province_data.filter(pl.col("gender") == "male")["name"].to_list()
        female_names = province_data.filter(pl.col("gender") == "female")["name"].to_list()
        combinations = "\n".join(
            f"{male}-{female}"
            for male in male_names
            for female in female_names
        )
        results.append({"province": province, "name": combinations})
    df_year_rank=pl.DataFrame(results).to_pandas()
    # convert to pandas only at GeoPandas boundary
    df_result = gdf_borders.merge(df_year_rank, left_on="province", right_on="province")
    # sort before groupby to ensure consistent combination order (e.g. always "Asel-Defne" not "Defne-Asel")
    df_result = df_result.sort_values(by=["province", "name"], ascending=[True, True])
    df_result = df_result.groupby(["geometry", "province"])["name"].apply(
        lambda x: "\n".join(x)).to_frame().reset_index()

    return df_result

def process_for_select_rank_tab(df,gdf_borders,names_from_multi_select,year,rank):
    # Helper for Tab 2.1.1
    df_year = df.filter(pl.col("year") == year)
    if names_from_multi_select:
        # filter by name and rank
        df_result = df_year.filter(pl.col("name").is_in(names_from_multi_select) & (pl.col("rank") <= rank))
        # group by province and join names with newline (replaces groupby + apply lambda)
        df_result_grouped = df_result.group_by("province").agg(pl.col("name").sort()).with_columns(
            pl.col("name").list.join("\n "))  # joins the list into a single string
        # merge with geodataframe borders (Polars → Pandas for GeoPandas compatibility)
        df_result_not_null = gdf_borders.merge(df_result_grouped.to_pandas(), left_on="province", right_on="province")
        # left join to keep all provinces including those with no match (#df_result_with_nulls)
        df_result = gdf_borders.merge(df_result_not_null[["province", "name"]], left_on="province", right_on="province",
                                      how="left")
        return df_result, df_result_not_null
    return None,None