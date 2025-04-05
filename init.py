import sqlite3

conn = sqlite3.connect('health.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS exercises')  # optional, to reset
cursor.execute('''
CREATE TABLE exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    body_part TEXT NOT NULL,
    severity TEXT NOT NULL,
    exercise TEXT NOT NULL,
    description TEXT
)
''')

data = [
    # Neck
    ('Neck', 'Mild Pain', 'Chin Tucks', 'Improves posture and relieves tension in neck muscles.'),
    ('Neck', 'Moderate Injury', 'Neck Isometrics', 'Builds strength without joint movement.'),
    ('Neck', 'Major Injury', 'Supported Neck ROM', 'Gentle assisted movements for post-injury recovery.'),

    # Shoulder
    ('Shoulder', 'Mild Pain', 'Pendulum Swings', 'Loosens joint gently.'),
    ('Shoulder', 'Moderate Injury', 'Wall Slides', 'Promotes range of motion safely.'),
    ('Shoulder', 'Moderate Injury', 'External Rotation with Band', 'Strengthens rotator cuff muscles.'),
    ('Shoulder', 'Major Injury', 'Assisted Shoulder Flexion', 'Post-surgical mobilization.'),

    # Elbow
    ('Elbow', 'Mild Pain', 'Wrist Flexor Stretch', 'Relieves tension in forearm.'),
    ('Elbow', 'Moderate Injury', 'Eccentric Wrist Curls', 'Strengthens tendons post-strain.'),
    ('Elbow', 'Major Injury', 'Passive Elbow Flexion', 'Gentle movement post-fracture.'),

    # Wrist
    ('Wrist', 'Mild Pain', 'Prayer Stretch', 'Opens wrist and forearm flexors.'),
    ('Wrist', 'Moderate Injury', 'Wrist Circles', 'Improves circulation and mobility.'),
    ('Wrist', 'Major Injury', 'Grip Squeeze with Soft Ball', 'Strengthens safely post-injury.'),

    # Lower Back
    ('Lower Back', 'Mild Pain', 'Cat-Cow Stretch', 'Mobilizes spine with gentle motion.'),
    ('Lower Back', 'Moderate Injury', 'Pelvic Tilts', 'Activates core and supports spine.'),
    ('Lower Back', 'Major Injury', 'Diaphragmatic Breathing', 'Pain-relieving technique with no spinal motion.'),

    # Hip
    ('Hip', 'Mild Pain', 'Hip Flexor Stretch', 'Releases tight hip muscles.'),
    ('Hip', 'Moderate Injury', 'Clamshells', 'Strengthens glutes and supports hip stability.'),
    ('Hip', 'Major Injury', 'Heel Slides', 'Initiates mobility post-surgery.'),

    # Knee
    ('Knee', 'Mild Pain', 'Quad Stretch', 'Relieves tightness and improves range.'),
    ('Knee', 'Moderate Injury', 'Step-Ups', 'Rebuilds leg strength safely.'),
    ('Knee', 'Major Injury', 'Straight Leg Raise', 'Protects joint while building strength.'),
    ('Knee', 'Major Injury', 'Heel Slides', 'Restores motion in a safe range.'),

    # Ankle
    ('Ankle', 'Mild Pain', 'Ankle Circles', 'Improves joint mobility.'),
    ('Ankle', 'Moderate Injury', 'Towel Scrunches', 'Strengthens foot and ankle.'),
    ('Ankle', 'Major Injury', 'Toe Raises', 'Improves strength post-immobilization.'),

    # Foot
    ('Foot', 'Mild Pain', 'Toe Stretch', 'Eases plantar tension.'),
    ('Foot', 'Moderate Injury', 'Marble Pickups', 'Improves foot control.'),
    ('Foot', 'Major Injury', 'Weight Shifts', 'Reintroduces pressure safely after fracture.')
]

cursor.executemany('''
INSERT INTO exercises (body_part, severity, exercise, description)
VALUES (?, ?, ?, ?)
''', data)

conn.commit()
conn.close()
print("Enhanced injury-specific exercise database created.")