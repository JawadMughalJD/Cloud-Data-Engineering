import requests

url = "https://api.apilayer.com/bank_data/all"

payload = {}
headers = {
    "apikey": "m0MppXlvnxmJNxwCyv7PqtFYAeavPmi2"
}

params = {
    'per_page':'5',
    'page':'1',
    'country':'pakistan'
}

response = requests.request("GET", url, headers=headers, data = payload, params=params)

print(response.text)
data = response.json()
print(data)