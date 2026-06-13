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


def render_rank_and_trend_sub_tabs(page_name, clusters, names, geo_level, tab_selected):
    """ Helper function for rendering 'Rank Bump Plot' & 'Rank Bar & Line Plot' (sub-tabs 2.2 & 2.3 of 'Plots Tab')  and 'Name Trend Analysis' (1.3 of 'Clustering Tab') """
    col_1, col_2,col_3,col_4,col_5  = st.columns([3,1,2,1,1])
    selected_names, use_rank_filtering, top_n, include_all_years, secondary_top_k_filter,always_or_appeared_in_top_k= render_rank_and_trend_sub_tabs_helper_rank_filtering_panel(col_1, page_name, names)
    use_province_or_cluster, selected_n_cluster = None, None
    if tab_selected=="rank_bar_line" : # ratio is only used for line plot
        use_count_or_ratio = col_2.radio("Select an option:", ["Use count", "Use ratio"])
        show_column="ratio" if "ratio" in use_count_or_ratio else "count"
    else:
        show_column="ratio"
    if geo_level:
        show_provinces_separately = col_3.toggle(f"Show provinces separately(does not aggregate counts for selected provinces)", value=False)
    else:
        show_provinces_separately = False
    if tab_selected=="rank_bar_line" and geo_level != None:
        use_province_or_cluster = col_3.radio("Select an option", options=[f"Use {geo_level}s", "Use clusters"],
                                          key="province_or_cluster").lower()
        selected_n_cluster = col_3.multiselect(f"Select clusters (default all)", clusters)
    else:
        use_province_or_cluster = ""

    plotter_engine = col_4.radio("Select plotter engine",
                      options=["Matplotlib", "Seaborn", "Plotly",  "Altair"],
                      index=3,
                      # key=f"bump_engine_{page_name}",
                      )
    # col_5 is used for bar&line plots (sub-tab 2.3 & 2.4), it is not used for rank bump plot
    plot_style = ""
    if "line" in tab_selected:
        plot_style = col_5.radio("Select plot style:", ["Line plot","Bar plot"] )
    return selected_names,use_rank_filtering,top_n,include_all_years,secondary_top_k_filter,always_or_appeared_in_top_k,use_province_or_cluster,show_column,selected_n_cluster,show_provinces_separately,plotter_engine,plot_style


def render_rank_and_trend_sub_tabs_helper_rank_filtering_panel(col_1, page_name, names):
    expression_in_sentence = "names or surnames" if page_name == "names_surnames" else "baby names"
    selected_names = col_1.multiselect(f"Filter {expression_in_sentence} (optional)", names)
    use_rank_filtering = col_1.toggle("Use rank filtering", value=True)
    with col_1.container(border=True):
        col_1_1, _ = st.columns([3, 1])
        top_n = col_1_1.selectbox(f"Filter (appeared at least once in) top-n",
                                  range(1, 11) if "usa" in page_name else range(1, 31), index=4,
                                  key="rank_" + page_name,
                                  disabled=not use_rank_filtering)
        include_all_years = col_1_1.radio("Select an option",
                                          ["Show Only Years When Names Are in Top-n",
                                           "Include All Years for Names Ever in Top-n"],
                                          key="include_all_years", disabled=not use_rank_filtering)
        thresholds = [10, 20, 50, 100, 200, 300, 400, 500, 600, 1000, 2000, 3000, 4000, 5000, 10000, 20000]
        options = ["No second filter"]
        for t in thresholds:
            options.append(f"Always in top-{t}")

        key = "always_top_filter_" + page_name
        disabled = not use_rank_filtering or not include_all_years
        secondary_top_k_filter = col_1_1.selectbox(
            'Secondary filter (only applies if "include all years option" is selected', options, key=key,
            disabled=disabled)
        always_or_appeared_in_top_k_label = st.radio(
            "Select how to apply the second filter:",  # Etiket
            ["Show names that always appeared in top-k every year",
             "Show names with missing years (NaN) that appeared in top-k when ranked"])
        always_or_appeared_in_top_k = (
                    always_or_appeared_in_top_k_label == "Show names that always appeared in top-k every year")

    return selected_names, use_rank_filtering, top_n, include_all_years, secondary_top_k_filter, always_or_appeared_in_top_k


def render_tab_selection(page_name,geo_level=None):
    # if "selected_tab" not in st.session_state:
    #    st.session_state["selected_tab_"+self.page_name] = "map"
    tabs_main = [stx.TabBarItemData(id="tab_main_algorithmic", title="Clustering & Trend Analysis Tabs", description=""),
                 stx.TabBarItemData(id="tab_main_plot", title="Plot Tabs", description="")]

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


def render_data_type():
    return st.radio("Select trend analysis type", ["Use ratios", "Use year‑over‑year ratio differences"])

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
