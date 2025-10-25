from core.database import users_collection, jobs_collection

def get_dashboard_stats():
    total_users = users_collection.count_documents({})
    total_customers = users_collection.count_documents({"user_type": "customer"})
    total_job_seekers = users_collection.count_documents({"user_type": "job_seeker"})
    total_jobs = jobs_collection.count_documents({})
    
    return {
        "total_users": total_users,
        "total_customers": total_customers,
        "total_job_seekers": total_job_seekers,
        "total_jobs": total_jobs
    }