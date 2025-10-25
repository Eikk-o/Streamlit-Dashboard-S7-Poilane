# Paris 2024 Olympic Athletes Dashboard

## ¤ Overview ¤
This project is an **interactive Streamlit dashboard** that explores the **age diversity of athletes** participating in the **Paris 2024 Olympic Games**. Using official athlete data, the dashboard provides insights into how age varies across sports, genders, countries, and continents.

---

## ¤ Features ¤
- **Data Cleaning & Preprocessing**:
  - Rename French columns to English.
  - Normalize gender and country names.
  - Compute missing ages and fills missing heights.
  - Drop duplicates and irrelevant columns.

- **Interactive Filters**:
  - Filter by sport, gender, and age range.

- **Visualizations**:
  - Age distribution histogram.
  - Boxplot by sport.
  - Violin plot by gender.
  - Scatter plot (Age vs Competitions).
  - Heatmap (Median age by sport & gender).
  - Choropleth world map (age metrics by country).

- **Dynamic Interpretations**:
  - Highlights countries with highest and lowest ages for selected metric.
  - Adds continent-level analysis to compare geographic trends.

- **Storytelling Conclusion**:
  - A narrative that transforms data into a human story of ambition and diversity.

---

## ¤ Project Structure ¤
```
paris2024-dashboard/
├─ app.py                  # Main Streamlit app
├─ sections/
│  ├─ intro.py            # Introduction
│  ├─ overview.py         # KPIs
│  ├─ deep_dives.py       # Comparisons, distributions, drilldowns
│  └─ conclusions.py      # Conclusion
├─ utils/
│  ├─ io.py               # Data loading and caching
│  ├─ prep.py             # Cleaning and processing
│  └─ viz.py              # Visualization functions
├─ data/
│  └─ paris2024-athletes.csv  # Dataset
└─ requirements.txt       # Dependencies
```

---

## ¤ Data Description ¤
- **Source**: Paris 2024 Athletes dataset (open license).
- **Key Columns**:
  - `Name`, `Sport`, `Country`, `Gender`, `Age`, `Height (cm)`, `Competitions`, `Birthdate`.

---

## ¤ Installation ¤
```bash
# Clone the repository
git clone https://github.com/Eikk-o/Streamlit-Dashboard-S7-Poilane.git
cd paris2024-dashboard

# Install dependencies
pip install -r requirements.txt
```

---

## >> How to Run
```bash
streamlit run app.py
```
Then open the local URL provided by Streamlit.

---

## ¤ Dashboard Insights ¤
- **Age Diversity**: From teenage gymnasts to veteran equestrians, the dashboard reveals striking contrasts.
- **Geographic Trends**:
  - Asia tends to have younger athletes.
  - Europe and Oceania lean older.
  - Africa and South America show balanced age profiles.
- **Implications**:
  - Training programs can adapt to age patterns.
  - Media can spotlight generational contrasts.

---

## ¤ Storytelling Conclusion ¤
The Paris 2024 Olympics is more than a competition, it is a **global narrative of resilience and dreams**. Every number represents a story: a young athlete chasing glory, a veteran defying time, and nations celebrating their cultural approach to sport.

Age is not a limit, it is a lens through which we see the beauty of diversity in sports.

---

## ¤ Future Improvements ¤
- Add performance metrics by age group.
- Explore correlations between age and medal success.
- Enable export of filtered data and visualizations.
