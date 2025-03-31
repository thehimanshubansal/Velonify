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
import spacy
import streamlit as st
from db import disaster_collection
from pymongo import MongoClient
import alert,os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fix for "RuntimeError: no running event loop" in Streamlit
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# OPENCAGE API Connection
OPENCAGE_API = os.getenv("OPENCAGE_API")

OPENCAGE_API_KEY = OPENCAGE_API
geocoder = OpenCageGeocode(OPENCAGE_API_KEY)


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




def get_ggnews(query,start_date,end_date):
    news_list = []

    ggnews = GoogleNews(lang="en", region="US", start=start_date, end=end_date)
    ggnews.search(query)
    result = ggnews.results()

    for news in result:
        location = extract_location_ner(news["title"]) or "Unknown"  # Assume media source as location if unknown
        if location == "Unknown":
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

def main(): 
    # Streamlit UI
    st.header("Disaster News Extractor")

    st.sidebar.markdown("# FILTERS")
    # Date Selection
    st.sidebar.markdown("### Select the Time Line")
    start_date = st.sidebar.date_input("Select Start Date", value=datetime.today())
    end_date = st.sidebar.date_input("Select End Date", value=datetime.today())

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
                    df = get_ggnews(disaster, start_date, end_date)
                    all_news = pd.concat([all_news,df])
            
            else: 
                for disaster in keywords:
                    df = get_ggnews(disaster, start_date, end_date)
                    all_news = pd.concat([all_news,df])
            


            all_news.dropna(axis=0, inplace=True)
            all_news.drop_duplicates(subset='Title', inplace=True)


            def fun(text):
                region, country, city = '', '', ''
                if len(text) == 1:
                    region = text[0]
                elif len(text) == 2:
                    region, country = text[0], text[1]
                elif len(text) == 3:
                    region, country, city = text[0], text[1], text[2]
                return region, country, city

            all_news = all_news[all_news['location_ner'] != 'Unknown']
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

            all_news = all_news.drop_duplicates(subset='Region')

            all_news = all_news.drop('location_ner',axis=1)

            if not all_news.empty:
                st.success(f"Found {len(all_news)} disaster-related news articles.")
                map_news = pd.DataFrame()
                map_news = all_news
                all_news = all_news.iloc[:,:-5]

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
                        text-align: left !important;
                    }
                    .styled-table th {
                        background-color: #f4f4f4;
                        font-weight: bold;
                        text-align: left !important;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(all_news.to_html(escape=False, index=False), unsafe_allow_html=True)

                # Provide CSV Download Option
                csv = all_news.to_csv(index=False).encode('utf-8')
                st.download_button(label="📥 Download CSV", data=csv, file_name="disaster_news.csv", mime="text/csv")
                # csv_file"  # Change to your actual CSV file path
                df = all_news

                # Convert DataFrame to dictionary for MongoDB insertion
                records = df.to_dict(orient="records")
                # Check for duplicates and insert only new records
                for record in records:
                    # Define criteria to check for duplicacy (e.g., title and published time)
                    duplicate1 = disaster_collection.find_one({"title": record["Title"], "published": record["Published At"]})
                    if not duplicate1:
                        disaster_collection.insert_one(record)
                        print(f"Inserted: {record['Title']}")
                    else:
                        print(f"Duplicate found, skipping: {record['Title']}")
                print("CSV Data Inserted Successfully, excluding duplicates.")

                # Alert Mechanism
                os.system('streamlit run alert.py')
               
            else:
                st.warning("No relevant disaster news found.")
