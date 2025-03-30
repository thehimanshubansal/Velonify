from fastapi import FastAPI, HTTPException
from models import User
from db import users_collection, disaster_collection
from send_emails import send_email

app = FastAPI()

# ✅ SIGNUP ROUTE
@app.post("/signup")
def signup(user: User):
    existing_user = users_collection.find_one({"email": user.email.lower()})

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user_data = {
        "username": user.username,
        "email": user.email.lower(),
        "password": user.password,
        "city": user.city,
        "state": user.state,
        "country": user.country
    }

    users_collection.insert_one(user_data)
    return {"message": "User registered successfully!"}

# ✅ LOGIN ROUTE + DISASTER ALERT
@app.post("/login")
def login(email: str, password: str):
    # Case-insensitive login check
    user = users_collection.find_one({"email": email.lower()})

    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # # 🔥 Fetch disasters' location in user's country
    # disasters = list(disaster_collection.find({"Region": user["city"]}))
    # print(disasters)
    # if disasters:
    #     # 🔥 Send alert emails to all users in the same country
    #     users_in_city = list(users_collection.find({"city": user["city"]}))
    #     print(users_in_city)
    #     for disaster in disasters:
    #         for u in users_in_city:
    #             send_email(
    #                 to_email=u["email"],
    #                 subject=f"🚨 Disaster Alert in {u['city']}",
    #                 message=f"""
    #                 Title: {disaster['Title']}
    #                 URL: {disaster['URL']}
    #                 Published At: {disaster['Published At']}
    #                 """
    #             )

    return {"message": "Logged in successfully and alerts sent!"}
