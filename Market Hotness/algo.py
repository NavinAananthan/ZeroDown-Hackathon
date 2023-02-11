import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt


def get_avg_price(market_metrics):

    avg_prices = market_metrics.groupby('market_id',as_index=False)['median_sale_price'].mean()
    return avg_prices


def UI(avg_price):

    market_id=st.text_input('Enter the Market ID to get the score')
    st.text(f"The Score is {market_id}")

    st.line_chart(avg_price)



market=pd.read_csv("E:\Zero-Down Hackathon\Market Hotness\market.csv")
market_metrics=pd.read_csv("E:\Zero-Down Hackathon\Market Hotness\market_metrics.csv")
market_id=market_metrics.groupby('market_id').count().reset_index()


# Removing null values from market dataframe
market_nan = market.isnull().sum().sum()
market=market.dropna()

# Removing the null values present in the market metrics dataframe
metric_nan = market_metrics['median_list_price_psqft'].isnull().sum().sum()


# Filling the missing datas 
pending_housedata=market_metrics[market_metrics["days_to_pending"].isna() & market_metrics["days_to_sell"].isna()]
pending_housedata=pending_housedata[pending_housedata["sold_homes_count"]<5]
pending_housedata=pending_housedata[pending_housedata["new_listings_count"]<10]
pending_housedata

indices=list(pending_housedata.index)
metrics=market_metrics.drop(indices)

metrics.days_to_pending.fillna(metrics.days_to_sell, inplace=True)
metrics.days_to_sell.fillna(metrics.days_to_pending, inplace=True)


avg_price=get_avg_price(metrics)

UI(avg_price)
