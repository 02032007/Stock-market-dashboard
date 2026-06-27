import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.title("📈 Stock Market Dashboard")

# Stock input
ticker = st.text_input("Enter Stock Symbol", "AAPL")

# Fetch stock data
stock = yf.Ticker(ticker)
current_price = stock.history(period="1d")["Close"].iloc[-1]
st.write(f"Current Price of {ticker}: ${current_price:.2f}")

# Portfolio tracking inputs
shares = st.number_input("Number of Shares", min_value=0, value=10)
buy_price = st.number_input("Purchase Price ($)", min_value=0.0, value=250.0)

# Portfolio calculations
investment_cost = shares * buy_price
current_value = shares * current_price
profit_loss = current_value - investment_cost

st.write(f"Investment Cost: ${investment_cost:.2f}")
st.write(f"Current Value: ${current_value:.2f}")
st.write(f"Profit/Loss: ${profit_loss:.2f}")

# Stock price history chart
hist = stock.history(period="6mo")
fig = go.Figure()
fig.add_trace(go.Scatter(x=hist.index, y=hist["Close"], mode="lines", name="Price"))
fig.update_layout(title=f"{ticker} Stock Price History", xaxis_title="Date", yaxis_title="Price ($)")
st.plotly_chart(fig)

# Portfolio summary table
data = {
    "Metric": ["Investment Cost", "Current Value", "Profit/Loss"],
    "Amount ($)": [investment_cost, current_value, profit_loss]
}
df = pd.DataFrame(data)
st.table(df)
