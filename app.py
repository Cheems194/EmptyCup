from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app=Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/EmptyCup"
db=PyMongo(app).db

@app.route("/")
def index():
    cards=db.DesignerCards.find({})
    return render_template("index.html",cards=cards)

@app.route("/shortlisted")
def shortlisted():
    cards=db.DesignerCards.find({"shortlisted":"True"})
    return render_template("index.html",cards=cards)


@app.route("/update-card/<id>", methods=["PATCH"])
def update_card(id):
    try:
        data = request.get_json()
        result = db.DesignerCards.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        if result.modified_count > 0:
            return jsonify({"message": "Card updated"}), 200
        else:
            return jsonify({"message": "No change made"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__=="__main__":
    app.run(debug=True)