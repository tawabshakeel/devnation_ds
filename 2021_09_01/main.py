import pandas as pd
import seaborn as sns
gross = pd.read_csv('disney_movies_total_gross.csv', parse_dates  = ['release_date'])
gross.head()

inflation_adjusted_gross_desc = gross.sort_values(by='inflation_adjusted_gross', ascending=False)

inflation_adjusted_gross_desc.head(10)

gross['release_year'] = pd.DatetimeIndex(gross['release_date']).year
group = gross.groupby(['genre', 'release_year']).mean()
genre_yearly = group.reset_index()
genre_yearly.head(10)

sns.relplot(kind='line', x='release_year', y='inflation_adjusted_gross', hue='genre', data=genre_yearly)

