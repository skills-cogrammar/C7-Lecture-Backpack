# Import the requests library, which allows you to send HTTP requests in Python.
import requests

# Define the URL for the API endpoint you want to send a POST request to.
url = "https://real-time-web-search.p.rapidapi.com/search"

# Define the payload with the search queries and limit.
# The payload is a dictionary containing:
# - "queries": A list of search terms you want to look up.
# - "limit": The number of search results to return for each query.
payload = {
    "queries": ["build a website", "chatgpt", "home depot", "world cup"],
    "limit": "10"
}

# Define the headers for the HTTP request.
# The headers dictionary includes:
# - "x-rapidapi-key": Your unique API key for authentication.
# - "x-rapidapi-host": The host name of the RapidAPI service.
# - "Content-Type": Specifies that the content being sent is in JSON format.
headers = {
    "x-rapidapi-key": "30e584c23dmsh3e9be1b33e648e0p156c84jsndcef92bc25d1",
    "x-rapidapi-host": "real-time-web-search.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Send a POST request to the API endpoint with the specified URL, payload, and headers.
# The `json=payload` argument ensures that the payload is sent as JSON.
response = requests.post(url, json=payload, headers=headers)

# Print the JSON response from the API.
# `response.json()` parses the JSON response content into a Python dictionary.
print(response.json())
