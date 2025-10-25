from fastapi import Depends
from auth.views.tokenAuthentication import get_current_user
from auth.views.checkAdmin import check_admin_role
from dashboard.views.dashboardLogic import get_dashboard_stats

def get_admin_dashboard(current_user: dict = Depends(get_current_user)):
    check_admin_role(current_user)
    return get_dashboard_stats()