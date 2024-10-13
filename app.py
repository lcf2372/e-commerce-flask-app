from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://c0917578:WfirtDrDqOYSLyhB@cluster0.aagh5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['shop_db']
products_collection = db['products']

# Insert mock data into the products collection
mock_data = [
    {
        "name": "Laptop",
        "tag": "Electronics",
        "price": 899.99,
        "image_path": "images/laptop.jpg"
    },
    {
        "name": "Headphones",
        "tag": "Electronics",
        "price": 199.99,
        "image_path": "images/headphones.jpg"
    }
]

# Insert mock data into MongoDB
# products_collection.insert_many(mock_data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
