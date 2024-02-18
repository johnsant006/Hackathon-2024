#imports necessary modules from Flask application
from flask import Flask, render_template, request, redirect, url_for

#creates an instance of Flask
app = Flask(__name__)

#creates an empty list to store contacts
contacts = []

#defines a route for the homepage
@app.route('/')
def index():
    #renders the index.html template and pass the contacts list to it
    return render_template('index.html', contacts=contacts)

#defines a route to handle adding a new contact
@app.route('/add_contact', methods=['POST'])
def add_contact():
    #extracts name, phone, and address from the form data
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    address = request.form['address']
    #appends the new contact to the contacts list as a dictionary
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    #redirects to the homepage
    return redirect(url_for('index'))

#runs the Flask application
if __name__ == '__main__':
    app.run(debug=True)
