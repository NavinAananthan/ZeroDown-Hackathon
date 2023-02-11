import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np


def get_avg_price(market_metrics):

    avg_prices = market_metrics.groupby('market_id',as_index=False)['median_sale_price'].mean()
    return avg_prices


def getmaxscore(price,score):
    for index,row in price.iterrows():
        if(row['median_sale_price']==score):
            print(row['median_sale_price'],row['market_id'])
            break




def getscore(id,price):
    for index,row in price.iterrows():
        if(row['market_id']==id):
            score=row['median_sale_price']
            break

    return score



def display_avg_price(score,mid,maxscore,maxid):
    st.text("Graph for the Avg sales price and their corresponding market_id")
    st.line_chart(pd.DataFrame(score,mid))
    st.text(f"The max sales {maxscore} has been done by the market id {maxid}")
    st.write("")
    st.write("")
    st.write("")



def avg_sales(score,mid):

    st.text("The below score is based on Average of the Sales after buying it")
    try:
        market_id=st.number_input('Enter the Market ID to get the score')
        ind=mid.index(int(market_id))
        st.text(f"The score is: {score[ind]}")
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

score=list(price["median_sale_price"])
mid=list(price["market_id"])


maxscore=max(score)
ind=score.index(maxscore)
maxind=mid[ind]

display_avg_price(score,mid,maxscore,maxind)
avg_sales(score,mid)

metrics.to_csv('metric.csv')
