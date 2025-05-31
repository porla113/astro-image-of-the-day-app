import requests, os
import streamlit as st
from datetime import date
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
url = "https://api.nasa.gov/planetary/apod?api_key=" + API_KEY

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    date_today = date.today()
    img_title = data["title"]
    img_copyright = data["copyright"]
    img_url = data["url"]
    img_caption = f"{img_title} by {img_copyright}"
    
    st.title(img_title)
    st.write(date_today.strftime("%A, %B %d, %Y"))
    st.image(img_url, caption=img_caption)
    st.write(data["explanation"])
else:
    print("Something is wrong! Status code: " + response.status_code)