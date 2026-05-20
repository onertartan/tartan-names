import streamlit as st
import geopandas as gpd
import ast

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
        title = title_prefix + selected_gender + " baby names"
    if display_option == "nth most common":
        if type(year) == int:
            title += f' in {year}'
        else:
            title += f' in between years {year}'
    elif display_option =="top-n to filter":
        if type(year) == int:
            title = f"Provinces where the selected {names_or_surnames} in top {rank} for {year}"
        else:
            title = f"Provinces where the selected {names_or_surnames} in top {rank} between years {year}"

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


def _parse_blob_centers(centers_text: str, n_features: int):
    if not centers_text.strip():
        return None

    try:
        centers = ast.literal_eval(centers_text)
    except (SyntaxError, ValueError):
        st.error("Centers must be a valid Python-style list, for example [[0, 0], [3, 3]].")
        return None

    if not isinstance(centers, (list, tuple)) or not centers:
        st.error("Centers must be a non-empty list of coordinate rows.")
        return None

    normalized_centers = []
    for row in centers:
        if not isinstance(row, (list, tuple)) or len(row) != n_features:
            st.error(f"Each center must contain exactly {n_features} values.")
            return None
        normalized_centers.append(list(row))

    return normalized_centers


def render_synthetic_data():
    st.subheader("Synthetic Data")
    col1, col2 = st.columns([1, 1])

    n_samples = col1.number_input("n_samples", min_value=1, value=100, step=1)
    n_features = col1.number_input("n_features", min_value=1, value=2, step=1)

    centers = col1.number_input("centers", min_value=1, value=3, step=1)
    random_state = col1.number_input("random_state",value=70)
    return {
        "n_samples": int(n_samples),
        "n_features": int(n_features),
        "centers": centers,
        "random_state": random_state,
    }

