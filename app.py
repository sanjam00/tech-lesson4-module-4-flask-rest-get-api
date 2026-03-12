# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# TODO: Define mock data for a list of products
# Example: Each product should have id, name, price, and category

# TODO: Implement a homepage route that returns a JSON welcome message

# TODO: Implement GET /products to return all products or filter by category

# TODO: Implement GET /products/<id> to return a single product by ID

# Mock product data
data = [
	{"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
	{"id": 2, "name": "Book", "price": 14.99, "category": "books"},
	{"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

@app.route("/")
def index():
	#Responds to GET requests at /
	return jsonify({"message": "Welcome to the Product API!", "resource_endpoint": "/products"}), 200

@app.route("/products", methods=["GET"])
def get_products():
	#Responds to GET requests at /products
	# Returns data in JSON format
	# Supports optional query filtering
	category = request.args.get("category")
	if category:
		filtered = [item for item in data if item["category"] == category]
		return jsonify(filtered), 200
	return jsonify(data), 200

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
	for p in data:
		if p["id"] == id:
			return jsonify(p), 200
	return jsonify({"message": "Product not fount"}), 400

if __name__ == "__main__":
	app.run(debug=True)
