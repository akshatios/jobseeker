from job_seeker.views.job_seekerLogin import job_seeker_login
from job_seeker.views.job_seekerRegister import job_seeker_register
from auth.views.createToken import create_token_for_user

def handle_job_seeker_login(email: str, password: str):
    user_data = job_seeker_login(email, password)
    return create_token_for_user(user_data)

def handle_job_seeker_register(email: str, password: str, name: str):
    return job_seeker_register(email, password, name)