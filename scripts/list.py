import requests

url = 'http://127.0.0.1:5000/contacts'

response = requests.get(url)

print(response.status_code)
print(response.content)
