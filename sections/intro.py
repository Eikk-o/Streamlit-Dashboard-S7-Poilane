import streamlit as st

def show_intro():
    st.header("Introduction")
    st.write("""
    **Context:** The Olympics bring together athletes of all ages. This dashboard explores age diversity across sports.
    **Objectives:** Understand which disciplines favor youth vs. experience.
    **Data Caveats:** Missing height data; age calculated from birth date.
    """)