# TRAIL

## IDEA

Every year, Our government is faced with some sort of challenge in handling emergency crisis situations. Our idea is to help with providing the Government with fast, concise and accurate solutions using a LLM such as GPT-3.5-turbo. We are implementing multiple features to make the crisis management process for the authorities in charge easier.


## APPROACH

- We use the available pathway LLM app to connect to GPT-3.5 to read the dataset thats necessary to our app
- We are using multiple modules in python such as geocoder, newsAPI, geoapi, requests to fetch required data and make it into a datatset.
- We are constantly trying to update the dataset by using a scheduler to keep the government upto date with the available services.
- We pass queries as a hard-code inside the script to get accurate results out of GPTs response.
- Based on the GPTs response, if the condition seems to severe, the user gets an option to send an alert to all the phone numbers stored in the database of that particular region.
- We are also planning to have an option to get data of all the NGOS nearby the disaster to seek help.
- At the end, we containerise the whole thing.

## WORKING OF PATHWAY LLM

Pathway LLM is a microservice. The program reads data from supplied dataset and embeds them using OpenAI document embedding model. By this it converts data base to vector database. Then this embedded data is and computes index by nearest neighbor index process. Then the program gets the query from user using REST API and indexes also them to get the appropriate prompt. This generated prompt is sent to GPT-4 chat service which sends the response to the user.

## USE-CASES

- Based on the dataset, pathway app estimates the extremeness of the financial losses that the government might face as an aftermath
- Our app detects the nearby locations and infrastructures (such as schools and hospitals) and informs the government to use them as rescue shelters.
- We provide them with the average casualties that they might expect during this disaster.
- App detects the NGOs that are nearby to the region of that specific disaster and helps in contacting them during the crisis.
- In case of a severe emergency, we also have a real time alert that is sent to the phones of the persons inside the local database of that region
- We also send the government real time weather information around the region where the disaster is happening.

## TECH-STACK

- Pathway LLM
- Python
- Git
- Chat-GPT
- Docker
- News API
- MySQL
