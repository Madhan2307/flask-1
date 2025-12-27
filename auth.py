from flask import Flask,request,jsonify
from pymongo import MongoClient

auth = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["Auth"]
collection = db["users"]

@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    existing = collection.find_one({"email": email})
    if existing:
        return jsonify({"message": "User already exists"})
    result = collection.insert_one({
        "email": email,
        "password": password
    })
    return jsonify({
        "message": "User registered successfully",
        "userId": str(result.inserted_id)
    })

@auth.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = collection.find_one({
        "email":email,
        "password":password
    })

    if not user:
        return jsonify({"error": "user not found"})
    return jsonify({
        "message":"user login successful"
    })

if __name__ == "__main__":
    auth.run(debug=True)