import pandas as pd

def translate_data(df):
    # Rename columns from French to English
    df.rename(columns={
        'nom': 'Name',
        'Pays': 'Country',
        'Discipline': 'Sport',
        'Genre': 'Gender',
        'Âge': 'Age',
        'Nombre de compétitions': 'Competitions',
        'Taille (en cm)': 'Height (cm)',
        'Date de naissance': 'Birthdate'
    }, inplace=True)

    # Replace French gender values with English
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].replace({'Homme': 'Male', 'Femme': 'Female'})


    # Country mapping dictionary
    country_mapping = {
        'République populaire de Chine': 'China',
        'Danemark': 'Denmark',
        'Norvège': 'Norway',
        "États-Unis d'Amérique": 'United States',
        'Pays-Bas': 'Netherlands',
        'Suède': 'Sweden',
        'Kazakhstan': 'Kazakhstan',
        'Espagne': 'Spain',
        'Israël': 'Israel',
        'Italie': 'Italy',
        'Qatar': 'Qatar',
        'Albanie': 'Albania',
        'Chili': 'Chile',
        'Équipe olympique des réfugiés': 'Refugee Olympic Team',
        'Türkiye': 'Turkey',
        'Égypte': 'Egypt',
        'République arabe syrienne': 'Syria',
        'Serbie': 'Serbia',
        'Soudan': 'Sudan',
        'Maroc': 'Morocco',
        'Belgique': 'Belgium',
        'Ouzbékistan': 'Uzbekistan',
        "République islamique d'Iran": 'Iran',
        'Singapour': 'Singapore',
        'Maldives': 'Maldives',
        'Azerbaïdjan': 'Azerbaijan',
        'Canada': 'Canada',
        'Ukraine': 'Ukraine',
        'Tadjikistan': 'Tajikistan',
        'Japon': 'Japan',
        'Sri Lanka': 'Sri Lanka',
        'Inde': 'India',
        'Autriche': 'Austria',
        'Slovénie': 'Slovenia',
        'Nigéria': 'Nigeria',
        'Jordanie': 'Jordan',
        'France': 'France',
        'Hongrie': 'Hungary',
        'Suisse': 'Switzerland',
        'Allemagne': 'Germany',
        'Guyana': 'Guyana',
        'Brésil': 'Brazil',
        'Libye': 'Libya',
        'Kenya': 'Kenya',
        'Palestine': 'Palestine',
        'Arabie saoudite': 'Saudi Arabia',
        'Cuba': 'Cuba',
        'Guinée': 'Guinea',
        'Guinée équatoriale': 'Equatorial Guinea',
        'Roumanie': 'Romania',
        'Grèce': 'Greece',
        'Australie': 'Australia',
        'Bahreïn': 'Bahrain',
        'Irlande': 'Ireland',
        'Indonésie': 'Indonesia',
        'Togo': 'Togo',
        'Lituanie': 'Lithuania',
        'Algérie': 'Algeria',
        'Samoa': 'Samoa',
        'Porto Rico': 'Puerto Rico',
        'Portugal': 'Portugal',
        'Mexique': 'Mexico',
        'Colombie': 'Colombia',
        'Pérou': 'Peru',
        'Mauritanie': 'Mauritania',
        'Niger': 'Niger',
        'Iraq': 'Iraq',
        "Côte d'Ivoire": 'Ivory Coast',
        'Finlande': 'Finland',
        'Trinité-et-Tobago': 'Trinidad and Tobago',
        'Kirghizistan': 'Kyrgyzstan',
        'Oman': 'Oman',
        'Émirats arabes unis': 'United Arab Emirates',
        'Yémen': 'Yemen',
        'Koweït': 'Kuwait',
        'Pologne': 'Poland',
        'Argentine': 'Argentina',
        'Angola': 'Angola',
        'Grande-Bretagne': 'United Kingdom',
        'Venezuela': 'Venezuela',
        'République dominicaine': 'Dominican Republic',
        'Nouvelle-Zélande': 'New Zealand',
        'Arménie': 'Armenia',
        'Éthiopie': 'Ethiopia',
        'AIN': 'Independent Athletes',
        'Sainte-Lucie': 'Saint Lucia',
        'Bermudes': 'Bermuda',
        'Saint-Kitts-et-Nevis': 'Saint Kitts and Nevis',
        'Paraguay': 'Paraguay',
        'République de Moldova': 'Moldova',
        'Cabo Verde': 'Cape Verde',
        'Érythrée': 'Eritrea',
        'Mongolie': 'Mongolia',
        'Uruguay': 'Uruguay',
        'Saint-Marin': 'San Marino',
        'Djibouti': 'Djibouti',
        'Ghana': 'Ghana',
        'République de Corée': 'South Korea',
        'République populaire démocratique de Corée': 'North Korea',
        'Malaisie': 'Malaysia',
        'Jamaïque': 'Jamaica',
        'République centrafricaine': 'Central African Republic',
        'Philippines': 'Philippines',
        'Bulgarie': 'Bulgaria',
        'Bahamas': 'Bahamas',
        'Cameroun': 'Cameroon',
        'Thaïlande': 'Thailand',
        'Gambie': 'Gambia',
        'Monaco': 'Monaco',
        'Chypre': 'Cyprus',
        'Afghanistan': 'Afghanistan',
        'Liban': 'Lebanon',
        'Guam': 'Guam',
        'El Salvador': 'El Salvador',
        'Panama': 'Panama',
        'Brunéi Darussalam': 'Brunei',
        'Tchéquie': 'Czech Republic',
        'Géorgie': 'Georgia',
        'République démocratique du Timor-Leste': 'East Timor',
        'Gabon': 'Gabon',
        'Hong Kong, Chine': 'Hong Kong',
        'Afrique du Sud': 'South Africa',
        'Honduras': 'Honduras',
        'Équateur': 'Ecuador',
        'Seychelles': 'Seychelles',
        'Kosovo': 'Kosovo',
        'Fidji': 'Fiji',
        'Burkina Faso': 'Burkina Faso',
        'Zambie': 'Zambia',
        'Slovaquie': 'Slovakia',
        'Comores': 'Comoros',
        'Guatemala': 'Guatemala',
        'Papouasie-Nouvelle-Guinée': 'Papua New Guinea',
        'Pakistan': 'Pakistan',
        'Îles Cook': 'Cook Islands',
        'Tunisie': 'Tunisia',
        'Haïti': 'Haiti',
        'Croatie': 'Croatia',
        'Luxembourg': 'Luxembourg',
        'Tchad': 'Chad',
        'Maurice': 'Mauritius',
        'Lettonie': 'Latvia',
        'Congo': 'Congo',
        'Sénégal': 'Senegal',
        'Îles Vierges britanniques': 'British Virgin Islands',
        'Mali': 'Mali',
        'Guinée-Bissau': 'Guinea-Bissau',
        'Andorre': 'Andorra',
        'Nicaragua': 'Nicaragua',
        'Bosnie-Herzégovine': 'Bosnia and Herzegovina',
        'Chinese Taipei': 'Chinese Taipei',
        'Malawi': 'Malawi',
        'Zimbabwe': 'Zimbabwe',
        'Ouganda': 'Uganda',
        'Malte': 'Malta',
        'Cambodge': 'Cambodia',
        'Grenade': 'Grenada',
        'Îles Caïmans': 'Cayman Islands',
        'Vanuatu': 'Vanuatu',
        'Népal': 'Nepal',
        'Îles Vierges américaines': 'US Virgin Islands',
        'Libéria': 'Liberia',
        'Tonga': 'Tonga',
        'Sao Tomé-et-Principe': 'Sao Tome and Principe',
        'Soudan du Sud': 'South Sudan',
        'Estonie': 'Estonia',
        'République démocratique populaire lao': 'Laos',
        'Suriname': 'Suriname',
        'Viet Nam': 'Vietnam',
        'Mozambique': 'Mozambique',
        'Bhoutan': 'Bhutan',
        'Bénin': 'Benin',
        'Costa Rica': 'Costa Rica',
        'Monténégro': 'Montenegro',
        'Botswana': 'Botswana',
        'Macédoine du Nord': 'North Macedonia',
        'Aruba': 'Aruba',
        'Kiribati': 'Kiribati',
        'Barbade': 'Barbados',
        'Madagascar': 'Madagascar',
        'Îles Salomon': 'Solomon Islands',
        'États fédérés de Micronésie': 'Micronesia',
        'Palaos': 'Palau',
        'Burundi': 'Burundi',
        'Bolivie': 'Bolivia',
        'République-Unie de Tanzanie': 'Tanzania',
        'Belize': 'Belize',
        'Antigua-et-Barbuda': 'Antigua and Barbuda',
        'Saint-Vincent-et-les-Grenadines': 'Saint Vincent and the Grenadines',
        'Islande': 'Iceland',
        'Myanmar': 'Myanmar',
        'Turkménistan': 'Turkmenistan',
        'Somalie': 'Somalia',
        'Îles Marshall': 'Marshall Islands',
        'Eswatini': 'Eswatini',
        'Samoa américaines': 'American Samoa',
        'Rwanda': 'Rwanda',
        'Bangladesh': 'Bangladesh',
        'Namibie': 'Namibia',
        'Nauru': 'Nauru',
        'République démocratique du Congo': 'Democratic Republic of the Congo',
        'Sierra Leone': 'Sierra Leone',
        'Dominique': 'Dominica',
        'Tuvalu': 'Tuvalu',
        'Lesotho': 'Lesotho',
        'Liechtenstein': 'Liechtenstein'
    }

    df['Country'] = df['Country'].replace(country_mapping)

    # Drop unused columns
    columns_to_keep = ['Name', 'Sport', 'Birthdate', 'Country', 'Age', 'Height (cm)', 'Gender', 'Competitions']
    df = df[columns_to_keep]

    return df


def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()

    # Convert birthdate to datetime
    if 'Birthdate' in df.columns:
        df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')

    # Compute age if missing
    if 'Age' not in df.columns or df['Age'].isnull().any():
        ref_date = pd.Timestamp('2024-08-01')
        df['Age'] = ((ref_date - df['Birthdate']).dt.days / 365).astype('Int64')

    # Fill missing heights with median
    if 'Height (cm)' in df.columns:
        df['Height (cm)'] = pd.to_numeric(df['Height (cm)'], errors='coerce')
        df['Height (cm)'].fillna(df['Height (cm)'].median(), inplace=True)

    # Remove rows missing essential fields
    df = df.dropna(subset=['Sport', 'Gender', 'Age'])

    return df


def analyze_data(df):
    summary = {
        "mean_age": round(df['Age'].mean(), 1),
        "median_age": int(df['Age'].median()),
        "min_age": int(df['Age'].min()),
        "max_age": int(df['Age'].max()),
        "rows_after_cleaning": len(df)
    }
    age_by_sport_gender = df.groupby(['Sport', 'Gender'])['Age'].median().reset_index()
    return summary, age_by_sport_gender

def filter_data(df, disciplines, gender, age_range):
    filtered = df.copy()
    if disciplines:
        filtered = filtered[filtered['Sport'].isin(disciplines)]
    if gender != "All":
        filtered = filtered[filtered['Gender'] == gender]
    filtered = filtered[(filtered['Age'] >= age_range[0]) & (filtered['Age'] <= age_range[1])]
    return filtered