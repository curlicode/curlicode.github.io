import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")


rate_interest = st.number_input(
    'interest rate'.title()
    ,min_value = 0
    ,max_value = 20
    ,value = 5.0
    ,step = 0.1
    ,format = '%.1f%'
    ,key = 'input-rate'
    ,help = 'Selected interest rate'
)

down_amount = st.number_input(
    'down payment'.title()
    ,min_value = 0
    ,max_value = 100
    ,value = 20.0
    ,step = 0.1
    ,format = '%.1f%'
    ,key = 'input-down'
    ,help = 'Selected down payment amount'
)