from pymongo import MongoClient

MONGODB_USERNAME = "pabinesh1998"  # Replace with your username
MONGODB_PASSWORD = "o8ubrWOGUCKQYgei"  # Replace with your password

uri = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.ubgogus.mongodb.net/test"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
