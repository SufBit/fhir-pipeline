from fetch import fetch_patients
from clean import clean_patient
import sqlite3
from store import create_table, insert_patient


def main():
    patients = fetch_patients("https://hapi.fhir.org/baseR4/Patient?_count=10")
    cleaned_patients = []
    rejected_patients = 0
    for patient in patients:
        try:
            cleaned_patient = clean_patient(patient)
            cleaned_patients.append(cleaned_patient)
        except ValueError as e:
            print(f"Error cleaning patient {patient.get('id', 'unknown')}: {e}")
            rejected_patients += 1
    print(f"Total patients fetched: {len(patients)}")
    print(f"Total patients cleaned: {len(cleaned_patients)}")
    print(f"Total patients rejected: {rejected_patients}")

    conn = sqlite3.connect("fhir.db")
    create_table(conn)
    insert_patient(conn, cleaned_patients)
    conn.close()

if __name__ == "__main__":
    main()