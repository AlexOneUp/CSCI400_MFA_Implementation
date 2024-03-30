import os
import ssl
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import bcrypt
import uuid

load_dotenv()

MONGO_PW = os.getenv("MONGO_PW")
MONGO_USER = os.getenv("MONGO_USER")
MONGO_USER_PW = os.getenv("MONGO_USER_PW")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
CLUSTER_DB = os.getenv("CLUSTER_DB")

client = MongoClient(
    f"mongodb+srv://{MONGO_USER}:{MONGO_USER_PW}@{MONGO_CLUSTER}.wjwidbk.mongodb.net/?retryWrites=true&w=majority",
)

db = client[CLUSTER_DB]
userCollection = db["users"]

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


def create_user(name, password):
    hashed_password = hash_password(password)
    userID = uuid.uuid4().hex
    user = {"_id": userID, "name": name, "password": hashed_password}
    userCollection.insert_one(user)
    return user

def auth_user(name, password):
    print(name, password)
    user = userCollection.find_one({"name": name})

    if user:
        if bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            return user
    return None
