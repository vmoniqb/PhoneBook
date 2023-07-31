import requests

# The phone number (or beginning substring) of the contact to search for.
phone_number = '123'

url = 'http://127.0.0.1:5000/contacts/search/phone/{}'.format(phone_number)

response = requests.get(url)

print(response.status_code)
print(response.content)
