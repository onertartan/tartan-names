import extra_streamlit_components as stx
import streamlit as st

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





def render_gender_name_surname_filters(page_name,cols):
    """
     Configure name/surname selection, temporal filtering, and gender selection state.

    This helper centralizes UI rendering and session state management for
    name-based analyses across both "Names & Surnames" and "Baby Names" pages.
    It ensures consistent handling of:
      (1) name vs. surname selection,
      (2) year range filtering,
      (3) gender selection with persistent session state.
    """
    name_surname_selection = "name"
    # data is a dictionary whose keys are names and surnames, values are corresponding dataframes
    # --- 1. Name/Surname Selection ---
    if "surnames" in page_name:
        name_surname_selection = cols[1].radio( "Select name or surname", ["Name", "Surname"], key="name_surname_selection").lower()
        st.session_state["name_surname_rb"] = name_surname_selection

    # --- 2. Date Filtering ---
    # Ensure year_1 and year_2 exist in session state
    selected_years = range(st.session_state["year_1"], st.session_state["year_2"] + 1)

    # --- 3. Gender Selection Logic ---
    disable = (name_surname_selection == "surname")

    # Define keys for clarity
    gender_list_state_key = "sex_" + page_name
    widget_key = "gender_radio_widget_" + page_name # used for sub-folder name in saving clustering results

    # 1. One-time Initialization
    # If the widget hasn't been initialized yet, set its initial value
    # based on the existing list data (if any).
    if widget_key not in st.session_state:
        # Default to "Both"
        initial_val = "Male"
        # If we have previous list data, sync the widget to match it
        if gender_list_state_key in st.session_state:
            current_list = st.session_state[gender_list_state_key]
            if current_list == ["male","female"]:
                initial_val = "Both genders"
            elif current_list == ["female"]:
                initial_val = "Female"

        st.session_state[widget_key] = initial_val

    # 2. Render Widget
    gender_selection = cols[0].radio("Select Gender", ["Male", "Female","Both genders"], key=widget_key,label_visibility="collapsed",disabled=disable )
    gender_selection_dict = {"Male":["male"],"Female":["female"],"Both genders":["male","female"]}
    # 3. Update the Data List based on the Widget's new value
    st.session_state[gender_list_state_key] = gender_selection_dict[gender_selection]
    # --- 4. Override for Surnames ---
    # If surname is selected, we force both genders (or ignore gender column)
    if disable:
        st.session_state[gender_list_state_key] = ["male", "female"]

    return name_surname_selection, selected_years, gender_list_state_key



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
