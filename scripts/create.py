import requests

url = 'http://127.0.0.1:5000/contacts/create'

data = {
    'first_name': '<enter first name here>',
    'last_name': '<enter last name here>',
    'phone_number': '<enter phone number here>',
    'address': '<enter address here>'
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.content)
