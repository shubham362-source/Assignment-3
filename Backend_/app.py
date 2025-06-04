from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB Atlas connection
client = MongoClient('mongodb+srv://flask_user:flask_pass123@cluster0.5tuuyga.mongodb.net/')
db = client['flask_user']
collection = db['cluster0']

@app.route('/api', methods=['GET'])
def get_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        data = request.json
        collection.insert_one(data)
        return jsonify({'message': 'Data submitted successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
