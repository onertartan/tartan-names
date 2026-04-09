import streamlit as st

def render_plot_map_sub_tab(names,page_name):
    # Expression depending on page
    expr = "names or surnames" if page_name == "names_surnames" else "baby names"
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
    return rank, display_option, include_top_n

def render_rank_plot_sub_tabs(page_name,clusters,geo_level):
    """ Helper function for rendering 'Rank Bump Plot' & 'Rank Bar Plot' sub-tabs of 'Plots Tab' """
    col_1, col_2_3_4 = st.columns([2,5])

    col_1.selectbox(f"Select rank", range(1, 11), index=4, key="rank_" + page_name)
    col_1.radio("Select an option",
                 ["Show Only Years When Names Are in Top-n", "Include All Years for Names Ever in Top-n"],
                 key="include_all_years")
    with col_2_3_4:
        return _render_common_helper_for_bar_and_rank_plots(clusters,geo_level)


def render_custom_bar_plot_sub_tab(page_name,clusters,names,geo_level):
    """ Helper function for rendering 'Custom Bar Plot'"""
    col_1, col_2_3_4 = st.columns([2,5])
    expression_in_sentence = "names or surnames" if page_name == "names_surnames" else "baby names"
    # names_surnames has extra name-surname radio group overlapping with name selector,if so move the selector to right col
    #empty_col = col_4 if self.page_name == "names_surnames" else col_2
    col_1.multiselect(f"Select {expression_in_sentence}", names, key="names_" + page_name)
    with col_2_3_4:
        return _render_common_helper_for_bar_and_rank_plots(clusters,geo_level)


def _render_common_helper_for_bar_and_rank_plots(clusters,geo_level):

    col_2,col_3,col_4 = st.columns([1,2,2])
    use_province_or_cluster = col_2.radio("Select an option", options=[f"Use {geo_level}s", "Use clusters"],
                                          key="province_or_cluster").lower()
    show_ratio = col_2.checkbox("Use ratio\n(default count)")
    show_column="ratio" if show_ratio else "count"
    selected_n_cluster = col_3.multiselect(f"Select clusters (default all)", clusters)
    show_provinces_separately = col_3.checkbox(f"Show provinces separately(does not aggregate counts for selected provinces)")
    plotter_engine = col_4.radio("Plot Style",
                      options=["Matplotlib", "Seaborn", "Plotly",  "Altair"],
                      index=3,
                      # key=f"bump_engine_{page_name}",
                      )
    return use_province_or_cluster, selected_n_cluster, show_provinces_separately, plotter_engine, show_column
