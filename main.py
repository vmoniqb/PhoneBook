from dataclasses import dataclass
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func

import config

# Initialize the DB and app
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
db.init_app(app)

# Initialize test DB and test app
test_db = SQLAlchemy()
test_app = Flask(__name__)
test_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL_TEST
test_db.init_app(test_app)


# Define the Contact model
@dataclass
class Contact(db.Model):
    id: db.Mapped[int] = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    first_name: db.Mapped[str] = db.mapped_column(db.String(120), nullable=False)
    last_name: db.Mapped[str] = db.mapped_column(db.String(120))
    phone_number: db.Mapped[str] = db.mapped_column(db.String(120))
    address: db.Mapped[str] = db.mapped_column(db.String(250))

with app.app_context():
    db.create_all()

@dataclass
class ContactTest(test_db.Model):
    id: test_db.Mapped[int] = test_db.mapped_column(test_db.Integer, primary_key=True, autoincrement=True)
    first_name: test_db.Mapped[str] = test_db.mapped_column(test_db.String(120), nullable=False)
    last_name: test_db.Mapped[str] = test_db.mapped_column(test_db.String(120))
    phone_number: test_db.Mapped[str] = test_db.mapped_column(test_db.String(120))
    address: test_db.Mapped[str] = test_db.mapped_column(test_db.String(250))


with test_app.app_context():
    test_db.create_all()


# Return a list of all contacts
@app.route('/contacts')
def list_all_contacts():
    contacts = Contact.query.order_by(Contact.last_name).all()
    return jsonify(contacts)


# Return the data for a specific contact
@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    contact = db.get_or_404(Contact, id, description=f'There is no contact with the given id.')
    return jsonify(contact)


# Create a new contact in the address book
@app.route('/contacts/create', methods=['GET', 'POST'])
def create_contact():
    if request.method == 'POST':
        request_body = request.get_json()

        try:
            last_name = request_body['last_name']
        except KeyError:
            last_name = None

        try:
            phone_number = request_body['phone_number']
        except KeyError:
            phone_number = None

        try:
            address = request_body['address']
        except KeyError:
            address = None

        contact = Contact(
            first_name=request_body['first_name'],
            last_name=last_name,
            phone_number=phone_number,
            address=address,
        )

        db.session.add(contact)
        db.session.commit()
        return jsonify('Contact successfully created', contact)

    return jsonify('Contact could not be created')


# Delete a contact from the address book
@app.route('/contacts/delete/<int:id>', methods=['GET', 'POST'])
def delete_contact(id):
    contact = db.get_or_404(Contact, id, description=f'The given contact does not exist.')
    db.session.delete(contact)
    db.session.commit()
    return jsonify('Contact successfully deleted', contact)


# Search all contacts by first or last name
@app.route('/contacts/search/name/<name>', methods=['GET'])
def search_contacts_by_name(name):
    contacts = (Contact.query
                .filter(or_(func.lower(Contact.first_name).startswith(func.lower(name)),
                            func.lower(Contact.last_name).startswith(func.lower(name))))
                .order_by(Contact.last_name).all())
    return jsonify(contacts)


# Search all contacts by phone number
@app.route('/contacts/search/phone/<phone>', methods=['GET'])
def search_contacts_by_phone(phone):
    contacts = (Contact.query.filter(Contact.phone_number.startswith(phone)).order_by(Contact.last_name).all())
    return jsonify(contacts)


if __name__ == '__main__':
    app.run(debug=True)
