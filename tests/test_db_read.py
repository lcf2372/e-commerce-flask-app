from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pytest

# Load environment variables
load_dotenv()

# Retrieve MongoDB credentials
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

def test_mongodb_connection():
    """
    Test MongoDB connection by pinging the database.
    Purpose: Ensures the application can successfully connect to MongoDB.
    """
    client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.ubgogus.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    try:
        client.admin.command('ping')  # Pinging the MongoDB server
        assert True  # Connection succeeded
    except Exception:
        assert False, "MongoDB connection failed"
