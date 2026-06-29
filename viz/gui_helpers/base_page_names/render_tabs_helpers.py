import extra_streamlit_components as stx
import streamlit as st

# module level — built once
GENDER_LABEL_TO_LIST = {
    "Male": ["male"],
    "Female": ["female"],
    "Both genders": ["male", "female"],
}

def render_plot_map_sub_tab(names,page_name):
    # Expression depending on page
    expr = "names or surnames" if page_name == "names_surnames" else "baby names"
    col_1, col_2 = st.columns([3,7])
    choice = col_1.radio("Choose how to display results when multiple years are selected:",
                      options=["Show results for the selected years",
                               "Show accumulated results between the selected years"])
    plotter_engine = col_2.radio("Select plotter engine",
                                 options=["Matplotlib", "Folium", "Plotly", "Altair"],
                                 index=0,
                                 # key=f"bump_engine_{page_name}",
                                 )
    accumulate =choice == "Show accumulated results between the selected years"
    options = list(range(1, 31))  # Options are [1-30]
    btn_col1, btn_col2 = st.columns([1, 1])
    rank = 0
    display_option = None
    button_clicked = btn_col1.button(f"Select {expr} and filter if they are in top-n", use_container_width=True)
    top_n = btn_col1.selectbox('Choose a number top-n to filter', options, index=1, key="top_n_filter")
    btn_col1.multiselect(f"Select {expr}", names,key="names_" + page_name)
    if button_clicked:
        rank = top_n
        display_option = "top-n to filter"
    # Second option for Nth Most Common
    button_clicked = btn_col2.button("Nth Most Common", use_container_width=True)
    include_top_n = btn_col2.checkbox("Include top-n to filter")
    if include_top_n:
        options=list(range(1,6))
    n_most_common = btn_col2.selectbox('Choose a number n for the "nth most common"', options)
    if button_clicked:
        rank = n_most_common
        display_option = "nth most common"
    return rank, display_option, include_top_n,accumulate,plotter_engine



def _render_name_surname_selection(page_name, col):
    """Render the name/surname radio (surname pages only) and return the selection."""
    # data is a dictionary whose keys are names and surnames, values are corresponding dataframes
    if "surnames" not in page_name:
        return "name"
    selection = col.radio("Select name or surname", ["Name", "Surname"],
                          key="name_surname_selection").lower()
    st.session_state["name_surname_rb"] = selection
    return selection


def _initial_gender_label(gender_list_key):
    """Sync the widget's first value to any previously stored gender list."""
    current_list = st.session_state.get(gender_list_key)
    if current_list == ["male", "female"]:
        return "Both genders"
    if current_list == ["female"]:
        return "Female"
    return "Male"


def _render_gender_selection(page_name, col, disabled):
    """Render the gender radio and return the selected list of gender values."""
    gender_list_key = "gender_list_" + page_name
    widget_key = "gender_radio_widget_" + page_name  # used for sub-folder name in saving clustering results

    # One-time initialization: if the widget hasn't been created yet, set its
    # initial value based on the existing list data (if any).
    if widget_key not in st.session_state:
        st.session_state[widget_key] = _initial_gender_label(gender_list_key)

    label = col.radio("Select Gender", list(GENDER_LABEL_TO_LIST), key=widget_key,
                      label_visibility="collapsed", disabled=disabled)
    # Surnames have no gender dimension → force both genders.
    gender_list = ["male", "female"] if disabled else GENDER_LABEL_TO_LIST[label]
    st.session_state[gender_list_key] = gender_list
    return gender_list


def render_gender_name_surname_filters(page_name, cols):
    """
    Configure name/surname selection, temporal filtering, and gender selection state.

    This helper centralizes UI rendering and session state management for
    name-based analyses across both "Names & Surnames" and "Baby Names" pages.
    It ensures consistent handling of:
      (1) name vs. surname selection,
      (2) year range filtering,
      (3) gender selection with persistent session state.

    Returns the selected gender values as a list, not a session-state key.
    """
    name_surname_selection = _render_name_surname_selection(page_name, cols[1])
    selected_years = range(st.session_state["year_1"], st.session_state["year_2"] + 1)
    gender_list = _render_gender_selection(
        page_name, cols[0], disabled=(name_surname_selection == "surname"))
    return name_surname_selection, selected_years, gender_list



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
