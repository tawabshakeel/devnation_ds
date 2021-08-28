import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('coinmarketcap_06122017.csv')
market_cap_raw = df[['id', 'market_cap_usd']]
market_cap_raw.count()

cap = market_cap_raw.query('market_cap_usd > 0')
cap.count()

cap.sort_values(by=['market_cap_usd'], ascending=False,inplace=True)
cap10 = cap.head(10)
sum_of_all = cap10['market_cap_usd'].sum()
cap10['market_cap_pcd'] =  (cap10['market_cap_usd'] / sum_of_all)*100
cap10['market_cap_pcd']
cap10.head(10).plot(x='id',y='market_cap_pcd',kind='bar')

COLORS = ['yellow', 'green', 'orange', 'cyan', 'cyan', 'blue', 'silver', 'orange', 'red', 'green']

ax = cap10.plot.bar(x='id', y='market_cap_usd', logy=True, color=COLORS)
ax.set_ylabel('USD')

volatility = df[['id', 'percent_change_24h', 'percent_change_7d']]
volatility = volatility.set_index('id').dropna()
volatility = volatility.sort_values('percent_change_24h', ascending = True)
volatility.head()

def top10_subplot(volatility_series, title):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    ax = (volatility_series[:10].plot.bar(color = 'red', ax = axes[0]))
    fig.suptitle(title)
    ax.set_ylabel('% change')
    ax = (volatility_series[-10:].plot.bar(color = 'blue', ax = axes[1]))
    return fig, ax

DTITLE = "24 hours top losers and winners"

fig, ax = top10_subplot(volatility.percent_change_24h, DTITLE)

volatility7d = volatility.sort_values('percent_change_7d', ascending = True)

WTITLE = "Weekly top losers and winners"

fig, ax = top10_subplot(volatility7d.percent_change_7d, WTITLE)


largecaps = cap.query('market_cap_usd > 10000000000')

largecaps