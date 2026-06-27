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
