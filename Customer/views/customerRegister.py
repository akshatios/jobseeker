from fastapi import HTTPException
from .customer_database import customers_collection
from core.utils import hash_password

def customer_register(email: str, password: str, name: str):
    if customers_collection.find_one({"email": email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_data = {
        "email": email,
        "password": hash_password(password),
        "name": name,
        "user_type": "customer"
    }
    result = customers_collection.insert_one(user_data)
    return {"user_id": str(result.inserted_id), "email": email, "message": "Registration successful"}