import requests

url = "https://dev02@one-it.ro:dev02@shop.one-it.ro/gomag/login"

payload = "{}"
response = requests.request("GET", url, data=payload)

print(response.text)