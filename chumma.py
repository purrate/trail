import os
import shutil
from webbrowser import get
import requests
import geocoder
import json

def getNews():
    current_location = geocoder.ip('me')
    latitude = current_location.latlng[0]
    longitude = current_location.latlng[1]
    radius = 400

    api_key = "b2810dea161648c39b9992907e6b20ee"

    # Modify the URL to include the location parameters
    url = f"https://newsapi.org/v2/top-headlines?country=in&lat={latitude}&lon={longitude}&radius={radius}&apikey={api_key}"

    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []

    with open('news.jsonl', 'w') as f:
        for article in articles:
            # Write each article as a JSON object with a "doc" field in the JSONL file
            f.write(json.dumps({"doc": article["title"]}) + '\n')

    # Define the source and destination paths
    source_path = 'news.jsonl'
    destination_path = 'examples/data/pathway-docs/news.jsonl'

    # Move the file to the destination directory
    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"'news.jsonl' has been moved to 'examples/data/pathway-docs'.")

getNews()
