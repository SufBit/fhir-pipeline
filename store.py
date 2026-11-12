def create_table(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Patients (
            id TEXT,
            family_name TEXT NOT NULL,
            gender TEXT NOT NULL,
            birth_date TEXT
        )
    ''')

def insert_patient(conn, patients):
    conn.execute('''
        DELETE FROM Patients
    ''')
    for patient in patients:
        conn.execute('''INSERT INTO Patients VALUES (?, ?, ?, ?)''', (patient['id'], patient['family_name'], patient['gender'], patient['birth_date']))

    conn.commit()

