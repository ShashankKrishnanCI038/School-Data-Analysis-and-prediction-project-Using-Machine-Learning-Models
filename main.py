import streamlit as st
import time
import sklearn
import tensorflow
import joblib #to save trained model in low size.

st.set_page_config(
    page_title="School Data Analysis using Machine Learning Models",
    page_icon="🏫"
)

# Set the background image
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image URL or local path
set_background("https://wallpaper-house.com/data/out/12/wallpaper2you_519097.png")


st.title('School Data Analysis using Machine Learning Models')

try:
    proid = st.number_input(label='Enter a Province ID', value=10000, min_value=10000, max_value=350000)

    cityid = st.number_input(label='Enter a City ID', value=10000, min_value=10000, max_value=350000)

    districtid = st.number_input(label='Enter a District ID', value=10000, min_value=10000, max_value=350000)

    schoolid = st.slider(
    label="Enter a School ID",
    min_value=10000000,
    max_value=80000000,
    value=10000000,
    step=1 )

    file = st.file_uploader("Choose Trained ML Model", type=['pkl']) # choose and upload the trained model file .pkl

    if file is not None:
        if st.button('Predict'):

            model = joblib.load(file)
            with st.spinner("Please wait for result"):
                time.sleep(3)

            sample = [[float(proid), float(cityid), float(districtid), float(schoolid)]]
            prediction  = model.predict(sample)

            if prediction[0] == 'N':
                st.write("the School is Public")
            elif prediction[0] == 'S':
                st.write("The schools is private")
            else:
                st.write("There is Some error.....Please try again later")

except AttributeError as se:
    pass
