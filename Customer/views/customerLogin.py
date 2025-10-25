from fastapi import HTTPException
from .customer_database import customers_collection
from core.utils import verify_password

def customer_login(email: str, password: str):
    user = customers_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"user_id": str(user["_id"]), "email": user["email"], "user_type": "customer"}