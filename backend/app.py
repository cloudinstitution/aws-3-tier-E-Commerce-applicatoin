from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow requests from the frontend
CORS(app)

products = [

    {
        "id": 1,
        "name": "Dell Laptop",
        "description": "Intel i7 | 16GB RAM | 512GB SSD",
        "price": 75000,
        "image": "https://picsum.photos/400/300?random=1"
    },

    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "description": "RGB Mechanical Keyboard",
        "price": 2500,
        "image": "https://picsum.photos/400/300?random=2"
    },

    {
        "id": 3,
        "name": "Wireless Mouse",
        "description": "Bluetooth Mouse",
        "price": 1200,
        "image": "https://picsum.photos/400/300?random=3"
    },

    {
        "id": 4,
        "name": "Gaming Monitor",
        "description": "27-inch Full HD Monitor",
        "price": 18500,
        "image": "https://picsum.photos/400/300?random=4"
    }

]


@app.route("/")
def home():

    return {
        "message": "Backend API is Running"
    }


@app.route("/products")
def get_products():

    return jsonify(products)


@app.route("/health")
def health():

    return {
        "status": "UP"
    }


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
