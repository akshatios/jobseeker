from fastapi import HTTPException
from core.database import users_collection
from core.utils import verify_password

def job_seeker_login(email: str, password: str):
    user = users_collection.find_one({"email": email, "user_type": "job_seeker"})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"user_id": str(user["_id"]), "email": user["email"], "user_type": "job_seeker"}