import streamlit as st
import pandas as pd

st.write('# Mortgage Assistant')

with st.sidebar:

    rate_interest = st.slider(
        'interest rate'.title()
        ,min_value = 0.0
        ,max_value = 20.0
        ,value = 5.0
        ,step = 0.1
        ,format = "%.1f"
        ,key = 'input-rate'
        ,help = 'Selected interest rate'
        )

    down_amount = st.number_input(
        'down payment'.title()
        ,min_value = 0.0
        ,max_value = 100.0
        ,value = 20.0
        ,step = 0.1
        ,format = "%.1f"
        ,key = 'input-down'
        ,help = 'Selected down payment amount'
    )

def calculate_amortization_amount(principal, interest_rate, periods):
    x = (1 + interest_rate) ** periods
    return principal * (interest_rate * x) / (x - 1)

def amortization_schedule(principal, interest_rate, periods):
    amortization_amount = calculate_amortization_amount(principal, interest_rate, periods)
    number = 1
    balance = principal
    table = []
    for period in range(periods):
        interest = balance * interest_rate
        principal = amortization_amount - interest
        balance = balance - principal
        table.append([(period + 1), amortization_amount, interest, principal, balance if balance > 0 else 0])
    return table

st.write(f"{rate_interest:.1f}")
st.write(f"{down_amount:.1f}")