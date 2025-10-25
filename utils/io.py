import pandas as pd
import streamlit as st

@st.cache_data
def load_raw_data():
    return pd.read_csv("./data/paris2024-athletes.csv", sep=";", encoding="utf-8")