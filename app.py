from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_exercises():
    conn = sqlite3.connect('health.db')
    cursor = conn.cursor()
    cursor.execute("SELECT body_part, severity, exercise, description FROM exercises")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    exercises = get_exercises()
    return render_template('index.html', exercises=exercises)

if __name__ == '__main__':
    app.run(debug=True)
