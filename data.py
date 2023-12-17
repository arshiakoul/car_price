import streamlit as st
import pandas as pd
import numpy as np

def app(car_df):
    st.header("View Data")
    with st.beta_expander("View Dataset"):
        st.table(car_df)
