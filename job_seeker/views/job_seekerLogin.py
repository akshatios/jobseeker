from fastapi import HTTPException
from .jobseeker_database import jobseekers_collection
from core.utils import verify_password

def job_seeker_login(email: str, password: str):
    user = jobseekers_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"user_id": str(user["_id"]), "email": user["email"], "user_type": "job_seeker"}