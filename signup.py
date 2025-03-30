import streamlit as st
import requests


st.title("Sign Up")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
city=st.text_input("City")
state=st.text_input("State")
country = st.text_input("Country")

if st.button("Sign Up"):
    data = {
        "username": username,
        "email": email,
        "password": password,
        "city": city,
        "state": state,
        "country": country
    }

    response = requests.post("http://localhost:8000/signup", json=data)

    if response.status_code == 200:
        st.success("Registered successfully!")
    else:
        st.error("Error in registration")
