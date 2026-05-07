import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

import os
base_path = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(base_path, 'df.csv'))
model = pkl.load(open(os.path.join(base_path, 'model.pkl'),'rb'))

st.header('Churn Prediction')
st.write('Telecom Service')
# SeniorCitizen','Partner','Dependents','tenure','PhoneService','InternetService','Contract','PaymentMethod','MonthlyCharges','TotalCharges'

col1, col2 = st.columns(2)
with col1:
    SeniorCitizen=st.selectbox('SeniorCitizen',['Yes','No'])
    Partner=st.selectbox('Partner of telecom company',df['Partner'].unique())
    Dependents=st.selectbox('Dependency',df['Dependents'].unique())
    tenure=st.number_input('Tenure length',min_value=0,max_value=100,step=1)
    PhoneService=st.selectbox('Phone-service',df['PhoneService'].unique())
with col2:
    InternetService=st.selectbox('Type of Internet service',df['InternetService'].unique())
    Contract=st.selectbox('Type of Contract',df['Contract'].unique())
    PaymentMethod=st.selectbox('Type of PaymentMethod',df['PaymentMethod'].unique())
    MonthlyCharges=st.text_input('Monthly charges')
    TotalCharges=st.text_input('Total charges')

if st.button('Predict'):
    if(SeniorCitizen=='Yes'):
        SeniorCitizen = 1
    else:
        SeniorCitizen = 0
    prediction = model.predict(pd.DataFrame([[SeniorCitizen,Partner,Dependents,tenure,PhoneService,InternetService,Contract,PaymentMethod,MonthlyCharges,TotalCharges]],columns=['SeniorCitizen','Partner','Dependents','tenure','PhoneService','InternetService','Contract','PaymentMethod','MonthlyCharges','TotalCharges']))[0]
    if prediction== 0 :

        st.markdown("<h1 style='color:red;'>Person is no longer with telecom service</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='color:green;'>Person is still enjoying with telecom service</h1>", unsafe_allow_html=True)
