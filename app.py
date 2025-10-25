import streamlit as st
from utils.io import load_raw_data
from utils.prep import clean_data, analyze_data, filter_data, translate_data
from utils.viz import (
    plot_age_histogram,
    plot_age_boxplot,
    plot_age_violin,
    plot_age_scatter,
    plot_age_heatmap,
    plot_world_map
)
from sections.intro import show_intro
from sections.conclusions import show_conclusion

st.set_page_config(page_title="Streamlit Dashboard - Paris 2024 Athletes Ages", layout="wide")


st.markdown("""
    <style>
    /* Entire page background */
    .stApp {
        background-color: #071F32;
    }

    /* Customize sidebar */
    section[data-testid="stSidebar"] {
        background-color: #DAC36C;
        color: #071F32;
    }
    </style>
""", unsafe_allow_html=True)



# Load raw data
raw_df = load_raw_data()
translated_df = translate_data(raw_df)

show_intro()

# Show raw data issues
st.markdown("### Initial Data check")
st.write("Missing values per column:")
st.write(translated_df.isnull().sum())

st.info("""
**The processing & cleaning strategy is as followed:**
- Renaming columns from French to English
- Removing unused columns (like Function, Competition locations, Medals, etc.).
- Dropping duplicate rows.
- Converting birth dates to datetime.
- Filling missing heights with the median value.
- Removing rows missing essential fields (Discipline and/or Gender, and Age if still missing).
""")

# Clean and analyze
df_clean = clean_data(raw_df)
summary_stats, age_by_sport_gender = analyze_data(df_clean)


# Sidebar filters
with st.sidebar:
    st.header("Filters")
    disciplines = st.multiselect(":gray[Select Sport]", sorted(df_clean['Sport'].dropna().unique())
                                 , help = "Choose one or more sports to filter the athletes displayed in the visualizations.")
    gender = st.selectbox(":gray[Gender]", ["All"] + sorted(df_clean['Gender'].dropna().unique())
                          , help = "Select a gender to filter the athletes displayed in the visualizations.")
    age_range = st.slider(":gray[Age Range]", int(df_clean['Age'].min()), int(df_clean['Age'].max()),
                          (int(df_clean['Age'].min()), int(df_clean['Age'].max()))
                          , help = "Adjust the age range to filter athletes displayed in the visualizations.")

# Apply filters
filtered_df = filter_data(df_clean, disciplines, gender, age_range)

# KPI row
st.markdown("### Key Metrics")
c1, c2, c3 = st.columns(3)
c1.metric("Youngest Athlete", f"{filtered_df['Age'].min()} yrs")
c2.metric("Oldest Athlete", f"{filtered_df['Age'].max()} yrs")
c3.metric("Median Age", f"{int(filtered_df['Age'].median())} yrs")

# Visualizations with purpose and insights
st.subheader("Age Distribution")
st.caption("**Purpose:** Show the overall spread of athlete ages to identify dominant age groups.")
plot_age_histogram(filtered_df)
st.caption("**Interpretation:** Most athletes cluster between 20–30 years, highlighting the prime competitive age.")

st.subheader("Age by Discipline")
st.caption("**Purpose:** Compare age ranges across sports to see which favor youth or experience.")
plot_age_boxplot(filtered_df)
st.caption("**Interpretation:** Gymnastics and skateboarding athletes are the youngest, while equestrian and shooting favor older athletes")

st.subheader("Age by Gender")
st.caption("**Purpose:** Explore whether gender influences age distribution in different sports.")
plot_age_violin(filtered_df)
st.caption("**Interpretation:** Gender differences are minimal overall, except in gymnastics where women tend to be younger.")

st.subheader("Age vs Competitions")
st.caption("**Purpose:** Understand if older athletes participate in fewer or more events.")
plot_age_scatter(filtered_df)
st.caption("**Interpretation:** Older athletes often compete in fewer events, suggesting specialization or endurance limits")

st.subheader("Median Age by Sport & Gender")
st.caption("**Purpose:** Provide a quick view of gender-age patterns using small multiples.")
plot_age_heatmap(filtered_df)
st.caption("**Interpretation:** Most sports show similar median ages for men and women, reinforcing gender parity in age diversity.")

st.subheader("World Map of Athlete Age")
st.caption("**Purpose:** See how athlete age varies globally by country.")

# Horizontal layout for dropdown and map
col1, col2 = st.columns([1, 4])

with col1:
    age_metric = st.selectbox(
        "Select Age Metric",
        ["median", "min", "max"],
        index=0,
        help="Choose which age metric to display on the world map."
    )


interpretation = {
    "median": "Globally, the median athlete age of the countries around the world stays approximatly the same. However, we can spot that Africa and Asia are two continents whose median athlete age may be slightly lower than in other continents, depending on the countries."
    " Countries with older athletes may focus on experience-based sports, while those with younger athletes might emphasize agility and endurance disciplines.",
    "min": "Developed countries of America, Europe, Asia and Australia show no clear difference in the age of their yougest ahtletes. However, in Africa, it is clear that they have less young athletes than in the other continents. "
    " Countries with very young athletes may be nurturing emerging talent, while those with higher minimum ages might prioritize seasoned competitors.",
    "max": "Developed countries in America, Europe and Oceania tend to have older athletes that the other countries. We observe that Africa is the continent with the less old athletes. "
    " Countries with very old athletes may value experience and longevity in sports, while those with lower maximum ages might focus on youth participation."
}

with col2:
    plot_world_map(filtered_df, agg_func=age_metric)

# Compute highest and lowest countries for interpretation
age_by_country = filtered_df.groupby("Country")["Age"].agg(age_metric).reset_index()
age_by_country.columns = ["Country", "Age"]

max_row = age_by_country.loc[age_by_country["Age"].idxmax()]
min_row = age_by_country.loc[age_by_country["Age"].idxmin()]

st.caption("Results:")
st.markdown(f"**Highest {age_metric.capitalize()} Age:** {max_row['Country']} ({max_row['Age']:.1f} yrs)")
st.markdown(f"**Lowest {age_metric.capitalize()} Age:** {min_row['Country']} ({min_row['Age']:.1f} yrs)")
st.caption(interpretation[age_metric])


# Conclusion
show_conclusion()