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
* Allows the user to view all the contacts that have been created. All elements of the database are returned and ordered based on last_name.
* Input: Request from the user to view all contacts.
* Output: Response containing all contacts currently in the database. 
* URI: `/contacts`

### View a certain event
* Allows the user to view a specific contact. A single element will be returned since IDs are unique.
* Input: Request containing the id of the contact to be viewed, `id: int`.
* Output: Response containing a single Contact.
* URI: `/contacts/<int:id>`

### Create new events
* Allows the user to create a new contact.
* Input: Request JSON specifying the Contact info, including:
  * `first_name: string`
  * `lastname: string`
  * `phone_number: string`
  * `address: string`
* Output: Response body confirming success or failure in creation.
* URI: `/contacts/create`

### Remove events
* Allows the user to delete a contact.
* Input: The id of the contact to be deleted, `id: int`.
* Output: Response body confirming success or failure in deletion.
* URI: `/contacts/delete/<int:id>`

### Search events via the title (first/last name) or description (phone number)
* Allows the user to search for contacts based on first name, last name, or phone number. All three are done based of the substring that the attribute starts with.
A single or multiple contacts can be returned depending on how many contacts match the search value entered.
* Input: Request containing the search string, `name: string` or `phone: string`.
* Output: Response with list of all contacts that start with the entered search term.
* URI: `/contacts/search/name/<name>`
* URI: `/contacts/search/phone/<phone>`

### Tools Used:
* Python3
* Flask
* Flask-SQLAlchemy - Library used to connect to the DB
* PostgresSQL - Database used to store data

## Installation Instructions
* Download the project zip file.
* Navigate to the folder `Phonebook/services/phonebook` and run `pip3 install -r requirements.txt`
* If PostgreSQL is not already installed on your device, run commands `brew install postgresql` and `brew services start postgresql` to ensure PostgreSQL is running.
* Locate the `postgresql.conf` file (likely location `cd /opt/homebrew/var/postgresql@14`)
* Update line 60 from `listen_addresses = 'localhost'` to `listen_addresses = '*'` in the .conf file
* Run Command: `/opt/homebrew/bin/createuser -s postgres`
* Run the application with command `python3 main.py`
  * Watchdog may need to be updated for a successful run (`pip3 install --upgrade watchdog`)


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
