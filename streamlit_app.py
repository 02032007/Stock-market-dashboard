import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.title("📈 Multi‑Stock Portfolio Dashboard")

# User enters multiple stock symbols separated by commas
symbols = st.text_input("Enter Stock Symbols (comma separated)", "AAPL,MSFT,GOOGL")
symbols = [s.strip().upper() for s in symbols.split(",") if s.strip()]

portfolio_data = []

# Multi-stock chart setup
fig = go.Figure()

for ticker in symbols:
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")["Close"].iloc[-1]

    st.subheader(f"{ticker} — Current Price: ${current_price:.2f}")

    # Portfolio tracking inputs for each stock
    shares = st.number_input(f"Number of Shares for {ticker}", min_value=0, value=0, key=f"shares_{ticker}")
    buy_price = st.number_input(f"Purchase Price ($) for {ticker}", min_value=0.0, value=0.0, key=f"buy_{ticker}")

    investment_cost = shares * buy_price
    current_value = shares * current_price
    profit_loss = current_value - investment_cost

    st.write(f"Investment Cost: ${investment_cost:.2f}")
    st.write(f"Current Value: ${current_value:.2f}")
    st.write(f"Profit/Loss: ${profit_loss:.2f}")

    portfolio_data.append({
        "Symbol": ticker,
        "Shares": shares,
        "Buy Price": buy_price,
        "Investment Cost ($)": investment_cost,
        "Current Value ($)": current_value,
        "Profit/Loss ($)": profit_loss
    })

    # Add each stock's history to the chart
    hist = stock.history(period="6mo")
    fig.add_trace(go.Scatter(x=hist.index, y=hist["Close"], mode="lines", name=ticker))

# Show portfolio summary table
if portfolio_data:
    df = pd.DataFrame(portfolio_data)
    st.subheader("📊 Portfolio Summary")
    st.table(df)

# Show combined chart
if symbols:
    fig.update_layout(title="Multi‑Stock Price History", xaxis_title="Date", yaxis_title="Price ($)")
    st.plotly_chart(fig)

