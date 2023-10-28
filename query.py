import requests
import time

query = {"user": "user", "query": "answer yes if there's a sign of disaster, answer no if there is not"}
response = requests.post("http://localhost:8080/", json=query).json()  # Parse the JSON response
print(response)
if response == 'Yes':
  quer = {"user": "user", "query": "tell us the name of the natural disaster which has a sign of happening"}
  respons = requests.post("http://localhost:8080/", json=quer).json()  # Parse the JSON response
  print(respons)
else:
  print("fuck ur mom")


