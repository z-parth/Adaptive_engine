from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

client = MongoClient(
    os.getenv("MONGODB_URI"),
    tlsCAFile=certifi.where()
)
db = client["adaptive_engine"]

questions_collection = db["questions"]
sessions_collection = db["sessions"]