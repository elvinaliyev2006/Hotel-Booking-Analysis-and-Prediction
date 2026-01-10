import streamlit as st
import joblib
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

model = joblib.load('hotel_model.pkl')
encoder = joblib.load('encoder.pkl')
@st.cache_data
<<<<<<< HEAD
def get_data():

=======
def get_data_from_csv():
>>>>>>> 049007ecee5cd4339bc76180abd605aa198ea682
    df = pd.read_csv('datasets/clean_hotel_data.csv')

    for col in ['market_segment', 'country', 'agent']:
        counts = df[col].value_counts()
        small_cats = counts[counts < 1000].index
        df[col] = df[col].replace(small_cats, 'Other')
    
    return df
<<<<<<< HEAD
df=get_data()
=======

df = get_data_from_csv()
>>>>>>> 049007ecee5cd4339bc76180abd605aa198ea682

st.title("🏨 Hotel Booking Predictor")
st.write("*Please Enter Features:*")
country_list=df['country'].unique()
agent_list=df['agent'].unique()
customer_list=df['customer_type'].unique()
market_segment_list=df['market_segment'].unique()

col1 , col2 = st.columns(2)

with col1:
    co=st.selectbox('Select country:',country_list)
    ag=st.selectbox('Select agent:',agent_list)
    cus=st.selectbox('Select customer type:',customer_list)
    mark=st.selectbox('Select market segment:',market_segment_list)

with col2:
    spe=st.number_input('Enter number of special requests:',min_value=0)
    adr=st.number_input('Enter adr:',min_value=0)
    lead_t=st.number_input('Enter lead time:',min_value=0)
    tot_st=st.number_input('Enter total stays:',min_value=0)
    p_c=st.number_input('Enter previous cancellations:',min_value=0)
    parking_s=st.number_input('Enter required car parking spaces:',min_value=0)
if st.button('Predict Booking Status'):
    input_data = pd.DataFrame({
        'country': [co],
        'lead_time': [lead_t],
        'total_of_special_requests': [spe],
        'previous_cancellations': [p_c],
        'adr': [adr],
        'customer_type': [cus],
        'required_car_parking_spaces': [parking_s],
        'market_segment': [mark],
        'total_stays': [tot_st],
        'agent': [ag]
    })
    cat_cols2 = ['agent', 'country', 'market_segment', 'customer_type']
    encoded_array = encoder.transform(input_data[cat_cols2])
    encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(cat_cols2))

    num_df = input_data.drop(columns=cat_cols2)
    final_df = pd.concat([encoded_df, num_df], axis=1)

    prediction = model.predict(final_df)
    

    if prediction[0] == 1:
        st.error("🚨 **Prediction:** This booking is likely to be **CANCELED**.")
    else:
        st.success("✅ **Prediction:** This booking is likely to be **CONFIRMED**.")
