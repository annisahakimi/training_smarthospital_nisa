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
    div.stButton > button:hover { background: linear-gradient(135deg, #1e429f, #1a56db) !important; }
    div[data-testid="stCheckbox"] label {
    font-size: 14px !important; font-weight: 500 !important; color: #374151 !important;
    }
  }
  
  </style>
""", unsafe_allow_html=True)

@st.cache_resource #to ensure model load once only when the program is run
def load_model():
  #rb = read binary. file pkl dalam 1.0 so nanti use rb to convert from binary
  with open('hospital_model.pkl', 'rb') as f:
    return pickle.load(f)

bundle        = load_model()
model         = bundle['model']
scaler        = bundle['scaler']
features      = bundle['features']
cols_to_scale = bundle['cols_to_scale']
dept_map_inv  = bundle['dept_map_inv']
gender_map    = bundle['gender_map']
temp_map      = bundle['temp_map']
hr_map        = bundle['hr_map']
dur_map       = bundle['dur_map']
cc_map        = bundle['cc_map']

DEPT_INFO =  {
  'Respiratory Medicine':{
      'icon':'🫁','color':'#0284c7','bg':'#e0f2fe','border':'#7dd3fc',
      'desc':'Specialises in conditions affecting the lungs and airways.',
      'next':['Visit Level 2, Wing B','Estimated wait: 15–25 min','Please wear a mask']
    },
  'Cardiology': {
        'icon':'❤️','color':'#dc2626','bg':'#fee2e2','border':'#fca5a5',
        'desc':'Specialises in heart and cardiovascular conditions.',
        'next':['Visit Level 3, Wing A','Estimated wait: 20–30 min','Bring any previous ECG reports']
    },
    'Gastroenterology': {
        'icon':'🫃','color':'#d97706','bg':'#fef3c7','border':'#fcd34d',
        'desc':'Specialises in digestive system and abdominal conditions.',
        'next':['Visit Level 1, Wing C','Estimated wait: 10–20 min','Avoid eating before consultation']
    },
    'Neurology': {
        'icon':'🧠','color':'#7c3aed','bg':'#ede9fe','border':'#c4b5fd',
        'desc':'Specialises in brain, spine, and nervous system conditions.',
        'next':['Visit Level 4, Wing A','Estimated wait: 25–35 min','Bring list of current medications']
    },
    'General Medicine': {
        'icon':'🩺','color':'#059669','bg':'#d1fae5','border':'#6ee7b7',
        'desc':'Handles general health concerns and non-specialist conditions.',
        'next':['Visit Level 1, Wing A','Estimated wait: 10–15 min','Registration desk is open 24/7']
    },
    'Dermatology': {
        'icon':'🔬','color':'#b45309','bg':'#fef9c3','border':'#fde68a',
        'desc':'Specialises in skin, hair, and nail conditions.',
        'next':['Visit Level 2, Wing D','Estimated wait: 15–20 min','Bring photos of affected area if possible']
    },
  }

#Hero header
#1 rem  = 16 pxl
st.markdown("""
<div style="background:linear-gradient(135deg,#1e3a8a 0%,#1a56db 60%,#0ea5e9 100%);
            padding:3rem 2rem 2.5rem;margin:-1rem -1rem 2rem;text-align:center;">
    <div style="font-size:14px;font-weight:500;color:rgba(255,255,255,0.7);
                text-transform:uppercase;letter-spacing:0.1em;margin-bottom:12px;">
        🏥 Future Classroom · Machine Learning
    </div>
    <div style="font-size:36px;font-weight:700;color:#ffffff;margin-bottom:12px;
                letter-spacing:-0.02em;">
        Smart Hospital Patient Navigator
    </div>
    <div style="font-size:18px;color:rgba(255,255,255,0.85);font-weight:400;">
        Find the Right Department for Your Symptoms
    </div>
</div>
""",unsafe_allow_html=True)
}





                   
