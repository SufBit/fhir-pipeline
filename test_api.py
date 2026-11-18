from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_patients():
    response = client.get("/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Assuming there could be zero or more patients

def test_get_patient():
    # request 1: the list
    list_response = client.get("/patients")
    first_id = list_response.json()[0]["id"]    
    # request 2: ONE patient, using that id
    detail_response = client.get(f"/patients/{first_id}")

    assert detail_response.status_code == 200
    assert detail_response.json()["id"] == first_id

def test_patient_not_found():
    response = client.get("/patients/nonexistent_id")  # Use an ID that doesn't exist
    assert response.status_code == 404
    assert response.json() == {"detail": "Patient not found"}