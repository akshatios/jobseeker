from pymongo import MongoClient
from core.config import DATABASE_URL

client = MongoClient(DATABASE_URL)
db = client.jobportal

# Collections
users_collection = db.users
admins_collection = db.admins
jobs_collection = db.jobs

# Import separate database files
from Customer.views.customer_database import customers_collection
from job_seeker.views.jobseeker_database import jobseekers_collection