import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# Apply consistent theme
def apply_theme(fig):
    fig.update_layout(
        font=dict(family="Arial", size=14, color="#FBFBFB"),
        title_font=dict(size=18, color="#DAC36C"),
        paper_bgcolor="#071F32",
        plot_bgcolor="#071F32",
        legend_title="Legend"
    )
    return fig

def plot_age_histogram(df):
    fig = px.histogram(df, x='Age', nbins=20, title='Age Distribution among athletes',
                       labels={'Age': 'Age (years)', 'Count': 'Number of Athletes'})
    fig.update_traces(marker_color='#27D2FF')
    fig.update_layout(xaxis_title="Age (years)", yaxis_title="Athletes count", showlegend=False, bargap=0.1)
    fig = apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

def plot_age_boxplot(df):
    fig = px.box(df, x='Sport', y='Age', title='Age by Sport',
                 labels={'Age': 'Age (years)', 'Sport': 'Sport'})
    fig.update_layout(xaxis_tickangle=-45)
    fig = apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

def plot_age_violin(df):
    fig = px.violin(df, x='Gender', y='Age', box=True, points='all',
                    title='Age by Gender', labels={'Age': 'Age (years)', 'Gender': 'Gender'})
    fig = apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)


def plot_age_scatter(df):
    fig = px.scatter(df, x='Age', y='Competitions', color='Sport',
                     title='Age vs Competitions',
                     labels={'Age': 'Age (years)', 'Competitions': 'Competitions'})
    fig = apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)


def plot_age_heatmap(df):
    pivot = df.pivot_table(index='Sport', columns='Gender', values='Age', aggfunc='median')
    fig = px.imshow(pivot, text_auto=True, aspect='auto', title='Median Age by Sport & Gender',
                    labels={'color': 'Median Age'})
    fig = apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

def plot_world_map(df, agg_func='median'):
    # Aggregate age by country
    age_by_country = df.groupby('Country')['Age'].agg(agg_func).reset_index()
    age_by_country.columns = ['Country', 'Age']

    # Create choropleth map
    fig = px.choropleth(
        age_by_country,
        locations='Country',
        locationmode='country names',
        color='Age',
        color_continuous_scale='Viridis',
        title=f'{agg_func.capitalize()} Athlete Age by Country',
        labels={'Age': f'{agg_func.capitalize()} Age'}
    )
    
    fig = apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)