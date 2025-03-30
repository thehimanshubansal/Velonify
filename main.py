import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")

import streamlit as st

# Define internal CSS
css_code = """
<style>
/* Style for Volentify title */
.title {
    text-align: center;
    font-size: 2em;
    font-weight: bold;
    background: linear-gradient(90deg, #4ADE80, #60A5FA, #F472B6, #FBBF24);
    background-size: 200% 200%;
    color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
    animation: gradientFlow 3s ease infinite;
}

/* Animation to make gradient flow */
@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>
"""

# Inject the CSS
st.markdown(css_code, unsafe_allow_html=True)

# Wrap st.title with a div to apply custom CSS
st.markdown('<div class="title" style="font-size: 4em">VOLENTIFY</div>', unsafe_allow_html=True)
st.markdown('<div class="title" style="padding-bottom: 10px">Real-Time Insights. Smarter Response. Safer World</div>', unsafe_allow_html=True)

# # Display Volentify title using st.title
# st.title("VOLENTIFY 🌍")

# # Close the div container
# st.markdown('</h1>', unsafe_allow_html=True)
# # Set up the navigation menu
selected = option_menu(
    menu_title="", 
    options=["Home","Insight", "About","Precaution","Login"],
    icons=["house","bell", "globe", "info","7-circle","key"],
    orientation="horizontal"
)


if selected == "Login":
    # Run the login.py script
    import login
    login.main()
    
if selected == "Signup":
    # Run the login.py script
    import signup
    signup.main()

elif selected == "About":
    # Run the about.py script
    import about
    about.main()
    

elif selected == "Home":
    # Run the home.py script
    import ggnews_dms4
    ggnews_dms4.main()
    
# elif selected == "Insight":
#     # Run the home.py script
#     import insight
#     insight.main()
    
elif selected == "Precaution":
    # Run the precausion.py script
    import precaution
    precaution.main()


# Footer HTML with Unicode social icons and proper formatting
footer_html = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    display: flex;
    padding: 12px;
    font-size: 14px;
    font-family: Arial, sans-serif;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.3);
    background-color: black;
}
b{
    text-align: left;
}
.x {
    margin-left: auto;
    margin-right: 0;
    color: white;
    text-align: right;
    font-weight: bold;
}
.x:hover {
    color: #ff8c00;
    text-decoration: underline;
}
</style>

<div class="footer">
    🌍 <b> Made with 💗 By Team Euphoria</b> | Stay Alert, Stay Safe! 🚀 <br>
    <div class="x">
    <a href="https://github.com/" target="_blank">💻 GitHub</a> |
    <a href="mailto:gyanthegreat05@gmail.com" target="_blank">📩 Contact Us</a> |
    <a href="https://www.linkedin.com/" target="_blank">👥 LinkedIn</a>
    </div>
</div>
"""

# Render the footer
st.markdown(footer_html, unsafe_allow_html=True)