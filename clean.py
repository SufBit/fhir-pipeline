def clean_patient(resource: dict) -> dict:
    # rule 1: missing id -> raise ValueError
    if not resource.get("id"):
        raise ValueError("Missing patient ID")
    # rule 2: missing family name -> your decision above
    name = resource.get("name", [])
    if not name:
        raise ValueError("Missing name")
    first_name = name[0]
    family_name = first_name.get("family")
    if not family_name:
        raise ValueError("Missing family name")
    
    #Rule 3: missing or invalid gender -> "unknown"
    gender = resource.get("gender")
    if gender not in ["male", "female", "other", "unknown"]:
        gender = "unknown"  
    # (rule 5 if you add birth_date: decide what a bad date does)
    birthDate = resource.get("birthDate")
    if not birthDate:
        birthDate = None  # or some default value, or raise an error
    return {
        "id": resource["id"],
        "family_name": family_name,
        "gender": gender,
        "birth_date": birthDate
    }   # flat dict: id, family_name, gender (and birth_date)