import streamlit as st
import pandas as pd
from datetime import datetime
import time
from GoogleNews import GoogleNews
from opencage.geocoder import OpenCageGeocode
from geopy.exc import GeocoderTimedOut
from geotext import GeoText
import folium
import re
from streamlit_folium import folium_static
import asyncio
import nltk
import spacy
import streamlit as st
from streamlit_auth0 import login_button, logout_button, get_access_token

# Auth0 Configuration
AUTH0_DOMAIN = "https://dev-thqkrqtp84us7xtc.us.auth0.com"
AUTH0_CLIENT_ID = "qF51UPUqRZkrypab9MmeCwVoOR3WJQU1"
AUTH0_CLIENT_SECRET = "8hAtDytaqbWtrO924BMc8OEv7lo7Eu0hsH-DpfAJIi7E69dy03mjcWK5M_JBvCiT"


nltk.download('punkt_tab', download_dir="D:\\CODING\\HackCrux DMS\\dms_env\\lib\\nltk_data\\")
# Fix for "RuntimeError: no running event loop" in Streamlit
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")


# d417b701036946ddb48e34a35c389150
OPENCAGE_API_KEY = "d417b701036946ddb48e34a35c389150"
geocoder = OpenCageGeocode(OPENCAGE_API_KEY)

from nltk.tokenize import word_tokenize
def extract_location(description):
    """Extracts possible city, state, district from news description using GeoText"""
    words = word_tokenize(description)
    locations = GeoText(" ".join(words))  # Extract places
    
    cities = locations.cities  # Extract city names
    countries = locations.countries  # Extract country names

    if cities:
        return cities[0]  # Return first detected city
    elif countries:
        return countries[0]  # If no city, return country
    else:
        return "Unknown"


def extract_location_ner(text):
    doc = nlp(text)
    location_ner_tags = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
    return location_ner_tags
    
def get_lat_lon(location):
    # Fetch latitude and longitude for city, state, or country with improved handling.
    if not location or location.lower() == "unknown":
        return (None, None)  # Return None for missing locations

    try:
        print(f"Fetching coordinates for: {location}")  # Debugging log

        # Try geocoding the full location
        geo_data = geocoder.geocode(location)
        if geo_data:
            return (geo_data[0]['geometry']['lat'], geo_data[0]['geometry']['lng'])

    except Exception as e:
        print(f"Error fetching coordinates for {location}: {e}")
    
    return (None, None)  

# Function to clean URLs
def clean_url(url):
    return re.split(r"[?&]ved=|[?&]usg=", url)[0]  # Remove tracking parameters




def get_ggnews(query,start_date,end_date,location_filter):
    news_list = []

    if location_filter:
        ggnews = GoogleNews(lang="en", region=location_filter[:2], start=start_date, end=end_date)
        ggnews.search(query)
        result = ggnews.results()

        for news in result:
            description = news.get("desc", "No description available")  # Fetch news description
            location = extract_location_ner(description) or "Unknown"  # Assume media source as location if unknown
            # Format URL as a clickable hyperlink
            url_link = f'<a href="{clean_url(news["link"])}" target="_blank">🔗 Read More</a>'


            news_list.append({
                "Title": news["title"],
                "location_ner": location,
                "Source": news["media"],
                "Published At": news["date"],
                "URL": url_link,    
            })
    else:
        ggnews = GoogleNews(lang="en", region="US", start=start_date, end=end_date)
        ggnews.search(query)
        result = ggnews.results()

        for news in result:
            description = news.get("desc", "No description available")  # Fetch news description
            location = extract_location_ner(description) or "Unknown"  # Assume media source as location if unknown
            # Format URL as a clickable hyperlink
            url_link = f'<a href="{clean_url(news["link"])}" target="_blank">🔗 Read More</a>'


            news_list.append({
                "Title": news["title"],
                "location_ner": location,
                "Source": news["media"],
                "Published At": news["date"],
                "URL": url_link,   
            })

    return pd.DataFrame(news_list)
 
# Streamlit UI
st.title("🌍 Disaster News Extractor")

# Login Button
# user_info = login_button(AUTH0_CLIENT_ID, AUTH0_DOMAIN)

# if user_info:
#     st.success(f"Welcome, {user_info['name']}!")
#     st.write("You are logged in.")
#     logout_button()
# else:
#     st.warning("Please log in to access the dashboard.")



st.sidebar.markdown("# FILTERS")
# Date Selection
st.sidebar.markdown("### Select the Time Line")
start_date = st.sidebar.date_input("Select Start Date", value=datetime.today())
end_date = st.sidebar.date_input("Select End Date", value=datetime.today())

# Location Filter Input
st.sidebar.markdown("### Choose Location")
location_filter = st.sidebar.selectbox("Filter by Location (Optional)",placeholder="Enter country or city (e.g., India, California)",options= ["US - United States", "IN - India", "GB - United Kingdom", "CA - Canada", "AU - Australia","DE - Germany", "FR - France", "JP - Japan", "CN - China", "BR - Brazil","IT - Italy", "ES - Spain", "MX - Mexico", "RU - Russia", "ZA - South Africa","KR - South Korea", "NL - Netherlands", "SE - Sweden", "CH - Switzerland", "AE - United Arab Emirates"])

# Disaster Filter Input
st.sidebar.markdown("### Select Disaster Type")
disaster_filter = st.sidebar.multiselect("Filter by Specific Disaster (Optional)",options=['Earthquake', 'Flood', 'Wildfire', 'Tsunami', 'Hurricane', 'Tornado', 'Cyclone', 'Landslide', 'Volcano', 'Storm'],placeholder="Enter disaster name (By default All) ")

# Search Button
if st.button("Fetch Disaster News"):
    with st.spinner(f"Fetching news from {start_date} to {end_date}..."):

        # Define disaster-related keywords
        keywords = ['earthquake', 'flood', 'wildfire', 'tsunami', 'hurricane', 'disaster', 'tornado', 'cyclone', 'landslide', 'volcano', 'storm']
        # keywords = "India"
        all_news = pd.DataFrame()
        
        # Fetch News Articles
        if disaster_filter:
            for disaster in disaster_filter:
                df = get_ggnews(disaster, start_date, end_date, location_filter)
                all_news = pd.concat([all_news,df])
        
        else: 
            for disaster in keywords:
                df = get_ggnews(disaster, start_date, end_date, location_filter)
                all_news = pd.concat([all_news,df])
        


        all_news.dropna(axis=0, inplace=True)
        all_news.drop_duplicates(subset='Title', inplace=True)


        def fun(text):
            country, region, city = '', '', ''
            if len(text) == 1:
                country = text[0]
            elif len(text) == 2:
                country, region = text[0], text[1]
            elif len(text) == 3:
                country, region, city = text[0], text[1], text[2]
            return country, region, city

        a = all_news['location_ner'].apply(fun)

        all_news['Region'] = ''
        all_news['Country'] = ''
        all_news['City'] = ''

        all_news[['Region','Country', 'City']] = pd.DataFrame(a.tolist(), index=all_news.index)

        def create_location(row):
            if row['Region']:
                return row['Region']
            elif row['City']:
                return row['City']
            else:
                return row['Country']

        all_news['Location'] = all_news.apply(create_location, axis=1)
        all_news = all_news.dropna(subset=['Location'])

        all_news = all_news[~all_news['URL'].str.lower().str.contains('politics|yahoo|sports|entertainment|cricket')]

        all_news[['Latitude', 'Longitude']] = all_news['Location'].apply(get_lat_lon).apply(pd.Series)


        if not all_news.empty:
            st.success(f"Found {len(all_news)} disaster-related news articles.")
            map_news = pd.DataFrame()
            map_news = all_news
            all_news = all_news.iloc[:,:-5]
            # st.dataframe(all_news)
            st.markdown(
                """
                <style>
                .styled-table {
                    width: auto;
                    max-height: 500px;
                    overflow-y: auto;
                    display: block;
                }
                .styled-table table {
                    width: auto;
                    border-collapse: collapse;
                }
                .styled-table th, .styled-table td {
                    padding: 8px 12px;
                    border: 1px solid #ddd;
                    text-align: left;
                }
                .styled-table th {
                    background-color: #f4f4f4;
                    font-weight: bold;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.markdown(all_news.to_html(escape=False, index=False), unsafe_allow_html=True)

            # Provide CSV Download Option
            csv = all_news.to_csv(index=False).encode('utf-8')
            st.download_button(label="📥 Download CSV", data=csv, file_name="disaster_news.csv", mime="text/csv")

            # Create Map Visualization
            st.subheader("🌍 Disaster Map Visualization")
            map_center = [20, 0]  # Center map around equator
            disaster_map = folium.Map(location=map_center, zoom_start=2,max_bounds=True,max_zoom=8,min_zoom=2)

            for _, row in map_news.iterrows():
                if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):
                    folium.Marker(
                        location=[row["Latitude"], row["Longitude"]],
                        popup=f"{row['Title']} - {row['Source']}",
                        icon=folium.Icon(color="red", icon="warning-sign")
                    ).add_to(disaster_map)

            folium_static(disaster_map)  # Display the map
            

        else:
            st.warning("No relevant disaster news found.")
           
