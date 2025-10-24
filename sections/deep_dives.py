import streamlit as st
from utils.viz import (
    plot_age_histogram,
    plot_age_boxplot,
    plot_age_violin,
    plot_age_scatter,
    plot_age_heatmap
)

def show_deep_dives(df):
    st.header("Deep Dives")
    st.write("Detailed comparisons and distributions.")
    plot_age_histogram(df)
    plot_age_boxplot(df)
    plot_age_violin(df)
    plot_age_scatter(df)
    plot_age_heatmap(df)