from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# App Initialization
app = Flask(__name__)

# Connect to MongoDB Atlas
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

client = MongoClient(
    f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.ubgogus.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
)
db = client['shop_db']
products_collection = db['products']

# Insert mock data only if the collection is empty
if products_collection.count_documents({}) == 0:
    mock_data = [
        {
            "name": "Laptop",
            "tag": "Electronics",
            "price": 899.99,
            "image_path": "images/laptop.jpg",
        },
        {
            "name": "Headphones",
            "tag": "Electronics",
            "price": 199.99,
            "image_path": "images/headphones.jpg",
        },
    ]
    products_collection.insert_many(mock_data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
