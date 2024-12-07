# Streamlit app layout
st.title("Real-Time Currency Converter with Exchange Rates Visualization")

# Select currencies
from_currency = st.selectbox("Select Base Currency", options=['USD', 'EUR', 'GBP', 'LKR', 'JPY', 'AUD'])
to_currency = st.selectbox("Select Target Currency", options=['USD', 'EUR', 'GBP', 'LKR', 'JPY', 'AUD'])
amount = st.number_input("Amount", min_value=0.0, format="%.2f")

# Convert currency
if st.button("Convert"):
    result = convert_currency(amount, from_currency, to_currency)
    if result is not None:
        st.success(f"💰{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        st.error("Error occurred in conversion rates")
