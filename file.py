from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

file = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["work"]
collection = db ["employee"]

@file.route("/addemp",methods=["POST"])
def postdata():
    data= request.json
    collection.insert_one(data)
    return jsonify({"message" : "done"})

@file.route("/putemp/<_id>",methods=["PUT"])
def putdata (_id):
    data=request.json
    collection.update_one({"_id":ObjectId(_id)},{"$set":data})
    return jsonify({"message": "done"})

@file.route("/getemp/<_id>",methods=["GET"])
def getdata (_id):
    objid=ObjectId(_id)
    data = collection.find_one({"_id":objid})
    data["_id"]=str(data["_id"])
    return jsonify(data)

@file.route("/clearemp/<_id>",methods=["DELETE"])
def deletedata (_id):
    collection.delete_one({"_id":ObjectId(_id)})
    return jsonify({"message":"done"})

if __name__ == "__main__":
    file.run(debug=True)
