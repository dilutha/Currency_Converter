# Real-Time Currency Converter

## Overview

This Streamlit application allows users to convert currencies in real-time using live exchange rate data. Users can select the currencies they want to convert, input an amount, and view the converted value. The app also provides an optional chart to visualize the exchange rates of various currencies.

## Features

1. **Currency Conversion**:
   - Convert an amount from one currency to another.
   - Select from a variety of popular currencies including USD, EUR, GBP, JPY , AUD and LKR.
   - Real-time exchange rates using an API.

2. **Exchange Rate Visualization**:
   - Display a bar chart of the exchange rates for a selected base currency.
   - View exchange rates for currencies like USD, EUR, GBP, and LKR.

## Installation

Follow these steps to set up and run the application:

### Prerequisites

- Python 3.x
- An API key from [ExchangeRate-API](https://www.exchangerate-api.com/) (replace the default key in the code with your own API key).

### Steps to Run:

1. Clone or download the repository.
2. Create and activate a virtual environment (optional but recommended):
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Use Terminal for following
   
   bash
   python -m venv venv
   source venv/bin/activate  

# On Windows, 
use `venv\Scripts\activate`

3. Install all dependencies 

pip install -r requirements.txt

4. As well you can use Anacando or alternative software (Optional)
5. Use terminal to move to your folder 

 cd < Path to the Folder>

6. Run the Application

 Streamlit run Currency_Converter.py


### Instructions:
- **requirements.txt**: List of dependencies to run the app (Streamlit, Requests, Pandas, and Plotly).
- **README.md**: Provides an overview of the project, installation instructions, and how to use the app.

Make sure to replace the placeholder `API_KEY` in your code with the actual API key you obtain from the [ExchangeRate-API](https://www.exchangerate-api.com/).

Let me know if you need any further adjustments!
