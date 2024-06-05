import requests

url = "http://127.0.0.1:5000/api/v1/"

headers = {"Content-Type": "application/json", "charset": "UTF-8"}
params = {"name": "Dell"}
response = requests.post(url, params = params, headers=headers, timeout=10) # Check this one out.

print(response.json())