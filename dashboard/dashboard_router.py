from fastapi import APIRouter, Depends
from dashboard.views.auth_handlers import get_admin_dashboard

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/stats")
def dashboard_stats(current_user: dict = Depends(get_admin_dashboard)):
    return current_user