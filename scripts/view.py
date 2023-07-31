import requests

# The id of the contact to view can be updated here
contact_id = 1

url = 'http://127.0.0.1:5000/contacts/{}'.format(contact_id)

response = requests.get(url)

print(response.status_code)
print(response.content)
