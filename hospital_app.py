import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# title in html
st.set_page_config(page_title = "Smart Hospital Patient Navigator", page_icon = "🏥",layout = "wide")

st.markdown("""
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html,body, [class"="css"] {font-family: 'Inter', sans-serif}

    #Main Menu {visibility: hidden;}
    header[data-testid="stHeader"]{display:none;}
    .stDeployButton {display:none;}
    footer { visibility: hidden;}
    .block-container {padding-top: 0 !important; padding-bottom: 2rem !important; max-width:1100px !important;}
    div[data-testid="stForm"] {border:none; padding:0}
    
    
  </style>
""", unsafe_allow_html=True)

st.title("Hello")


                   
