import pandas as pd
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt


market=pd.read_csv("E:\Zero-Down Hackathon\Market Hotness\market.csv")
market_metrics=pd.read_csv("E:\Zero-Down Hackathon\Market Hotness\market_metrics.csv")


avg_prices = market_metrics.groupby('market_id')['median_sale_price'].mean()
avg_prices=pd.DataFrame(avg_prices)

market_id=market_metrics.groupby('market_id').count().reset_index()

m_id=market_id['market_id']

avg_prices['m_id']=sorted(m_id)

#print(max(avg_prices['median_sale_price']))


st.line_chart(avg_prices)


#plt.plot(avg_prices['m_id'],avg_prices['median_sale_price'])
#plt.show()

#print(market.head())
#print(market_metrics.head())