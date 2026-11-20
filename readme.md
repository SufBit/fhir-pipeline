# FHIR Patient Pipeline

The project uses FHIR end points that read and store the data into an SQLite database, we call the database using APIs to get patinet records

# About The Data

This is test patient data from a public server

# How to run it 

pip install -r requirements.txt - Installs requirements
python main.py it runs the pipeline, fetch, clean, store in fhir.db
uvicorn api:app --reload, starts a local server and auto restarts when changes are made
pytest - runs all test
docker build -t fhir-api - Builds the docker image 
docker run -p 8000:8000 fhir-api starts the container from the image

# API Endpoints

- /health - Just makes sure api is working
- /patients - Gets all patients in database
- /patients/{id} - Gets specific patient with ID

## Design decisions

- **Missing patient id → rejected.** The id is the key used to store and look up every record, so a patient without one can't be found again.
- **Missing family name → rejected.** A record with no name is hard to use or verify, so it's counted as rejected and not stored.
- **Missing or invalid gender → `unknown`.** FHIR defines `unknown` as a valid value, so the record stays usable instead of being dropped over one missing field.
- **Table emptied before each insert.** The pipeline is safe to re-run. Without this, every run would add the same patients again.
- **Fetch capped at a few pages.** The public test server holds thousands of patients. A small sample is enough and keeps runs fast.

## Next steps

- Mount the database as a Docker volume so the container can use fresh data without a rebuild.
- Add authentication to the API.
- Add FHIR Observations (labs and vitals) and join them to patients.