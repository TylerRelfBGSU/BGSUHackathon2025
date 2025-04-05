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
    ('Neck', 'Mild Pain', 'Neck Tilts', 'Gently stretches the neck muscles for relief.'),
    ('Neck', 'Moderate Injury', 'Neck Isometrics', 'Builds strength without joint movement.'),
    ('Neck', 'Moderate Injury', 'Side Neck Stretch', 'Relieves tightness in neck and upper trapezius.'),
    ('Neck', 'Major Injury', 'Supported Neck ROM', 'Gentle assisted movements for post-injury recovery.'),
    ('Neck', 'Major Injury', 'Chin to Chest Stretch', 'Gentle mobility for recovery after surgery or trauma.'),

    # Shoulder
    ('Shoulder', 'Mild Pain', 'Pendulum Swings', 'Loosens joint gently.'),
    ('Shoulder', 'Mild Pain', 'Shoulder Shrugs', 'Relieves tightness and improves blood circulation.'),
    ('Shoulder', 'Moderate Injury', 'Wall Slides', 'Promotes range of motion safely.'),
    ('Shoulder', 'Moderate Injury', 'External Rotation with Band', 'Strengthens rotator cuff muscles.'),
    ('Shoulder', 'Moderate Injury', 'Internal Rotation with Band', 'Strengthens internal rotator cuff muscles.'),
    ('Shoulder', 'Major Injury', 'Assisted Shoulder Flexion', 'Post-surgical mobilization.'),
    ('Shoulder', 'Major Injury', 'Passive Shoulder Extension', 'Post-surgical movement for flexibility.'),
    
    # Elbow
    ('Elbow', 'Mild Pain', 'Wrist Flexor Stretch', 'Relieves tension in forearm.'),
    ('Elbow', 'Mild Pain', 'Triceps Stretch', 'Relieves tightness and stretches the triceps muscles.'),
    ('Elbow', 'Moderate Injury', 'Eccentric Wrist Curls', 'Strengthens tendons post-strain.'),
    ('Elbow', 'Moderate Injury', 'Reverse Wrist Curls', 'Targets extensor muscles to aid in recovery.'),
    ('Elbow', 'Major Injury', 'Passive Elbow Flexion', 'Gentle movement post-fracture.'),
    ('Elbow', 'Major Injury', 'Elbow Extensions with Light Resistance', 'Rebuilds elbow strength after injury.'),

    # Wrist
    ('Wrist', 'Mild Pain', 'Prayer Stretch', 'Opens wrist and forearm flexors.'),
    ('Wrist', 'Mild Pain', 'Wrist Flexor Stretch', 'Relieves wrist flexor tightness.'),
    ('Wrist', 'Moderate Injury', 'Wrist Circles', 'Improves circulation and mobility.'),
    ('Wrist', 'Moderate Injury', 'Resisted Wrist Flexion', 'Strengthens the wrist and forearm flexors.'),
    ('Wrist', 'Major Injury', 'Grip Squeeze with Soft Ball', 'Strengthens safely post-injury.'),
    ('Wrist', 'Major Injury', 'Forearm Plank', 'Strengthens wrists and forearms while engaging core.'),

    # Lower Back
    ('Lower Back', 'Mild Pain', 'Cat-Cow Stretch', 'Mobilizes spine with gentle motion.'),
    ('Lower Back', 'Mild Pain', 'Child’s Pose', 'Stretches and relaxes the lower back muscles.'),
    ('Lower Back', 'Moderate Injury', 'Pelvic Tilts', 'Activates core and supports spine.'),
    ('Lower Back', 'Moderate Injury', 'Knee-to-Chest Stretch', 'Relieves lower back tension and stretches hip flexors.'),
    ('Lower Back', 'Major Injury', 'Diaphragmatic Breathing', 'Pain-relieving technique with no spinal motion.'),
    ('Lower Back', 'Major Injury', 'Bridge Pose', 'Strengthens glutes and lower back muscles while keeping core stable.'),

    # Hip
    ('Hip', 'Mild Pain', 'Hip Flexor Stretch', 'Releases tight hip muscles.'),
    ('Hip', 'Mild Pain', 'Standing Hip Abduction', 'Strengthens hip abductors and promotes stability.'),
    ('Hip', 'Moderate Injury', 'Clamshells', 'Strengthens glutes and supports hip stability.'),
    ('Hip', 'Moderate Injury', 'Side-Lying Leg Raise', 'Targets hip abductors for strengthening.'),
    ('Hip', 'Major Injury', 'Heel Slides', 'Initiates mobility post-surgery.'),
    ('Hip', 'Major Injury', 'Hip Rotations', 'Gentle movement to restore mobility after hip injury.'),

    # Knee
    ('Knee', 'Mild Pain', 'Quad Stretch', 'Relieves tightness and improves range.'),
    ('Knee', 'Mild Pain', 'Hamstring Stretch', 'Improves flexibility and reduces tension.'),
    ('Knee', 'Moderate Injury', 'Step-Ups', 'Rebuilds leg strength safely.'),
    ('Knee', 'Moderate Injury', 'Lunges', 'Strengthens quadriceps and hip flexors with control.'),
    ('Knee', 'Major Injury', 'Straight Leg Raise', 'Protects joint while building strength.'),
    ('Knee', 'Major Injury', 'Heel Slides', 'Restores motion in a safe range.'),
    ('Knee', 'Major Injury', 'Quad Sets', 'Strengthens quadriceps muscles post-injury.'),

    # Ankle
    ('Ankle', 'Mild Pain', 'Ankle Circles', 'Improves joint mobility.'),
    ('Ankle', 'Mild Pain', 'Calf Stretch', 'Relieves tension in calf muscles and improves ankle flexibility.'),
    ('Ankle', 'Moderate Injury', 'Towel Scrunches', 'Strengthens foot and ankle.'),
    ('Ankle', 'Moderate Injury', 'Standing Heel Raises', 'Strengthens the calves and improves ankle function.'),
    ('Ankle', 'Major Injury', 'Toe Raises', 'Improves strength post-immobilization.'),
    ('Ankle', 'Major Injury', 'Ankle Dorsiflexion Stretch', 'Stretches the dorsiflexors to improve ankle movement.'),

    # Foot
    ('Foot', 'Mild Pain', 'Toe Stretch', 'Eases plantar tension.'),
    ('Foot', 'Mild Pain', 'Foot Rolls', 'Relieves tension and improves blood flow to the feet.'),
    ('Foot', 'Moderate Injury', 'Marble Pickups', 'Improves foot control and strength.'),
    ('Foot', 'Moderate Injury', 'Towel Curls', 'Strengthens the muscles on the bottom of the foot.'),
    ('Foot', 'Major Injury', 'Weight Shifts', 'Reintroduces pressure safely after fracture.'),
    ('Foot', 'Major Injury', 'Heel Raises', 'Strengthens the calves and supports foot rehabilitation.'),

    # Upper Back
    ('Upper Back', 'Mild Pain', 'Seated Rows', 'Strengthens upper back muscles and improves posture.'),
    ('Upper Back', 'Mild Pain', 'Thoracic Extension Stretch', 'Relieves tension and improves upper back mobility.'),
    ('Upper Back', 'Moderate Injury', 'Scapular Retraction', 'Strengthens the muscles around the shoulder blades.'),
    ('Upper Back', 'Moderate Injury', 'Wall Angels', 'Improves shoulder mobility and posture.'),
    ('Upper Back', 'Moderate Injury', 'Prone Y-T-W', 'Strengthens upper back muscles and stabilizers.'),
    ('Upper Back', 'Major Injury', 'Assisted Upper Back Rotation', 'Gentle stretch for recovery from upper back injury.'),
    ('Upper Back', 'Major Injury', 'Thoracic Spine Mobilization', 'Assisted movements to restore upper back mobility after injury.')
]

cursor.executemany('''
INSERT INTO exercises (body_part, severity, exercise, description)
VALUES (?, ?, ?, ?)
''', data)

conn.commit()
conn.close()
print("Enhanced injury-specific exercise database created.")