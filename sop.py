import streamlit as st
import random
from pymongo import MongoClient
from datetime import datetime
import database

# Connect to MongoDB
client = MongoClient("connection_url")
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


#####################################################################################################################################################33
# Function to validate word limits
def validate_word_limits(text, min_words, max_words):
    word_count = len(text.split())
    if word_count < min_words:
        st.error(f"Minimum {min_words} words required.")
        return False
    elif word_count > max_words:
        st.error(f"Maximum {max_words} words allowed.")
        return False
    return True


# Generate a random OTP
def generate_otp():
    return str(random.randint(1000, 9999))


# st.title("Welcome to the Statement of Purpose Generator")
st.markdown(
    "<h1 style='text-align: center; color: #80ed99;'>Welcome to the Statement of Purpose Generator</h1>",
    unsafe_allow_html=True,
)
# st.markdown(
#     "<h2 style='text-align: center; color: #ade8f4;'>user login</h2>",
#     unsafe_allow_html=True,
# )


def signup_or_login():
    show_signup = st.checkbox("Signup")
    show_login = st.checkbox("Login")

    if show_signup:
        st.header("Signup")
        username = st.text_input("Name")
        email = st.text_input("Email")
        phone_number = st.text_input("Mobile Number")
        
        st.markdown(
            "<h1 style='text-align: center; color: #c8b6ff;'>SOP Generate</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h6 style='text-align: center; color: #fcf6bd;'>answer in minimum of 50 words and a maximum of 200 words.</h6>",
            unsafe_allow_html=True,
        )
        program = st.text_area("Which program is this SOP for? ")
        university = st.text_area("Which university is this SOP for?")
        field_interest = st.text_area("How did you become interested in this field? Describe an instance that made you interested in the field or a sequence of events that made you interested in the field.")
        career_goal = st.text_area("What is your career goal? And why did you choose this as your goal?")
        subjects_studied = st.text_area("What subjects have you studied so far that have made you competent in your area of interest? What relevant skills, knowledge pieces have you learnt from these subjects? When and where did you study these subjects? ")
        projects_internships = st.text_area("What projects, internships, research work have you done so far to achieve your career goals and how have these helped you get closer to achieving your career goals? Quantify the outcomes / achievements from these projects if any. OR Resume.")
        lacking_skills = st.text_area("What specific skills / knowledge do you currently lack which are needed for you to achieve your career goals? These should be skills / knowledge that you don’t currently have.")
        program_benefits = st.text_area("What specific skills / knowledge will the master's program give you which will help you achieve your career goal? Elaborate based on courses, research work, networking events and other relevant activities at the university.")
        contribution = st.text_area("How will you contribute to the university based on your knowledge, experience? Cite specific things you can do to strengthen your peer’s learning, classroom discussion and how you can contribute to the student community at college.")

        if st.button("Signup"):
            if (
                validate_word_limits(program, 50, 200)
                and validate_word_limits(university, 50, 200)
                and validate_word_limits(field_interest, 50, 200)
                and validate_word_limits(career_goal, 50, 200)
                and validate_word_limits(subjects_studied, 50, 200)
                and validate_word_limits(projects_internships, 50, 200)
                and validate_word_limits(lacking_skills, 50, 200)
                and validate_word_limits(program_benefits, 50, 200)
                and validate_word_limits(contribution, 50, 200)
            ):
                # Generate and send OTP (you can replace this with your actual OTP sending logic)
                otp = generate_otp()
                st.write(f"An OTP has been sent to {phone_number}: {otp}")
                # Store user data for verification
                # create_user(username, email, phone_number)
                user_data = user_schema.copy()
                user_data["username"] = username
                user_data["email"] = email
                user_data["phone_number"] = phone_number
                user_data["program"] = program
                user_data["university"] = university
                user_data["field_interest"] = field_interest
                user_data["career_goal"] = career_goal
                user_data["subjects_studied"] = subjects_studied
                user_data["projects_internships"] = projects_internships
                user_data["lacking_skills"] = lacking_skills
                user_data["program_benefits"] = program_benefits
                user_data["contribution"] = contribution
                user_data["last_logged_in"] = datetime.now().strftime("%A, %d %B %Y - %H:%M:%S")
                # Check if the user already exists
                existing_user = get_user_data(username)
                if existing_user==username:
                    if existing_user:
                        # Update the user's data with new information
                        new_data = {
                            "program" : program,
                            "university" : university,
                            "field_interest" : field_interest,
                            "career_goal" : career_goal,
                            "subjects_studied" : subjects_studied,
                            "projects_internships" : projects_internships,
                            "lacking_skills" : lacking_skills,
                            "program_benefits" : program_benefits,
                            "contribution" : contribution,
                            "last_logged_in" : datetime.now().strftime("%A, %d %B %Y - %H:%M:%S")
                        }
                        update_user(username, new_data)
                else:
                    # Insert a new user document
                    users_collection.insert_one(user_data)

    if show_login:
        # ... Your login form code here ...
        st.header("Login")
        user_Moble = st.text_input("Mobile Number")
        otp = st.text_input("OTP")

        if st.button("Login"):
            # Validate and process login data here
            pass  # Add your login logic here


#         if st.button("Signup"):
#             if (
#                 validate_word_limits(program, 50, 200)
#                 and validate_word_limits(university, 50, 200)
#                 and validate_word_limits(field_interest, 50, 200)
#                 and validate_word_limits(career_goal, 50, 200)
#                 and validate_word_limits(subjects_studied, 50, 200)
#                 and validate_word_limits(projects_internships, 50, 200)
#                 and validate_word_limits(lacking_skills, 50, 200)
#                 and validate_word_limits(program_benefits, 50, 200)
#                 and validate_word_limits(contribution, 50, 200)
#             ):
#                 # Generate and send OTP (you can replace this with your actual OTP sending logic)
#                 otp = generate_otp()
#                 st.write(f"An OTP has been sent to {mobile_number}: {otp}")

#                 # Store user data for verification
#                 user_data = user_schema.copy()
#                 user_data["username"] = name
#                 user_data["email"] = email
#                 user_data["phone_number"] = mobile_number
#                 user_data["program"] = program
#                 user_data["university"] = university
#                 user_data["field_interest"] = field_interest
#                 user_data["career_goal"] = career_goal
#                 user_data["subjects_studied"] = subjects_studied
#                 user_data["projects_internships"] = projects_internships
#                 user_data["lacking_skills"] = lacking_skills
#                 user_data["program_benefits"] = program_benefits
#                 user_data["contribution"] = contribution
#                 user_data["last_logged_in"] = datetime.now().strftime(
#                     "%A, %d %B %Y - %H:%M:%S"
#                 )

#             # Check if the user already exists
#             existing_user = users_collection.find_one({"phone_number": mobile_number})
#             if existing_user:
#                 # Update existing user data with a new OTP and last_logged_in timestamp
#                 existing_user["otp"] = otp
#                 existing_user["last_logged_in"] = user_data["last_logged_in"]
#                 users_collection.update_one(
#                     {"phone_number": mobile_number}, {"$set": existing_user}
#                 )
#             else:
#                 # Insert a new user document
#                 users_collection.insert_one(user_data)

#     elif page == "Login":
#         st.header("Login")
#         mobile_number = st.text_input("Mobile Number")
#         otp = st.text_input("OTP")

#         if st.button("Login"):
#             # Verify OTP and retrieve user data
#             user = users_collection.find_one(
#                 {"phone_number": mobile_number, "otp": otp}
#             )
#             if user:
#                 # Update last_logged_in timestamp
#                 user["last_logged_in"] = datetime.now().strftime(
#                     "%A, %d %B %Y - %H:%M:%S"
#                 )
#                 users_collection.update_one(
#                     {"phone_number": mobile_number}, {"$set": user}
#                 )
#                 st.write(f"Welcome, {user.get('username')}!")
#             else:
#                 st.write(
#                     "Invalid credentials. Please check your mobile number and OTP."
#                 )


if __name__ == "__main__":
    signup_or_login()
