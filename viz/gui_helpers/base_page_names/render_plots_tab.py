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

def render_rank_filtering_panel(col_1,page_name,names):
    expression_in_sentence = "names or surnames" if page_name == "names_surnames" else "baby names"
    selected_names = col_1.multiselect(f"Filter {expression_in_sentence} (optional)", names)
    use_rank_filtering = col_1.toggle("Use rank filtering", value=True)
    with col_1.container(border=True):
        col_1_1, _ = st.columns([3, 1])
        top_n = col_1_1.selectbox(f"Filter top-n", range(1, 11), index=4, key="rank_" + page_name,
                                  disabled=not use_rank_filtering)
        include_all_years = col_1_1.radio("Select an option",
                                          ["Show Only Years When Names Are in Top-n",
                                           "Include All Years for Names Ever in Top-n"],
                                          key="include_all_years", disabled=not use_rank_filtering)
        n_for_second_filter = col_1_1.selectbox(
            'Second filter (Only applies if "include all years option" is selected',
            [
                "No second filter",
                "Always in top-10",
                "Always in top-20",
                "Always in top-50",
                "Always in top-100",
                "Always in top-200",
                "Always in top-300",
                "Always in top-400",
                "Always in top-500",
                "Always in top-600",
                "Always in top-1000",
                "Always in top-2000",
                "Always in top-3000",
                "Always in top-4000",
                "Always in top-5000","Always in top-10000","Always in top-20000"
            ],
            key="always_top_filter_" + page_name, disabled=not use_rank_filtering
        )
    return selected_names,use_rank_filtering,top_n,include_all_years,n_for_second_filter

def render_rank_and_trend_sub_tabs(page_name, clusters, names, geo_level, tab_selected):
    """ Helper function for rendering 'Rank Bump Plot' & 'Rank Bar & Line Plot' (sub-tabs 2.2 & 2.3 of 'Plots Tab')  and 'Name Trend Analysis' (1.3 of 'Clustering Tab') """
    col_1, col_2,col_3,col_4,col_5  = st.columns([3,1,2,1,1])
    selected_names, use_rank_filtering, top_n, include_all_years, n_for_second_filter= render_rank_filtering_panel(col_1,page_name,names)

    use_province_or_cluster, selected_n_cluster = None, None
    if tab_selected=="rank_bar_line" : # ratio is only used for line plot
        use_count_or_ratio = col_2.radio("Select an option:", ["Use count", "Use ratio"])
        show_column="ratio" if "ratio" in use_count_or_ratio else "count"
    else:
        show_column="ratio"
    show_provinces_separately = col_3.toggle(f"Show provinces separately(does not aggregate counts for selected provinces)", value=False)
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
    return selected_names,use_rank_filtering,top_n,include_all_years,n_for_second_filter,use_province_or_cluster,show_column,selected_n_cluster,show_provinces_separately,plotter_engine,plot_style
