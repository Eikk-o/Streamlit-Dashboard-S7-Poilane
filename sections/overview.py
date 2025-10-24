import streamlit as st

def show_overview(df):
    st.header("Overview")
    st.write("High-level trends in athlete ages.")
    st.metric("Average Age", f"{df['Âge'].mean():.1f} yrs")
    st.metric("Age Range", f"{df['Âge'].min()} - {df['Âge'].max()} yrs")