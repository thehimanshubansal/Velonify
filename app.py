import streamlit as st
from streamlit_auth0 import login_button, logout_button, get_access_token

# Auth0 Configuration
AUTH0_DOMAIN = "YOUR_AUTH0_DOMAIN"
AUTH0_CLIENT_ID = "YOUR_AUTH0_CLIENT_ID"
AUTH0_CLIENT_SECRET = "YOUR_AUTH0_CLIENT_SECRET"

st.title("Real-Time Disaster Aggregation Dashboard")

# Login Button
user_info = login_button(AUTH0_CLIENT_ID, AUTH0_DOMAIN)

if user_info:
    st.success(f"Welcome, {user_info['name']}!")
    st.write("You are logged in.")
    logout_button()
else:
    st.warning("Please log in to access the dashboard.")
