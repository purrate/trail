#!/bin/bash

while true; do
  response=$(curl -s --data '{"user": "user", "query": "answer yes if theres a sign of disaster, answer no if theres not"}' http://localhost:8080/)
  echo "Response: $response"
  sleep 1  # Adjust the sleep duration as needed
done
