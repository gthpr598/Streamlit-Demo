import streamlit as st
import yfinance as yf
import datetime

st.title("Welcome to StockViz")

ticker_symbol = st.text_input("Enter the stock Name", value = "AAPL")

ticker_data = yf.Ticker(ticker_symbol)

##Getting input from user for start and end date
dt1, dt2 = st.columns(2)
with dt1:
    start = st.date_input("Start Date: ", datetime.date(2019,6,8))

with dt2:
    end = st.date_input("End Date: ", datetime.date(2020,3,5))

##Loading Start and End date from input
hist = ticker_data.history(period="1mn", start=start, end=end)

##Creating table of Data
st.dataframe(hist,use_container_width=True)

##Graphical Representation of Data
col1, col2 = st.columns(2)

with col1:
    st.write("""
    Daily Opening Price Chart
    """)
    st.line_chart(hist, y="Open")

with col2:
    st.write("""
    Daily Closing Price Chart
    """)
    st.line_chart(hist, y="Close")


st.write("""
    Daily Volume Chart
    """)
st.line_chart(hist, y="Volume")
