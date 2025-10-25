from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from auth.views.adminLogin import admin_login
from auth.views.createToken import create_token_for_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

class AdminLoginRequest(BaseModel):
    email: str
    password: str

@router.post("/admin/login")
def login_admin(request: AdminLoginRequest):
    admin_data = admin_login(request.email, request.password)
    admin_data["user_type"] = "admin"
    return create_token_for_user(admin_data)