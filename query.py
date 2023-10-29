
import time
import requests
from requests.structures import CaseInsensitiveDict
from geopy.geocoders import OpenCage


latitude = input("enter latitude of the place")
longitude = input("enter longitude of the place")
radius = int(input("enter surrounding radius"))

url = f"https://api.geoapify.com/v2/places?categories=healthcare&filter=circle:{longitude},{latitude},{radius}&apiKey=4373f00847434c0aa84a736ed9317207"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    for i in range(len(data)-1):
     if "features" in data and len(data["features"]) > 0:
        # Extract the name of the first healthcare facility
        healthcare_name = data["features"][i]["properties"]["name"]
        print("Healthcare Name:", healthcare_name)
     else:
        print("No healthcare facilities found in the specified area.")
else:
    print(f"Error: {response.status_code} - Unable to retrieve data.")


