from fastapi import APIRouter
from pydantic import BaseModel
from Customer.views.auth_handlers import handle_customer_login, handle_customer_register

router = APIRouter(prefix="/customer", tags=["Customer"])

class CustomerLoginRequest(BaseModel):
    email: str
    password: str

class CustomerRegisterRequest(BaseModel):
    email: str
    password: str
    name: str

@router.post("/login")
def login_customer(request: CustomerLoginRequest):
    return handle_customer_login(request.email, request.password)

@router.post("/register")
def register_customer(request: CustomerRegisterRequest):
    return handle_customer_register(request.email, request.password, request.name)