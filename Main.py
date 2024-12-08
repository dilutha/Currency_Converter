# -*- coding: utf-8 -*-
"""Currency_new.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KQC2D4OAQ1Zr_9qpbX4YQ01H8T6Tpy9n
"""

pip install streamlit pandas plotly requests

import streamlit as st
import requests
import pandas as pd
import plotly.express as px
API_KEY = '6ab4dd50f1659904149c169e'  # Use your provided API key
BASE_URL = 'https://v6.exchangerate-api.com/v6/{}/'

# Function to get exchange rates for a base currency
def get_exchange_rates(base_currency):
    url = BASE_URL.format(API_KEY) + 'latest/' + base_currency
    response = requests.get(url)
    data = response.json()

    if 'conversion_rates' in data:
        return data['conversion_rates']
    else:
        error_message = data.get('error-type', 'Unexpected error occurred')
        st.error(f"Error fetching conversion rates: {error_message}")
        return {}

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)
    if to_currency in rates:
        return amount * rates[to_currency]
    else:
        return None

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

st.header("📈 Exchange Rate Difference (Relative to Target Currency)")

# Show exchange rate chart button
if st.button("Show Exchange Rate Chart"):
    # Get exchange rates for the selected base currency
    rates = get_exchange_rates(from_currency)

    if rates:
        # Prepare data for the chart (exclude the selected target currency from the comparison)
        exchange_rates = []
        for currency, rate in rates.items():
            if currency != to_currency:
                # If target currency is LKR, calculate the exchange rate as LKR = 1
                if to_currency == 'LKR':
                    rate_to_lkr = 1 / rate
                    exchange_rates.append({'Currency': currency, 'Exchange Rate (LKR = 1)': rate_to_lkr})
                else:
                    exchange_rates.append({'Currency': currency, 'Exchange Rate': rate})

        # Create a DataFrame
        rates_df = pd.DataFrame(exchange_rates)

        if not rates_df.empty:
            # Plot the exchange rates as a bar chart using Plotly
            if to_currency == 'LKR':
                fig = px.bar(rates_df,
                             x='Currency',
                             y='Exchange Rate (LKR = 1)',
                             title=f'Exchange Rates of Currencies Relative to 1 LKR',
                             labels={"Exchange Rate (LKR = 1)": "Exchange Rate (LKR = 1)", "Currency": "Currency"},
                             color='Currency',
                             color_discrete_sequence=px.colors.qualitative.Set1)
            else:
                fig = px.bar(rates_df,
                             x='Currency',
                             y='Exchange Rate',
                             title=f'Exchange Rates Relative to {to_currency}',
                             labels={"Exchange Rate": f"Exchange Rate ({to_currency})", "Currency": "Currency"},
                             color='Currency',
                             color_discrete_sequence=px.colors.qualitative.Set1)

            # Show the plot in the Streamlit app
            st.plotly_chart(fig)
        else:
            st.error(f"No data available for exchange rates relative to {to_currency}")
    else:
        st.error("Unable to fetch exchange rates.")

# Footer
st.caption("Powered by ExchangeRate-API | Built with 💻 Streamlit")
