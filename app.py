import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Firebase credentials and database URL from environment variables
firebase_cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
firebase_db_url = os.getenv('FIREBASE_DB_URL')

# Initialize Firebase with your credentials from the .env file
cred = credentials.Certificate(firebase_cred_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': firebase_db_url
})

app = Flask(__name__)

# Get all available body parts for the dropdown (assumes Firebase has a structure with body parts)
def get_body_parts():
    ref = db.reference('')
    exercises_data = ref.get()  # Get all the exercises from the Firebase Realtime Database
    print("Fetched exercises data:", exercises_data)  # Log the fetched data

    if exercises_data is None:
        print("No data found at the root of the database.")
        return []

    # Exclude "messages" key from the list of body parts
    body_parts = [key for key in exercises_data.keys() if key.lower() != 'messages']
    print("Filtered body parts:", body_parts)  # Log filtered body parts

    return body_parts

# Function to fetch exercises based on body part and severity
def get_exercises(body_part=None, severity=None):
    ref = db.reference('')
    exercises_data = ref.get()  # Get all exercises from the database
    
    if exercises_data:
        # Log the structure of the data to verify it matches
        print("Fetched exercises data:", exercises_data)
    
    if body_part and severity:
        exercises = exercises_data.get(body_part, {}).get(severity, [])
    else:
        exercises = []
    
    # Reformat the exercises to match the new structure (description, exercise)
    formatted_exercises = [
        {'exercise': ex['exercise'], 'description': ex['description']}
        for ex in exercises
    ]
    
    return formatted_exercises

@app.route('/')
def index():
    body_parts = get_body_parts()  # Get all body parts for the dropdown
    print("Body parts fetched:", body_parts)  # Log body parts list for debugging
    return render_template('index.html', body_parts=body_parts)

@app.route('/get_exercises', methods=['POST'])
def get_exercises_ajax():
    body_part = request.form.get('body_part')
    severity_int = request.form.get('severity')

    print(f"Selected Body Part: {body_part}")
    print(f"Selected Severity: {severity_int}")

    severity_map = {
        '1': 'Mild Pain',
        '2': 'Moderate Injury',
        '3': 'Major Injury'
    }
    
    severity = severity_map.get(severity_int)

    # Get the exercises based on selected body part and severity
    exercises = get_exercises(body_part, severity)

    # Format exercises to include body part and severity
    exercises_data = [
        {'exercise': ex['exercise'], 'description': ex['description'], 'body_part': body_part, 'severity': severity}
        for ex in exercises
    ]
    
    return jsonify(exercises_data)
    
@app.route('/submit_message', methods=['POST'])
def submit_message():
    body_part = request.form['body_part']
    severity_map = {'1': 'Mild Pain', '2': 'Moderate Injury', '3': 'Major Injury'}
    severity = severity_map.get(request.form['severity'])
    message = request.form['message']

    ref = db.reference(f"messages/{body_part}/{severity}")
    ref.push(message)
    return '', 204

@app.route('/get_messages', methods=['POST'])
def get_messages():
    body_part = request.form['body_part']
    severity_map = {'1': 'Mild Pain', '2': 'Moderate Injury', '3': 'Major Injury'}
    severity = severity_map.get(request.form['severity'])

    ref = db.reference(f"messages/{body_part}/{severity}")
    messages_data = ref.get()
    messages = list(messages_data.values()) if messages_data else []
    return jsonify(messages)
    
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
