from fastapi import APIRouter
from pydantic import BaseModel
from job_seeker.views.auth_handlers import handle_job_seeker_login, handle_job_seeker_register

router = APIRouter(prefix="/job-seeker", tags=["Job Seeker"])

class JobSeekerLoginRequest(BaseModel):
    email: str
    password: str

class JobSeekerRegisterRequest(BaseModel):
    email: str
    password: str
    name: str

@router.post("/login")
def login_job_seeker(request: JobSeekerLoginRequest):
    return handle_job_seeker_login(request.email, request.password)

@router.post("/register")
def register_job_seeker(request: JobSeekerRegisterRequest):
    return handle_job_seeker_register(request.email, request.password, request.name)