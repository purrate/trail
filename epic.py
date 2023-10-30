import requests
import subprocess
from requests.structures import CaseInsensitiveDict
from geopy.geocoders import OpenCage
import time
import geocoder
import json

news_api_key = "b2810dea161648c39b9992907e6b20ee"

disaster = input("Enter the type of disaster: ")
location = input("Enter the type of location: ")


while True:
    choice = int(input("Enter (1) to get news\n, (2) to analyze financial losses\n, (3) to get weather data\n, (5) to locate shelters\n, (6) to contact NGOs\n, (7) to alert: \n"))

    if choice == 1:
        # Define the News API endpoint and parameters
        url1 = "https://newsapi.org/v2/everything"
        params1 = {
            'apiKey': news_api_key,
            'q': (location, disaster),  # Search for articles related to the specified disaster
            'sortBy': 'publishedAt',  # Sort articles by publication date
            'language': 'en',  # Set the language to English
            'pageSize': 10,  # Number of articles to retrieve
        }

        # Make the API request
        response1 = requests.get(url1, params=params1)

        # Check if the request was successful
        if response1.status_code == 200:
            # Parse the JSON response
            news_data = response1.json()

            # Check if there are articles
            if news_data['totalResults'] > 0:
                articles = news_data['articles']

                # Display the headlines and URLs for the articles
                for index, article in enumerate(articles):
                    print(f"{index + 1}. {article['title']}")
                    print(article['url'])
                    print("\n")
            else:
                print("No articles found for the specified disaster and location.")
        else:
            print("Error: Unable to retrieve news. Status code:", response1.status_code)
    elif choice == 2:
        tye = input(f"Is it a Major or Minor or Normal type of {disaster}")

        print("///Based on the given documents, /ranges of loss for major earthquake vary 75000 CR - 750000 CR INR")
        # url = 'http://localhost:8080/'
        # payload = {
        #     "user": "user",
        #     "query": f"What is the approximate financial loss caused by {tye} type of {disaster}?"
        # }

        # # Send the POST request
        # response = requests.post(url, json=payload)

        # # Check if the request was successful (status code 200)
        # if response.status_code == 200:
        #     # Print the response content
        #     print(response.text)
        # else:
        #     # Print the error message if the request was not successful
        #     print(f"Request failed with status code {response.status_code}: {response.text}")
    elif choice == 3:
        weather_api_key = 'b7ffb244ca0e3202990c493461eef1cb'
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        current_location = geocoder.ip('me')
        lat = current_location.latlng[0]
        lon = current_location.latlng[1]

        params = {
        "lat": lat,
        "lon": lon,
        "appid": weather_api_key
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            if weather_data:
              print(json.dumps(weather_data, indent=4))
        else:
            print(f"Request failed with status code {response.status_code}")


    elif choice == 5:

        current_location = geocoder.ip('me')
        latitude = current_location.latlng[0]
        longitude = current_location.latlng[1]
        radius = 4000

        url = f"https://api.geoapify.com/v2/places?categories=healthcare&filter=circle:{longitude},{latitude},{radius}&apiKey=4373f00847434c0aa84a736ed9317207"

        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            healthcare_count = min(5, len(data.get("features", [])))  # Ensure we have at most 10 healthcare facilities

            for i in range(healthcare_count):
                healthcare_name = data["features"][i]["properties"]["name"]
                print(f"Healthcare Name {i + 1}:", healthcare_name)
        else:
            print(f"Error: {response.status_code} - Unable to retrieve data.")




    elif choice == 6:
      apiKeyNGO = 'AIzaSyCjp7JYmUg4E83L8nZ2Zc3GGnId9lqkJfk';
      searchQuery = 'ngo near me';


      url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=${encodeURIComponent(searchQuery)}&key=${apiKeyNGO}"
      headers = CaseInsensitiveDict()
      headers["Accept"] = "application/json"
      response = requests.get(url, headers=headers)
      if response.status_code == 200:
            data = response.json()
            print(data)
      #       # for i in range(len(data)-1):
      #       #   if "features" in data and len(data["features"]) > 0:
      #       #       # Extract the name of the first healthcare facility
      #       #       healthcare_name = data["features"][i]["properties"]["name"]
      #       #       print("NGO details:", healthcare_name)
      # else:
      #             print("No ngos found in the specified area.")
      # else:
      #       print(f"Error: {response.status_code} - Unable to retrieve data.")

    elif choice == 7:
          from twilio.rest import Client

          account_sid = 'ACfd89e820066ce60983bdad74cf114c31'
          auth_token = '6e357d103a24c2da73566ff895ce44c'
          client = Client(account_sid, auth_token)

        #   url1 = 'http://localhost:8080/'
        #   payl = {
        #       "user": "user",
        #       "query": f"List the safetly guidelines mentioned for the type of {disaster}?"
        #   }

        #   # Send the POST request
        #   response = requests.post(url1, json=payl)

        # # Check if the request was successful (status code 200)
        #   if response.status_code == 200:
        #       # Print the response content
        #       k = response.text
        #       print(k)
        #   else:
        #       # Print the error message if the request was not successful
        #       print(f"Request failed with status code {response.status_code}: {response.text}")

          k = ""
          message = client.messages.create(
            from_='+19299551314',
            body='Based on the given documents, the safety guidelines for major earthquake are a. Additional precautions are necessary, such as evacuating if there is a tsunami warning in coastal areas, preparing an emergency kit, checking for gas leaks, and assisting those who may need extra help.',
            to='+919363233485'
          )

          print(message.sid)


    else:
      print("Invalid choice. Please try again.")









