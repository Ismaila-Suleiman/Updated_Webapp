import streamlit as st

from PIL import Image

with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')

img = Image.open("puppy.jpg")

st.sidebar.image(img.resize((250,250)))

st.checkbox("Agree")

st.title("My First WebApp")

st.subheader("You are welcome to Wellness.com where all your health concerns are addressed")

st.selectbox("Gender", ['Male', 'Female', 'Others'])

w = st.sidebar.number_input("How much do you weigh")

h = st.sidebar.number_input("How tall are you in metres")

def bmi_calc(w,h):
    bmi = round(w/(h**2),1)
    return bmi

if st.sidebar.button("Calculate"):
    st.balloons()
    st.sidebar.write(bmi_calc(w,h))

a1, a2 = st.columns(2)

with a1:
    st.checkbox("Accept")
    st.number_input("How long has Wellness being in existence", step=1)
    st.text_input("What is your name?")

with a2:
    st.checkbox("Reject")
    st.text_area("Your current address")
    st.date_input("Date of last Visit")