import requests

# The name of the contact to search for.
# It can be the first or last name, and it can be a beginning substring i.e. you can search 'Sm' to find 'Smith'.
name = 'Smith'

url = 'http://127.0.0.1:5000/contacts/search/name/{}'.format(name)

response = requests.get(url)

print(response.status_code)
print(response.content)