import locale

import extra_streamlit_components as stx
import streamlit as st

# not used currently
def load_css(file_path: str) -> None:
    """
    Load CSS from a file and inject it into the Streamlit app using st.markdown.
    Args: file_path: Path to the CSS file.
    """
    try:
        with open(file_path, "r") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        print(f"CSS file not found: {file_path}")
    except Exception as e:
        print(f"CSS file not found: {file_path}")

def sidebar_controls_plot_options_setup(page_name):
    sidebar = st.sidebar
    if st.session_state.get("selected_tab_" + page_name, "map") == "map":
        st.session_state["visualization_option"] = sidebar.radio("Choose visualization option",
                                                                 ["Matplotlib", "Folium"]).lower()

def render_tab_selection(page_name):
    # if "selected_tab" not in st.session_state:
    #    st.session_state["selected_tab_"+self.page_name] = "map"
    tabs_main = [stx.TabBarItemData(id="tab_main_clustering", title="Clustering Tabs", description=""),
                 stx.TabBarItemData(id="tab_main_plot", title="Plots Tab", description="")
                 ]
    tab_main_selected = stx.tab_bar(data=tabs_main, default="tab_main_clustering")

    if tab_main_selected == "tab_main_clustering":
        tabs = [stx.TabBarItemData(id="tab_geo_clustering", title="Geographical Clustering", description=""),
                stx.TabBarItemData(id="tab_name_clustering", title="Name Clustering", description="") ]
        st.session_state["selected_tab_" +page_name] = stx.tab_bar(data=tabs, default="tab_geo_clustering")
    else:
        tabs = [ stx.TabBarItemData(id="tab_map", title="Map Plot", description=""),
                 stx.TabBarItemData(id="rank_bump", title="Rank Bump Plot", description=""),
                 stx.TabBarItemData(id="rank_bar", title="Rank Bar Plot", description=""),
                 stx.TabBarItemData(id="custom_bar", title="Custom Name Bar Plot", description="")]
        st.session_state["selected_tab_" + page_name] = stx.tab_bar(data=tabs, default="tab_map")
    return st.session_state["selected_tab_" +page_name]

def render_gender_name_surname_filters(page_name,cols):
    """ Common helper function for rendering
     'Names and Surnames' page and 'Baby Names' pages
    """
    name_surname_selection = "name"
    # data is a dictionary whose keys are names and surnames, values are corresponding dataframes
    # --- 1. Name/Surname Selection ---
    if page_name == "names_surnames":
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
        initial_val = "Both genders"
        # If we have previous list data, sync the widget to match it
        if gender_list_state_key in st.session_state:
            current_list = st.session_state[gender_list_state_key]
            if current_list == ["male"]:
                initial_val = "Male"
            elif current_list == ["female"]:
                initial_val = "Female"

        st.session_state[widget_key] = initial_val

    # 2. Render Widget
    gender_selection = cols[0].radio("Select Gender", ["Both genders", "Male", "Female"], key=widget_key,label_visibility="collapsed",disabled=disable )
    gender_selection_dict = {"Male":["male"],"Female":["female"],"Both genders":["male","female"]}
    # 3. Update the Data List based on the Widget's new value
    st.session_state[gender_list_state_key] = gender_selection_dict[gender_selection]
    # --- 4. Override for Surnames ---
    # If surname is selected, we force both genders (or ignore gender column)
    if disable:
        st.session_state[gender_list_state_key] = ["male", "female"]

    return name_surname_selection, selected_years, gender_list_state_key

def render_rank_plot_sub_tabs(page_name,clusters):
    """ Helper function for rendering 'Rank Bump Plot' & 'Rank Bar Plot' sub-tabs of 'Plots Tab' """
    col_1, col_2, col_3,_ = st.columns([2,1,2,2])
    col_1.selectbox(f"Select rank", range(1, 21), index=4, key="rank_" + page_name)
    col_1.radio("Select an option",
                 ["Show Only Years When Names Are in Top-n", "Include All Years for Names Ever in Top-n"],
                 key="include_all_years")
    return _render_common_helper_bar(col_2, col_3, clusters)


def render_custom_bar_plot_sub_tab(page_name,clusters,names):
    """ Helper function for rendering 'Custom Bar Plot'"""
    col_1, col_2, col_3,_ = st.columns([2,1,2,2])
    expression_in_sentence = "names or surnames" if page_name == "names_surnames" else "baby names"
    # names_surnames has extra name-surname radio group overlapping with name selector,if so move the selector to right col
    #empty_col = col_4 if self.page_name == "names_surnames" else col_2
    col_1.multiselect(f"Select {expression_in_sentence}", names, key="names_" + page_name)
    return _render_common_helper_bar(col_2, col_3, clusters)

def _render_common_helper_bar(col_2, col_3, clusters):
    use_province_or_cluster = col_2.radio("Select an option", options=["Use provinces", "Use clusters"],
                                          key="province_or_cluster").lower()
    selected_n_cluster = col_3.multiselect(f"Select clusters (default all)", clusters)
    show_provinces_separately = col_3.checkbox(f"Show provinces separately(does not aggregate counts for selected provinces)")
    return use_province_or_cluster, selected_n_cluster, show_provinces_separately


def render_top_n_selector(max_n):
    return st.number_input("", min_value=1, max_value=max_n,  value=30,  key="top_n_names")