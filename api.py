from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/patients")
def get_patients():
    conn = sqlite3.connect("fhir.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM Patients''')
    patients = cursor.fetchall()
    conn.close()
    all_patients = [dict(patient) for patient in patients]
    return all_patients

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):
    conn = sqlite3.connect("fhir.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Patients WHERE id = ?''', (patient_id,))
    patient = cursor.fetchone()
    conn.close()
    if patient:
        return dict(patient)
    else:
        raise HTTPException(status_code=404, detail="Patient not found")