# Data Storytelling Dashboard: Diversity of Athletes by Age

## 📖 Project Overview
This project is a **Streamlit web application** that tells the story of **age diversity among athletes at the Paris 2024 Olympics**. It explores how age varies across disciplines, genders, and participation levels, using interactive visualizations.

The narrative follows:
- **Hook:** Why age diversity matters in sports.
- **Context:** Olympics unite generations.
- **Insights:** Which sports favor youth vs. experience.
- **Implications:** Training, media coverage, and research directions.

---

## 📂 Folder Structure
```
pp.py
├─ app.py                  # Main Streamlit app
├─ sections/
│  ├─ intro.py            # Context, objectives, data caveats
│  ├─ overview.py         # KPIs, high-level trends
│  ├─ deep_dives.py       # Comparisons, distributions, drilldowns
│  └─ conclusions.py      # Insights, implications, next steps
├─ utils/
│  ├─ io.py               # Data loading and caching
│  ├─ prep.py             # Cleaning and feature engineering
│  └─ viz.py              # Visualization functions
├─ data/
│  └─ paris2024-athletes.csv  # Dataset
├─ assets/                # Optional images/logos
└─ requirements.txt       # Dependencies
```

---

## ✅ Features
- Sidebar filters for discipline and gender.
- KPI metrics (youngest, oldest, median age).
- Five interactive charts:
  1. Histogram of ages
  2. Boxplot by discipline
  3. Violin plot by gender
  4. Scatter plot (age vs competitions)
  5. Heatmap (median age by sport & gender)
- Data quality notes and key insights section.

---

## ⚙️ Installation
1. Clone the repository:
```bash
git clone <your-repo-url>
cd pp.py
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the Streamlit app:
```bash
streamlit run app.py
```
Access the dashboard at `http://localhost:8501`.

---

## 📊 Dataset
- **Source:** Paris 2024 Athletes dataset
- **License:** Open Data (cite original portal)

---

## 🚀 Deployment
You can deploy the app on **Streamlit Cloud**:
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your repo and deploy.

---

## 🛠 Tech Stack
- Python 3.9+
- Streamlit ≥ 1.33
- Pandas, Seaborn, Matplotlib

---

## 📌 Notes
- Document any missing data or caveats in `intro.py`.
- Ensure reproducibility with pinned dependencies.

