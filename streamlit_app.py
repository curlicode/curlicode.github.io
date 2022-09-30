import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

with st.sidebar:

    rate_interest = st.number_input(
        'interest rate'.title()
        ,min_value = 0.0
        ,max_value = 20.0
        ,value = 5.0
        ,step = 0.1
        ,format = "%f"
        ,key = 'input-rate'
        ,help = 'Selected interest rate'
        )

    down_amount = st.number_input(
        'down payment'.title()
        ,min_value = 0.0
        ,max_value = 100.0
        ,value = 20.0
        ,step = 0.1
        ,format = "%f"
        ,key = 'input-down'
        ,help = 'Selected down payment amount'
    )