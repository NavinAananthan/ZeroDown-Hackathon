import pandas as pd
import streamlit as st


def get_avg_price(market,market_metrics,market_id):
    avg_prices = market_metrics.groupby('market_id')['median_sale_price'].mean()
    avg_prices=pd.DataFrame(avg_prices)
    m_id=market_id['market_id']
    avg_prices['m_id']=sorted(m_id)

    st.write("Visualization of Average Prices with respect to their Market id")
    st.line_chart(avg_prices)
    st.write("\n We can interpret that from the above given")



market=pd.read_csv("E:\Zero-Down Hackathon\Market Hotness\market.csv")
market_metrics=pd.read_csv("E:\Zero-Down Hackathon\Market Hotness\market_metrics.csv")
market_id=market_metrics.groupby('market_id').count().reset_index()

get_avg_price(market,market_metrics,market_id)


