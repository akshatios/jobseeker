from pymongo import MongoClient
from core.config import DATABASE_URL

client = MongoClient(DATABASE_URL)
db = client.jobportal

# Collections
users_collection = db.users
admins_collection = db.admins
jobs_collection = db.jobs