from core.utils import verify_token

def validate_token(token: str):
    payload = verify_token(token)
    if payload:
        return {"valid": True, "user": payload}
    return {"valid": False, "message": "Invalid token"}