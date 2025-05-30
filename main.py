import requests, os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.nasa.gov/planetary/apod?api_key=" + API_KEY
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data["title"])
    print(data["date"])