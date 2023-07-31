## Architecture Description

The PhoneBook REST API can be used to track entries of contacts that include the names and contact information for people.
An authenticated user can create, delete, search, and view contacts that are stored in the database.
A Contact in the PhoneBook is defined as follows:

```
Contact {
    id: int
    first_name: string
    last_name: string
    phone_number: string
    address: string
}
```

The PhoneBook is set up to use PostgreSQL as a database, SQLAlchemy to connect to the database, and Flask to define the API. 
There are 6 HTTP methods defined for accessing and managing the Contacts in the PostgreSQL database.


### List all events
* URI: `/contacts`

### View a certain event
* URI: `/contacts/<int:id>`

### Create new events
* URI: `/contacts/create`

### Remove events
* URI: `/contacts/delete/<int:id>`

### Search events via the title (first/last name) or description (phone number)
* URI: `/contacts/search/name/<name>`
* URI: `/contacts/search/phone/<phone>`

### Tools Used:
* Python3
* Flask
* Flask-SQLAlchemy - Library used to connect to the DB
* PostgresSQL - Database used to store data

## Installation Instructions
* Download the project zip file.
* Navigate to the project folder and run `python3 main.py`
* In a separate window, run the below scripts to execute each action.
  * All scripts can be found in the
  `PhoneBook/scripts` directory.
  * Parameter values can be changed in each script to update the user input.
  * Each script is named to correspond to the word in bold under the “This
solution should provide” heading.

## Script Examples for Execution

* The user being able to see/list all the events they have created
  * See `Phonebook/scripts/list.py` for an example.
* The user being able to create new events
 * See `Phonebook/scripts/create.py` for an example.
* The user can pick a certain event to view its data
  * See `Phonebook/scripts/view.py` for an example.
* The user being able to remove those events if needed.
  * See `Phonebook/scripts/remove.py` for an example.
* User being able to search the events via the title or description of the event
  * See `Phonebook/scripts/list.py` for an example.
