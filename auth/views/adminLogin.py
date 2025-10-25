from fastapi import HTTPException
from core.database import admins_collection
from core.utils import verify_password

def admin_login(email: str, password: str):
    # Default admin credentials
    if email == "admin@gmail.com" and password == "admin12345":
        return {"admin_id": "default_admin", "email": "admin@gmail.com"}
    
    admin = admins_collection.find_one({"email": email})
    if not admin or not verify_password(password, admin["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"admin_id": str(admin["_id"]), "email": admin["email"]}