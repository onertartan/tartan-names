import streamlit as st
import geopandas as gpd

from viz.color_mapping import create_cluster_color_mapping


# ------------- helpers -------------
def get_title_statement(gender, page_name):
    if page_name == "names_surnames" and st.session_state["name_surname_rb"] == "Surname":
        title_statement = "Surnames"
    else:
        title_statement = "Names"

    if page_name == "baby_names":
        title_statement = "Baby " + title_statement

    if len(gender) == 1 and title_statement != "Surnames":
        gender = gender[0]
        title_statement = " " + gender.capitalize() + " " + title_statement

    return title_statement


# Map Plot helpers
def get_ordinal(n):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def create_title_for_plot( rank, year, display_option, page_name):
    names_or_surnames = "names"
    selected_gender = "male and female" if len(st.session_state["sex_" + page_name]) != 1 else st.session_state["sex_" + page_name][0]
    # Adjust phrasing based on rank
    if rank == 1:
        title_prefix = "The most common "
    else:
        title_prefix = f"The {get_ordinal(rank)} most common "

    if page_name == "names_surnames":
        if st.session_state["name_surname_rb"] == "Surname":
            title = title_prefix + "surnames"
            names_or_surnames="surnames"
        else:
            title = title_prefix + selected_gender+" names"
    else:
        title = title_prefix.title() + selected_gender + " baby names"
    if display_option == "nth most common":
        title += f' in {year}'
    elif display_option =="top-n to filter":
        title = f"Provinces where the selected {names_or_surnames} in top {rank} for {year}"

    return title, names_or_surnames

def set_color_mapping(df_result: gpd.GeoDataFrame, cluster_color_mapping: dict) -> gpd.GeoDataFrame:
    df_result["clusters"] = df_result["name"].factorize()[0]
    color_map = create_cluster_color_mapping(df_result.set_index("name"), cluster_color_mapping)
    df_result["color"] = df_result["clusters"].map(color_map).fillna("gray")
    return df_result


def build_legend_entries(df_result: gpd.GeoDataFrame) -> list[str]:
    df_count = (
        df_result["name"].str.split("\n")
        .explode()
        .value_counts()
        .rename_axis("name")
        .reset_index(name="count")
    )
    return [f"{row['name']}: {row['count']}" for _, row in df_count.iterrows()]

