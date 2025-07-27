from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

# 1. Create Flask App
app = Flask(__name__)

# 2. Connect to MongoDB
client = MongoClient("mongodb+srv://teenasahu0406:teena@0406@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority")
db = client["founders_event"]  # database name
registrations = db["registrations"]  # collection for event registrations
messages = db["messages"]  # collection for contact form messages

# 3. Home Page - Event Info
@app.route('/')
def index():
    return render_template('index.html')

# 4. Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'department': request.form['department']
        }
        registrations.insert_one(data)  # Save to MongoDB
        return render_template('index.html', message='Registration successful!')
    return render_template('register.html')

# 5. Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        msg = {
            'name': request.form['name'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        messages.insert_one(msg)  # Save to MongoDB
        return render_template('index.html', message='Message sent successfully!')


    return render_template('contact.html')

@app.route('/foundathon', methods=['GET', 'POST'])
def foundathon():
    if request.method == 'POST':
        data = {
            'event': 'Foundathon',
            'name': request.form['name'],
            'email': request.form['email'],
            'department': request.form['department']
        }
        registrations.insert_one(data)
        return render_template('index.html', message='Registered for Foundathon!')
    return render_template('foundathon.html')

@app.route('/ideathon', methods=['GET', 'POST'])
def ideathon():
    if request.method == 'POST':
        data = {
            'event': 'Ideathon',
            'name': request.form['name'],
            'email': request.form['email'],
            'department': request.form['department']
        }
        registrations.insert_one(data)
        return render_template('index.html', message='Registered for Ideathon!')
    return render_template('ideathon.html')


# 6. Run App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

