from datetime import timedelta
from core.utils import create_access_token
from core.config import ACCESS_TOKEN_EXPIRE_MINUTES

def create_token_for_user(user_data: dict):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_data["email"], "user_type": user_data.get("user_type", "user")},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}