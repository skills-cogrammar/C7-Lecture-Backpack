import requests

url = "https://twitter154.p.rapidapi.com/hashtag/hashtag"

payload = {
	"hashtag": "#python",
	"limit": 20,
	"section": "top",
	"language": "en"
}
headers = {
	"x-rapidapi-key": "30e584c23dmsh3e9be1b33e648e0p156c84jsndcef92bc25d1",
	"x-rapidapi-host": "twitter154.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())