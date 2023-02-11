import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt


def get_avg_price(market,market_metrics,market_id):
    avg_prices = market_metrics.groupby('market_id')['median_sale_price'].mean()
    avg_prices=pd.DataFrame(avg_prices)
    m_id=market_id['market_id']
    avg_prices['m_id']=sorted(m_id)

    plt.bar(avg_prices['m_id'],avg_prices['median_sale_price'])
    plt.show()


def UI():

    market_id=st.text_input('Enter the Market ID to get the score')
    st.text(f"The Score is {market_id}")



market=pd.read_csv("E:\Zero-Down Hackathon\Market Hotness\market.csv")
market_metrics=pd.read_csv("E:\Zero-Down Hackathon\Market Hotness\market_metrics.csv")
market_id=market_metrics.groupby('market_id').count().reset_index()


# Removing null values from market dataframe
market_nan = market.isnull().sum().sum()
market=market.dropna()

# Removing the null values present in the market metrics dataframe
metric_nan = market_metrics['median_list_price_psqft'].isnull().sum().sum()


# Filling the missing datas 
market_metrics=market_metrics[market_metrics["days_to_pending"].isna() & market_metrics["days_to_sell"].isna()]
market_metrics=market_metrics[market_metrics["sold_homes_count"]<5]
market_metrics=market_metrics[market_metrics["new_listings_count"]<10]

indices=list(market_metrics.index)
market_metrics=market_metrics.drop(indices)

market_metrics.days_to_pending.fillna(market_metrics.days_to_sell, inplace=True)
market_metrics.days_to_sell.fillna(market_metrics.days_to_pending, inplace=True)


#UI()
