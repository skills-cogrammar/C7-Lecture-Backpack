# Import the requests library for sending HTTP requests.
import requests

# Define the headers for the HTTP request.
# The headers dictionary includes:
# - "content-type": Specifies that the content being sent is in JSON format.
# - "X-RapidAPI-Key": Your unique API key for authentication.
# - "X-RapidAPI-Host": The host name of the RapidAPI service.
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "4ac6c9bdb3mshb4e0b566f9a1d29p1c8350jsn4412c9dd2197",
    "X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
}

# Define the URL for the API endpoint you want to send a POST request to.
url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

# Define the payload with the model and messages.
# The payload is a dictionary containing:
# - "model": The specific model to be used, e.g., "gpt-3.5-turbo".
# - "messages": A list of messages to be sent, where each message has a "role" and "content".
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ]
}

# Send a POST request to the API endpoint with the specified URL, payload, and headers.
# The `json=payload` argument ensures that the payload is sent as JSON.
# The `timeout=10` argument specifies a timeout of 10 seconds for the request.
response = requests.post(url, json=payload, headers=headers, timeout=10)

# Print the status code of the response.
print(f"Status code: {response.status_code}")

# Print the JSON response from the API.
# `response.json()` parses the JSON response content into a Python dictionary.
print(f"Status response: {response.json()}")

# Extract and print the specific response content from the API.
# This accesses the "choices" list in the JSON response, gets the first item, and then retrieves the "content" of the "message".
print(f"Response from GPT: {response.json()['choices'][0]['message']['content']}")
