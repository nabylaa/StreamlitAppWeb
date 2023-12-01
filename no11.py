import pickle
import streamlit as st
import pandas as pd
import numpy as np

@st.cache(suppress_st_warning=True)
def get_value(val, my_dict):    
    for key, value in my_dict.items():        
        if val == key:            
            return value
        
# Load model
model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))
app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Prediction'])  # two pages
if app_mode == 'Home':    
    # Title
    st.markdown("<h1 style='text-align: center;'>Prediksi Harga Mobil</h1><br>", unsafe_allow_html=True)

    # Image
    st.image('car.jpg')

    # Header for Dataset
    st.header("Dataset")

    # Read CSV
    df1 = pd.read_csv('CarPrice.csv')

    # Display DataFrame
    st.dataframe(df1)

    # Chart for Highway-mpg
    st.write("Grafik Highway-mpg")
    chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
    st.line_chart(chart_highwaympg)

    # Chart for curbweight
    st.write("Grafik curbweight")
    chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
    st.line_chart(chart_curbweight)

    # Chart for horsepower
    st.write("Grafik horsepower")
    chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
    st.line_chart(chart_horsepower)


elif app_mode == 'Prediction':    
    st.image('car2.jpg')    

    # Input features
    highwaympg = st.number_input('Highway-mpg', 0, 10000000)
    curbweight = st.number_input('Curbweight', 0, 10000000)
    horsepower = st.number_input('Horsepower', 0, 10000000)

    # Prediction button
    if st.button('Prediksi'):
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])
        # Format and display the prediction
        harga_mobil_str = np.array(car_prediction)
        harga_mobil_float = float(harga_mobil_str[0])
        harga_mobil_formatted = "{:,.2f}".format(harga_mobil_float)
        st.markdown(f'Harga Mobil: $ {harga_mobil_formatted}')
