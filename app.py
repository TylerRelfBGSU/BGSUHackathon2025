from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Map integer severity to string
severity_map = {
    '1': 'Mild Pain',
    '2': 'Moderate Injury',
    '3': 'Major Injury'
}

def get_exercises(body_part=None, severity=None):
    conn = sqlite3.connect('health.db')
    cursor = conn.cursor()

    query = "SELECT body_part, severity, exercise, description FROM exercises WHERE 1=1"
    
    if body_part:
        query += " AND body_part = ?"
    if severity:
        query += " AND severity = ?"

    params = []
    if body_part:
        params.append(body_part)
    if severity:
        params.append(severity)

    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()
    conn.close()

    return rows

@app.route('/', methods=['GET'])
def index():
    body_parts = ['Neck', 'Shoulder', 'Elbow', 'Wrist', 'Lower Back', 'Upper Back', 'Hip', 'Knee', 'Ankle', 'Foot']
    severities = ['Mild Pain', 'Moderate Injury', 'Major Injury']
    return render_template('index.html', body_parts=body_parts, severities=severities)

@app.route('/get_exercises', methods=['POST'])
def get_exercises_ajax():
    body_part = request.form.get('body_part')
    severity_int = request.form.get('severity')
    severity = severity_map.get(severity_int)

    exercises = get_exercises(body_part, severity)

    exercises_data = [
        {'body_part': row[0], 'severity': row[1], 'exercise': row[2], 'description': row[3]}
        for row in exercises
    ]
    
    return jsonify(exercises_data)

if __name__ == '__main__':
    app.run(debug=True)
