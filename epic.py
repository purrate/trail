import requests
import subprocess
from requests.structures import CaseInsensitiveDict
from geopy.geocoders import OpenCage
import time

news_api_key = "b2810dea161648c39b9992907e6b20ee"

disaster = input("Enter the type of disaster: ")
location = input("Enter the type of location: ")


while True:
    choice = int(input("Enter (1) to get news\n, (2) to analyze financial losses\n, (3) to get weather data\n, (4) to get weather data\n, (5) to locate shelters\n, (6) to contact NGOs\n, (7) to alert: \n"))

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

        url = 'http://localhost:8080/'
        payload = {
            "user": "user",
            "query": f"What is the approximate financial loss caused by {tye} type of {disaster}?"
        }

        # Send the POST request
        response = requests.post(url, json=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content
            print(response.text)
        else:
            # Print the error message if the request was not successful
            print(f"Request failed with status code {response.status_code}: {response.text}")
    elif choice == 3:
        weather_api_key = 'b7ffb244ca0e3202990c493461eef1cb'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}"

        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            if weather_data:
              # Access the weather data
              temperature = weather_data['main']['temp']
              humidity = weather_data['main']['humidity']
              description = weather_data['weather'][0]['description']

              print(f"Weather in {location}:")
              print(f"Temperature: {temperature} K")
              print(f"Humidity: {humidity}%")
              print(f"Description: {description}")
        else:
            print(f"Request failed with status code {response.status_code}")


    elif choice == 5:
        latitude = input("enter latitude of the place")
        longitude = input("enter longitude of the place")
        radius = int(input("enter surrounding radius"))

        url = f"https://api.geoapify.com/v2/places?categories=healthcare&filter=circle:{longitude},{latitude},{radius}&limit=20&apiKey=4373f00847434c0aa84a736ed9317207"

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
          auth_token = '27de90032ec3ae9a0dab73966ea675f7'
          client = Client(account_sid, auth_token)

          url1 = 'http://localhost:8080/'
          payl = {
              "user": "user",
              "query": f"List the safetly guidelines mentioned for the type of {disaster}?"
          }

          # Send the POST request
          response = requests.post(url1, json=payl)

        # Check if the request was successful (status code 200)
          if response.status_code == 200:
              # Print the response content
              k = response.text
              print(k)
          else:
              # Print the error message if the request was not successful
              print(f"Request failed with status code {response.status_code}: {response.text}")


          message = client.messages.create(
            from_='+19299551314',
            body=k,
            to='+919363233485'
          )

          print(message.sid)


    else:
      print("Invalid choice. Please try again.")









