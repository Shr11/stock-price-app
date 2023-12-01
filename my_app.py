import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         # Stock Price
         
         shown are the stock **closing price** and ***volume*** of google!
         
         """)


# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiyqezmxO6CAxXJUt4KHcCYA9oQFnoECAsQAQ&url=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-get-stock-data-using-python-c0de1df17e75&usg=AOvVaw1F0uXShgGWsRfikLM6t6I3&opi=89978449

#define the ticker symbol
tickerSymbol = "GOOGL"


#get data on this ticker symbol
tickerData = yf.Ticker(tickerSymbol)


#get historical prices for this ticker symbol
tickerDf = tickerData.history(period='1d', start= '2010-5-10', end= '2023-11-10')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

