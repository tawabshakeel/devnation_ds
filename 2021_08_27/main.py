from IPython.display import display
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def answer_one():
    musicians_data = pd.read_csv('halftime_musicians.csv')
    return display(musicians_data)
    tv_data=pd.read_csv('tv.csv')
    return display(tv_data)
    super_bowls_data= pd.read_csv('super_bowls.csv')
    return display(super_bowls_data)

answer_one()
def answer_two():
    musicians_data= halftime_musicians.info(self, verbose=None, buf=None, max_cols=None, memory_usage=None, null_counts=None)
    return musicians_data
    tv_data= tv_data.info(self, verbose=None, buf=None, max_cols=None, memory_usage=None, null_counts=None)
    return tv_data

plt.hist(super_bowls_data['combined_pts'])
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()


display(super_bowls_data[super_bowls_data['combined_pts'] < 60])
display(super_bowls_data[super_bowls_data['combined_pts'] < 15])
plt.hist(super_bowls_data.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Numberof Super Bowls')
plt.show()

display(super_bowls_data[super_bowls_data['difference_pts'] == 1])
display(super_bowls_data[super_bowls_data['difference_pts'] >= 35])

tv_data=pd.read_csv('tv.csv')
super_bowls_data= pd.read_csv('super_bowls.csv')
game_tv_data = pd.merge(tv_data[tv_data['super_bowl'] > 1], super_bowls_data, on='super_bowl')
sns.regplot(x='difference_pts', y='share_household', data=game_tv_data)

tv_data=pd.read_csv('tv.csv')
plt.subplot(3, 1, 1)
plt.plot(tv_data['super_bowl'], tv_data['avg_us_viewers'], color='#648FFF')
plt.title('Average Number of US Viewers')


plt.subplot(3, 1, 2)
plt.plot(tv_data['super_bowl'], tv_data['rating_household'], color = '#648FFF')
plt.title('Household Rating')

plt.subplot(3, 1, 3)
plt.plot(tv_data['super_bowl'], tv_data['ad_cost'], color = '#648FFF')

plt.xlabel('SUPER BOWL')
plt.tight_layout()


def answer_seven():
    return halftime_musicians[halftime_musicians['super_bowl'] <= 27]


musicians_data = pd.read_csv('halftime_musicians.csv')
halftime_appearances = musicians_data.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = musicians_data.sort_values('super_bowl', ascending=False)
halftime_appearances[halftime_appearances['super_bowl'] > 1]

musicians_data = pd.read_csv('halftime_musicians.csv')
no_bands = musicians_data[musicians_data.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()
no_bands = no_bands.sort_values('num_songs', ascending=False)
display(no_bands.head(15))

patriots = 'New England Patriots'
rams = 'Los Angeles Rams'
super_bowl_LIII_winner = patriots
print('The winner of Super Bowl LIII will be the', super_bowl_LIII_winner)