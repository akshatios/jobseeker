from fastapi import APIRouter
from auth.auth_router import router as auth_router
from Customer.customer_router import router as customer_router
from job_seeker.job_seeker_router import router as job_seeker_router
from dashboard.dashboard_router import router as dashboard_router

def include_routers(app):
    app.include_router(auth_router)
    app.include_router(customer_router)
    app.include_router(job_seeker_router)
    app.include_router(dashboard_router)