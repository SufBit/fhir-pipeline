import requests
import json


url = "https://hapi.fhir.org/baseR4/Patient?_count=10"
response = requests.get(url, timeout=10)
response.raise_for_status()
bundle = response.json()

print(len(bundle["entry"]))

for entry in bundle["entry"]:
    patient = entry["resource"]
    print(f"Patient ID: {patient['id']}, Name: {patient['name'][0]['given'][0]} {patient['name'][0]['family']}")

json.dump(bundle["entry"][0]["resource"], open("bundle.json", "w"), indent=2)
