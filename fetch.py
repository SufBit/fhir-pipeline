import requests
import time

def get_with_retry(url: str, retries: int = 3) -> requests.Response:
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise
            time.sleep(2)


def fetch_patients(url, max_pages = 3):
    patients = []
    page_count = 0
    while url and page_count < max_pages:
        bundle = get_with_retry(url).json()
        patients_data = bundle.get("entry", [])
        for patient_entry in patients_data:
            patient = patient_entry.get("resource", {})
            patients.append(patient)
        url = None
        for link in bundle.get("link", []):
            if link["relation"] == "next":
                url = link["url"]
        page_count += 1
    return patients

print(len(fetch_patients("https://hapi.fhir.org/baseR4/Patient?_count=10")))
