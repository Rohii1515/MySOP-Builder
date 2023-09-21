from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient(
    "connection_url"
)
db = client["SOP_Builder"]
users_collection = db["users"]
login_collection = db["logins"]
# User Schema
user_schema = {
    "username": "",
    "email": "",
    "phone_number": "",
    "last_logged_in": None,
    "program": "",
    "university": "",
    "field_interest": "",
    "career_goal": "",
    "subjects_studied": "",
    "projects_internships": "",
    "lacking_skills": "",
    "program_benefits": "",
    "contribution": "",
    "conclusion": "",
}

# Login Schema
login_schema = {
    "name": "",
    "email": "",
    "mobile_number": "",
    "otp": "",
}

# Functions for CRUD operations for users

def create_user(username, email, phone_number):
    user_data = user_schema.copy()
    user_data["username"] = username
    user_data["email"] = email
    user_data["phone_number"] = phone_number
    user_data["last_logged_in"] = datetime.now().strftime("%A,%d %B %Y - %H:%M:%S")
    result = users_collection.insert_one(user_data)
    return result.inserted_id


def get_user_data(username):
    return users_collection.find_one({"username": username})


def update_user(username, data):
    users_collection.update_one({"username": username}, {"$set": data})


def delete_user(username):
    result = users_collection.delete_one({"username": username})
    return result.deleted_count

# Functions for CRUD operations for login

def create_login(name, email, mobile_number, otp):
    login_data = login_schema.copy()
    login_data["name"] = name
    login_data["email"] = email
    login_data["mobile_number"] = mobile_number
    login_data["otp"] = otp
    result = login_collection.insert_one(login_data)
    return result.inserted_id

def get_login_data(mobile_number):
    return login_collection.find_one({"mobile_number": mobile_number})

def update_login(mobile_number, data):
    login_collection.update_one({"mobile_number": mobile_number}, {"$set": data})

def delete_login(mobile_number):
    result = login_collection.delete_one({"mobile_number": mobile_number})
    return result.deleted_count
