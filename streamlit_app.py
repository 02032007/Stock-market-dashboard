import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("📈 Stock Market Dashboard")

ticker = st.text_input("Enter Stock Symbol", "AAPL")

stock = yf.Ticker(ticker)

period = st.selectbox(
    "Select Time Period",
    ["1mo", "3mo", "6mo", "1y", "5y"]
)

history = stock.history(period=period)

info = stock.info

st.subheader(info["longName"])
st.metric("Current Price", f"${info['currentPrice']}")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=history.index,
        y=history["Close"],
        mode="lines",
        name="Close Price"
    )
)

fig.update_layout(
    title="Stock Price History",
    xaxis_title="Date",
    yaxis_title="Price ($)"
)

st.plotly_chart(fig, use_container_width=True)
