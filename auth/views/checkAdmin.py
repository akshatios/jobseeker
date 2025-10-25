from fastapi import HTTPException
from auth.views.tokenAuthentication import get_current_user

def check_admin_role(current_user: dict):
    if current_user.get("user_type") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user