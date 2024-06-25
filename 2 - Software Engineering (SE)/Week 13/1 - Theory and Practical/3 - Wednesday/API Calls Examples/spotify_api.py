# Import the requests library, which allows you to send HTTP requests in Python.
import requests

# Define the URL for the API endpoint you want to send a GET request to.
url = "https://spotify23.p.rapidapi.com/search/"

# Define the query string parameters for the GET request.
# The querystring is a dictionary containing:
# - "q": The search term, in this case, "justin bieber".
# - "type": The type of search, e.g., "multi" to search across multiple categories (artists, albums, tracks, etc.).
# - "offset": The index of the first result to return (used for pagination).
# - "limit": The number of results to return.
# - "numberOfTopResults": The number of top results to return.
querystring = {
    "q": "justin bieber",
    "type": "multi",
    "offset": "0",
    "limit": "1",
    "numberOfTopResults": "1"
}

# Define the headers for the HTTP request.
# The headers dictionary includes:
# - "x-rapidapi-key": Your unique API key for authentication.
# - "x-rapidapi-host": The host name of the RapidAPI service.
headers = {
    "x-rapidapi-key": "30e584c23dmsh3e9be1b33e648e0p156c84jsndcef92bc25d1",
    "x-rapidapi-host": "spotify23.p.rapidapi.com"
}

# Send a GET request to the API endpoint with the specified URL, headers, and query string parameters.
response = requests.get(url, headers=headers, params=querystring)

# Print the JSON response from the API.
# `response.json()` parses the JSON response content into a Python dictionary.
print(response.json())
