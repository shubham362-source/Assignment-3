from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import json

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can access backend

# MongoDB connection
MONGO_URI = "mongodb+srv://flask_user:flask_pass123@cluster0.5tuuyga.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["flask_user"]
collection = db["cluster0"]

# GET data from local file or MongoDB
@app.route("/api", methods=["GET"])
def get_data():
    try:
        data = list(collection.find({}, {"_id": 0}))  # Exclude Mongo's _id
        return jsonify(data)
    except Exception as e:
        with open("data.json") as f:
            data = json.load(f)
        return jsonify(data)

# POST data to MongoDB
@app.route("/submit", methods=["POST"])
def submit_data():

    try:
        data = request.json
        collection.insert_one(data)
        return jsonify({"message": "Data submitted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
