import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def plot_age_histogram(df):
    fig = px.histogram(df, x='Âge', nbins=20, title='Age Distribution',
                       labels={'Âge': 'Age (years)', 'count': 'Number of Athletes'})
    fig.add_vline(x=30, line_dash="dash", line_color="red", annotation_text="Age 30 threshold")
    fig.update_traces(marker_color='blue')
    fig.update_layout(xaxis_title="Age (years)", yaxis_title="Athletes", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def plot_age_boxplot(df):
    fig = px.box(df, x='Discipline', y='Âge', title='Age by Discipline',
                 labels={'Âge': 'Age (years)', 'Discipline': 'Sport'})
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

def plot_age_violin(df):
    fig = px.violin(df, x='Genre', y='Âge', box=True, points='all',
                    title='Age by Gender', labels={'Âge': 'Age (years)', 'Genre': 'Gender'})
    st.plotly_chart(fig, use_container_width=True)

def plot_age_scatter(df):
    fig = px.scatter(df, x='Âge', y='Nombre de compétitions', color='Discipline',
                     hover_data=['nom'], title='Age vs Competitions',
                     labels={'Âge': 'Age (years)', 'Nombre de compétitions': 'Competitions'})
    fig.add_hline(y=5, line_dash="dot", line_color="green", annotation_text="5 competitions")
    st.plotly_chart(fig, use_container_width=True)

def plot_age_heatmap(df):
    pivot = df.pivot_table(index='Discipline', columns='Genre', values='Âge', aggfunc='median')
    fig = px.imshow(pivot, text_auto=True, aspect='auto', title='Median Age by Sport & Gender',
                    labels={'color': 'Median Age'})
    st.plotly_chart(fig, use_container_width=True)

def plot_map(df):
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', hover_name='nom', color='Discipline',
                                zoom=1, height=500)
        fig.update_layout(mapbox_style='open-street-map')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No geographic data available for map visualization.")