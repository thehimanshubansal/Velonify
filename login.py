import streamlit as st
import requests
import os

def main():
    # ✅ Streamlit UI
    st.title("Login")

    email = st.text_input("Email").strip().lower()   # Strip and lowercase email
    password = st.text_input("Password", type="password").strip()

    # ✅ Backend URL (Update if deployed)
    BACKEND_URL = "http://localhost:8000/login"

    # ✅ LOGIN FUNCTION
    if st.button("Login"):
        if not email or not password:
            st.error("Please enter both email and password.")
        else:
            # Send request to FastAPI backend
            response = requests.post(
                BACKEND_URL,
                params={"email": email, "password": password}  # Use params not json
            )

            if response.status_code == 200:
                st.success("Logged in successfully!")
            else:
                st.error("Invalid email or password")
    # import signup
    # st.markdown("Don't have an account yet? [Sign Up](./signup.py)", unsafe_allow_html=True)
    if st.button("Sign Up"):
        os.system("streamlit run signup.py")