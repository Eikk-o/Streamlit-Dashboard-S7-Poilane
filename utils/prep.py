import pandas as pd

def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()

    # Convert birth date to datetime
    if 'Date de naissance' in df.columns:
        df['Date de naissance'] = pd.to_datetime(df['Date de naissance'], errors='coerce')

    # Compute age if missing
    if 'Âge' not in df.columns or df['Âge'].isnull().any():
        ref_date = pd.Timestamp('2024-08-01')
        df['Âge'] = ((ref_date - df['Date de naissance']).dt.days / 365).astype('Int64')

    # Fill missing heights with median
    if 'Taille (en cm)' in df.columns:
        df['Taille (en cm)'] = pd.to_numeric(df['Taille (en cm)'], errors='coerce')
        df['Taille (en cm)'].fillna(df['Taille (en cm)'].median(), inplace=True)

    # Remove rows missing essential fields
    df = df.dropna(subset=['Discipline', 'Genre', 'Âge'])

    return df

def analyze_data(df):
    summary = {
        "mean_age": round(df['Âge'].mean(), 1),
        "median_age": int(df['Âge'].median()),
        "min_age": int(df['Âge'].min()),
        "max_age": int(df['Âge'].max()),
        "rows_after_cleaning": len(df)
    }
    age_by_sport_gender = df.groupby(['Discipline', 'Genre'])['Âge'].median().reset_index()
    return summary, age_by_sport_gender

def filter_data(df, disciplines, gender, age_range):
    filtered = df.copy()
    if disciplines:
        filtered = filtered[filtered['Discipline'].isin(disciplines)]
    if gender != "All":
        filtered = filtered[filtered['Genre'] == gender]
    filtered = filtered[(filtered['Âge'] >= age_range[0]) & (filtered['Âge'] <= age_range[1])]
    return filtered