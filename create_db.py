from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.jobportal

# Create collections with sample data
users_data = {
    "name": "Sample User",
    "email": "user@example.com",
    "role": "job_seeker"
}

admins_data = {
    "username": "admin",
    "email": "admin@example.com"
}

jobs_data = {
    "title": "Software Developer",
    "company": "Tech Corp",
    "location": "Remote"
}

# Insert sample data
db.users.insert_one(users_data)
db.admins.insert_one(admins_data)
db.jobs.insert_one(jobs_data)

print("jobportal database created successfully!")
print("Refresh MongoDB Compass to see the database.")