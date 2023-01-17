import requests

url = "https://api.apilayer.com/bank_data/banks_by_country"

payload={}
headers = {
  'apikey': 'm0MppXlvnxmJNxwCyv7PqtFYAeavPmi2'
}

params = {
  'country_code' : 'PK'
}

response = requests.request("GET", url, headers=headers, data=payload, params=params)

print(response.text)
data = response.json()
print(data)
