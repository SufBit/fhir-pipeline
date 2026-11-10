import pytest
from clean import clean_patient

def make_patient():
    return {
        "resourceType": "Patient",
        "id": "nhanes-120412",
        "name": [{"use": "official", "family": "Whitfield", "given": ["Horace"]}],
        "gender": "male",
        "birthDate": "1973-02-28",
    }

def test_normal_patient():
    result = clean_patient(make_patient())
    assert result == {"id": "nhanes-120412", "family_name": "Whitfield", "gender": "male", "birth_date": "1973-02-28"}   # fill in the flat dict you expect

def test_missing_id():
    patient = make_patient()
    del patient["id"]
    with pytest.raises(ValueError):
        clean_patient(patient)

def test_missing_family_name():
    patient = make_patient()
    del patient["name"][0]["family"]
    with pytest.raises(ValueError):
        clean_patient(patient)

def test_missing_gender():
    patient = make_patient()
    del patient["gender"]
    result = clean_patient(patient)
    assert result["gender"] == "unknown"

def test_invalid_gender():
    patient = make_patient()
    patient["gender"] = "invalid"
    result = clean_patient(patient)
    assert result["gender"] == "unknown"

def test_missing_name():
    patient = make_patient()
    del patient["name"]
    with pytest.raises(ValueError):
        clean_patient(patient)

def test_empty_id():
    patient = make_patient()
    patient["id"] = ""
    with pytest.raises(ValueError):
        clean_patient(patient)