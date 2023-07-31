import requests

# The id of the contact to delete can be updated here
contact_id = 0

url = 'http://127.0.0.1:5000/contacts/delete/{}'.format(contact_id)

response = requests.post(url)

print(response.status_code)
print(response.content)
