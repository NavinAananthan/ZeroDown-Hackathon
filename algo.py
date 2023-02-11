import pandas as pd
import streamlit as st
import numpy as np


def get_avg_price(market_metrics):
    avg_prices = market_metrics.groupby('market_id',as_index=False)['median_sale_price'].mean()
    return avg_prices


def get_avg_days_to_sell(market_metrics):
    return True




def max_score(score,mid,maxscore,maxid):
    st.text("Graph for the Avg sales price and their corresponding market_id")
    st.line_chart(pd.DataFrame(score,mid))
    st.text(f"The max sales {maxscore} has been done by the market id {maxid}")
    st.write("")
    st.write("")
    st.write("")



def avg_sales(score,mid,city,mdi):

    st.text("The below score is based on Average of the Sales after buying it")
    try:
        market_id=st.number_input('Enter the Market ID to get the score')
        ind=mid.index(int(market_id))
        cind=mdi.index(int(market_id))
        st.text(f"The score is: {score[ind]} and the city where it belongs is {city[cind]}")
    except:
        st.warning("Sorry, Enter correct Market id")

   
def day_sell(score,mid):
    st.text("The below score is based on days took to sell")
    try:
        market_id=st.number_input('Enter the Market ID to get the score')
        ind=mid.index(int(market_id))
        st.text(f"The score is: {score[ind]}")
    except:
        st.warning("Sorry, Enter correct Market id")


market=pd.read_csv("E:\Zero-Down Hackathon\market.csv")
market_metrics=pd.read_csv("E:\Zero-Down Hackathon\market_metrics.csv")
market_id=market_metrics.groupby('market_id').count().reset_index()


# Removing null values from market dataframe
market_nan = market.isnull().sum().sum()
market=market.dropna()


# Removing the null values and filling missing data present in the market metrics dataframe
metric_nan = market_metrics['median_list_price_psqft'].isnull().sum().sum()
pending_housedata=market_metrics[market_metrics["days_to_pending"].isna() & market_metrics["days_to_sell"].isna()]
pending_housedata=pending_housedata[pending_housedata["sold_homes_count"]<5]
pending_housedata=pending_housedata[pending_housedata["new_listings_count"]<10]
indices=list(pending_housedata.index)
metrics=market_metrics.drop(indices)
metrics.days_to_pending.fillna(metrics.days_to_sell, inplace=True)
metrics.days_to_sell.fillna(metrics.days_to_pending, inplace=True)


# This block is for calculating the avg price score
avg_price=get_avg_price(metrics)
price=pd.DataFrame(avg_price)
score=list(price["median_sale_price"])
mid=list(price["market_id"])

city=list(market['city'])
mdi=list(market['id'])

maxscore=max(score)
ind=score.index(maxscore)
maxind=mid[ind]
max_score(score,mid,maxscore,maxind)
avg_sales(score,mid,city,mdi)

print(len(metrics))

# This block is for calculating the days of sold
