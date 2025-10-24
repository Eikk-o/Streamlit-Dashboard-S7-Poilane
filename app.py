import streamlit as st
from utils.io import load_raw_data
from utils.prep import clean_data, analyze_data, filter_data
from utils.viz import (
    plot_age_histogram,
    plot_age_boxplot,
    plot_age_violin,
    plot_age_scatter,
    plot_age_heatmap,
    plot_map
)

st.set_page_config(page_title="Streamlit Dashboard", layout="wide")

# Load raw data
raw_df = load_raw_data()

st.title("Data Storytelling: Diversity of Athletes by Age")
st.caption("Source: Paris 2024 Athletes — Olympics.com — Open License")

# Headline insight
st.markdown("**Headline Insight:** Age diversity at the Olympics spans from teens to veterans, shaping the dynamics of each sport.")

# Show raw data issues
st.markdown("### Initial Data Quality Check")
st.write("Missing values per column:")
st.write(raw_df.isnull().sum())

st.info("""
**Cleaning Strategy:**
- Dropped duplicate rows.
- Converted birth dates to datetime.
- Computed age if missing using reference date (Aug 2024).
- Filled missing heights with median value.
- Removed rows missing essential fields (Discipline, Gender, Age).
""")

# Clean and analyze
df_clean = clean_data(raw_df)
summary_stats, age_by_sport_gender = analyze_data(df_clean)

st.success("Data cleaned successfully! Below are summary statistics after cleaning:")
st.json(summary_stats)

# Sidebar filters (purposeful only)
with st.sidebar:
    st.header("Filters")
    # st.help("Filter athletes by discipline, gender, and age range to explore diversity patterns.")
    disciplines = st.multiselect("Select Disciplines", sorted(df_clean['Discipline'].dropna().unique()))
    gender = st.selectbox("Gender", ["All"] + sorted(df_clean['Genre'].dropna().unique()))
    age_range = st.slider("Age Range", int(df_clean['Âge'].min()), int(df_clean['Âge'].max()),
                          (int(df_clean['Âge'].min()), int(df_clean['Âge'].max())))

# Apply filters
filtered_df = filter_data(df_clean, disciplines, gender, age_range)

# KPI row
st.markdown("### Key Metrics")
c1, c2, c3 = st.columns(3)
c1.metric("Youngest Athlete", f"{filtered_df['Âge'].min()} yrs")
c2.metric("Oldest Athlete", f"{filtered_df['Âge'].max()} yrs")
c3.metric("Median Age", f"{int(filtered_df['Âge'].median())} yrs")

# Visualizations with headline insights
st.subheader("Age Distribution")
st.caption("Insight: Most athletes cluster between 20–30 years.")
plot_age_histogram(filtered_df)

st.subheader("Age by Discipline")
st.caption("Insight: Gymnastics skews youngest; equestrian oldest.")
plot_age_boxplot(filtered_df)

st.subheader("Age by Gender")
st.caption("Insight: Gender differences are minimal except in gymnastics.")
plot_age_violin(filtered_df)

st.subheader("Age vs Competitions")
st.caption("Insight: Older athletes often compete in fewer events.")
plot_age_scatter(filtered_df)

st.subheader("Median Age by Sport & Gender")
st.caption("Insight: Small multiples reveal nuanced gender-age patterns.")
plot_age_heatmap(filtered_df)

st.subheader("Map of Competition Venues")
st.caption("Insight: Venues spread across Paris and beyond.")
plot_map(filtered_df)

st.markdown("### Key Insights & Next Steps")
st.success("Younger athletes dominate gymnastics and skateboarding; older athletes excel in equestrian and shooting.")