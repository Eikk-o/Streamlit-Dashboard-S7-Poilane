import streamlit as st

def show_intro():
    st.title("Topic: Diversity of Athletes by Age during Paris 2024 Olympic Games")
    st.caption("Source: Paris 2024 Athletes — Olympics.com — Open License")

    # Problematic
    st.markdown("""
    ### Why ?
    In the Olympic Games, age diversity is not just a curiosity or a random attribute of athletes. It reflects the physical and strategic demands of each sport.
    Thus, understanding these patterns may help federations to design better training programs and inspires fan by showcasing both youth and experience.
    """)

    st.write("""
    **Context:** This dashboard explores age diversity across sports.
    **Objectives:** Understand which disciplines favor youth vs. experience.
    """)

    # Headline insight
    st.markdown("**Insights:** Athletes range from teenagers to veterans, shaping the competitive landscape of each discipline.")