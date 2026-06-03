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


def render_tab_selection(page_name,geo_level=None):
    # if "selected_tab" not in st.session_state:
    #    st.session_state["selected_tab_"+self.page_name] = "map"
    tabs_main = [stx.TabBarItemData(id="tab_main_algorithmic", title="Clustering & Trend Analysis Tabs", description=""),
                 stx.TabBarItemData(id="tab_main_plot", title="Plot Tabs", description="")
                 ]
    tab_main_selected = stx.tab_bar(data=tabs_main, default="tab_main_algorithmic")

    if tab_main_selected == "tab_main_algorithmic":
        tabs=[stx.TabBarItemData(id="tab_name_trend_analysis", title="Name Trend Analysis", description="")]
        if geo_level:
            tabs.extend([stx.TabBarItemData(id="tab_geo_clustering", title="Geographical Clustering", description=""),
                    stx.TabBarItemData(id="tab_name_clustering", title="Name Clustering", description="")])
        st.session_state["selected_tab_" +page_name] = stx.tab_bar(data=tabs, default="tab_name_trend_analysis")
    else:
        tabs=[stx.TabBarItemData(id="rank_bump", title="Rank Bump Plot", description=""),
        stx.TabBarItemData(id="rank_bar_line", title="Rank Bar & Line Plot", description="")]
        if geo_level:
            tabs.append(stx.TabBarItemData(id="tab_map", title="Map Plot", description=""))
        st.session_state["selected_tab_" + page_name] = stx.tab_bar(data=tabs, default="rank_bump")
    return st.session_state["selected_tab_" +page_name]

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


def render_data_coverage_if_rank_available(max_rank):
        use_data_option = st.radio("**Data coverage**", ["Use all data","Use top-n names"],index=1)
        top_n_names = render_top_n_selector(max_rank)
        return use_data_option, top_n_names

def render_top_n_selector(max_n):
    col1,col2=st.columns([15,85])
    return col1.number_input("Top-n", min_value=1, max_value=max_n,  value=30,  key="top_n_names")


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
