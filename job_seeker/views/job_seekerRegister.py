from fastapi import HTTPException
from .jobseeker_database import jobseekers_collection
from core.utils import hash_password

def job_seeker_register(email: str, password: str, name: str):
    if jobseekers_collection.find_one({"email": email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_data = {
        "email": email,
        "password": hash_password(password),
        "name": name,
        "user_type": "job_seeker"
    }
    result = jobseekers_collection.insert_one(user_data)
    return {"user_id": str(result.inserted_id), "email": email, "message": "Registration successful"}