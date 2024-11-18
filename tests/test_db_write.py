from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pytest

# Load environment variables
load_dotenv()

# Retrieve MongoDB credentials
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

def test_insert_document():
    """
    Test inserting a document into MongoDB.
    Purpose: Ensures the application can successfully write to the database.
    """
    client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.aagh5.mongodb.net/?retryWrites=true&w=majority")
    db = client['shop_db']
    collection = db['products']

    # Insert test document
    new_data = {"name": "Test Product", "tag": "Test", "price": 9.99}
    collection.insert_one(new_data)

    # Query the document
    inserted_data = collection.find_one({"name": "Test Product"})
    assert inserted_data is not None
    assert inserted_data['name'] == "Test Product"

    # Cleanup
    collection.delete_one({"name": "Test Product"})
