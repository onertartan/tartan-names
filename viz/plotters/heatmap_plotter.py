from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
def plot_heatmap(heatmap_df,x_label,y_label,title):
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        heatmap_df,
        ax=ax,
        cmap="coolwarm",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"label": title},
    )
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)