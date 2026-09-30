import streamlit as st
from typing import List, Optional

from matplotlib import pyplot as plt


def province_selector(all_provinces, key_prefix: str = "province", default_excluded: Optional[List[str]] = None) -> List[str]:
    """
    Render a province selector with two mutually exclusive modes:
    exclude selected provinces or include selected provinces.

    Args:
        key_prefix: Unique prefix for session state keys and widget IDs
        all_provinces: Complete list of all provinces
        default_excluded: Provinces to exclude by default on first load

    Returns:
        List of currently selected provinces
    """
    provinces = sorted({province for province in all_provinces if province is not None})
    mode_key = f"{key_prefix}_mode"
    excluded_key = f"{key_prefix}_excluded"
    excluded_widget_key = f"{key_prefix}_excluded_multiselect"
    included_key = f"{key_prefix}_included"
    included_widget_key = f"{key_prefix}_included_multiselect"
    pending_action_key = f"{key_prefix}_pending_action"

    if mode_key not in st.session_state:
        st.session_state[mode_key] = "Exclude selected provinces"

    if excluded_key not in st.session_state:
        st.session_state[excluded_key] = [province for province in (default_excluded or []) if province in provinces]
    else:
        st.session_state[excluded_key] = [province for province in st.session_state[excluded_key] if province in provinces]

    if included_key not in st.session_state:
        st.session_state[included_key] = provinces.copy()
    else:
        st.session_state[included_key] = [province for province in st.session_state[included_key] if province in provinces]

    pending_action = st.session_state.pop(pending_action_key, None)
    if pending_action == "clear_excluded":
        st.session_state[excluded_key] = []
        st.session_state[excluded_widget_key] = []
    elif pending_action == "select_all_included":
        st.session_state[included_key] = provinces.copy()
        st.session_state[included_widget_key] = provinces.copy()
    elif pending_action == "clear_included":
        st.session_state[included_key] = []
        st.session_state[included_widget_key] = []

    if excluded_widget_key not in st.session_state:
        st.session_state[excluded_widget_key] = st.session_state[excluded_key].copy()
    if included_widget_key not in st.session_state:
        st.session_state[included_widget_key] = st.session_state[included_key].copy()

    mode = st.radio(
        "**Province Selection**",
        ["Exclude selected provinces", "Include selected provinces"],
        key=mode_key,
        horizontal=True,
    )

    col_selector, col_actions = st.columns([4, 1])

    if mode == "Exclude selected provinces":
        with col_selector:
            excluded = st.multiselect(
                "Exclude provinces",
                options=provinces,
                key=excluded_widget_key,
                placeholder="Search and select provinces to exclude...",
            )
        with col_actions:
            if st.button("Clear", key=f"{key_prefix}_clear_excluded_btn", type="secondary"):
                st.session_state[pending_action_key] = "clear_excluded"
                st.rerun()
        st.session_state[excluded_key] = excluded
        selected_provinces = [province for province in provinces if province not in excluded]
        st.caption(f"**{len(selected_provinces)}** provinces selected, **{len(excluded)}** excluded")
        return selected_provinces

    with col_selector:
        included = st.multiselect(
            "Include provinces",
            options=provinces,
            key=included_widget_key,
            placeholder="Search and select provinces to include...",
        )
    with col_actions:
        if st.button("All", key=f"{key_prefix}_select_all_included_btn", type="secondary"):
            st.session_state[pending_action_key] = "select_all_included"
            st.rerun()
        if st.button("Clear", key=f"{key_prefix}_clear_included_btn", type="secondary"):
            st.session_state[pending_action_key] = "clear_included"
            st.rerun()

    st.session_state[included_key] = included
    st.caption(f"**{len(included)}** provinces selected for inclusion")
    return included


def sidebar_controls_basic_setup(*args):
    """
       Renders the sidebar controls
       Parameters: starting year, ending year
    """
    # Inject custom CSS to set the width of the sidebar
    #   st.markdown("""<style>section[data-testid="stSidebar"] {width: 300px; !important;} </style> """,  unsafe_allow_html=True)
    if "visualization_option" not in st.session_state:
        st.session_state["visualization_option"] = "matplotlib"
    start_year = args[0]
    end_year = args[1]
    with (st.sidebar):
        st.header('Visualization options')
         # if ifadesine gerek olmadigi dusunulerek (hata olursa bu if kalktigi icin olabilir) metot classmethod'dan static'e donusttu. Boylelikle higher-education kullanabildi.
        # options= list(range(start_year, end_year + 1)) if cls.page_name != "sex_age_edu_elections" else [2018,2023]
        options = list(range(start_year, end_year + 1))
        # Create a slider to select a single year
        st.select_slider("Select a year", options, end_year, on_change=update_selected_slider_and_years, args=[1],  key="slider_year_1")
        # Create sliders to select start and end years
        st.select_slider("Or select start and end years",options, [options[0],options[-1]],on_change=update_selected_slider_and_years, args=[2], key="slider_year_2")


        if "selected_slider" not in st.session_state:
            st.session_state["selected_slider"] = 1
        update_selected_slider_and_years(st.session_state["selected_slider"])

        if st.session_state["selected_slider"] == 1:
            st.write("You have selected a single year from the first slider.")
            st.write("Selected year:", st.session_state["year_1"])
        else:
            st.write("You have selected start and end years from the second slider.")
            st.write("Selected start year:", st.session_state["year_1"], "\nSelected end year:", st.session_state["year_2"])

        # Main content
        if "animation_images_generated" not in st.session_state:
            st.session_state["animation_images_generated"] = False

def update_selected_slider_and_years(slider_index):
    st.session_state["selected_slider"] = slider_index
    if slider_index == 1:
        st.session_state["year_1"] = st.session_state["year_2"] = int(st.session_state.slider_year_1)
    else:
        st.session_state["year_1"], st.session_state["year_2"] = int(st.session_state.slider_year_2[0]), int(st.session_state.slider_year_2[1])


def figure_setup(display_change=False):
    if st.session_state["visualization_option"] != "matplotlib":
        return None, None
    if st.session_state["year_1"] == st.session_state["year_2"] or st.session_state["selected_slider"] == 1 or \
            st.session_state["animate"]:
        n_rows = 1
    elif display_change:
        n_rows = 3
    else:
        n_rows = 2
    fig, axs = plt.subplots(n_rows, 1, squeeze=False, figsize=(10, 4 * n_rows),
                            gridspec_kw={'wspace': 0, 'hspace': 0.1})  # axs has size (3,1)
    # fig.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8, wspace=0.5, hspace=0.5)
    return fig, axs
