import streamlit as st
from PIL import Image

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

st.header("Get in Touch")

st.sidebar.header("Project Programmer")
profile = Image.open(r"C:\Users\SHASHANK K\PycharmProjects\Project Files\School Data Analysis\Shashank K.jpg")
st.sidebar.image(profile, caption="Shashank Krishnan, AIML Engineer")

st.write("""
 **School Data Analysis Using Machine Learning Models** is a WebApp that is Developed by Shashank K, AIML Engineering graduate from Don Bosco Institute of Technology, Kumbalagodu.

 For Any Queries ragarding trained CNN Model:
    * Please do mail to shashank2002.shashu@gmail.com 
    * Ping me on +91 7829493269

""")