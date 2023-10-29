import requests
from requests.structures import CaseInsensitiveDict
import geocoder

# Get the current location's latitude and longitude
current_location = geocoder.ip('me')
latitude = current_location.latlng[0]
longitude = current_location.latlng[1]
radius = 400

# Construct the URL with the correct format
url = f"https://api.geoapify.com/v2/places?categories=healthcare&filter=circle:{longitude},{latitude},{radius}&apiKey=4373f00847434c0aa84a736ed9317207"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url, headers=headers)
print(resp.content)
print(resp.status_code)
