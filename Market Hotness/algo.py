import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt


def get_avg_price(market_metrics):

    avg_prices = market_metrics.groupby('market_id',as_index=False)['median_sale_price'].mean()
    return avg_prices


def getmaxscore(price,score):
    for index,row in price.iterrows():
        if(row['median_sale_price']==score):
            mid=row['market_id']
            break

    return mid



def getscore(id,price):
    for index,row in price.iterrows():
        if(row['market_id']==id):
            score=row['median_sale_price']
            break

    return score



def display_avg_price(avg_price,max_market,max_score):
    st.write("")
    st.write("")
    st.write("")
    st.text("Graph for the Avg sales price and their corresponding market_id")
    st.line_chart(pd.DataFrame(avg_price))

    st.text(f"The max sales {max_score} has been done by the market id {max_market}")



def UI(avg_price):

    mid=st.text_input('Enter the Market ID to get the score')
    st.text("The score is: ")
    



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


indices=list(pending_housedata.index)
metrics=market_metrics.drop(indices)

metrics.days_to_pending.fillna(metrics.days_to_sell, inplace=True)
metrics.days_to_sell.fillna(metrics.days_to_pending, inplace=True)


avg_price=get_avg_price(metrics)
price=pd.DataFrame(avg_price)

max_score=max(price['median_sale_price'])
max_market=getmaxscore(price,max_score)

UI(price)
display_avg_price(price,max_market,max_score)
