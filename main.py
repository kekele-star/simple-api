from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

# create a get route
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Theo Dora",
        "email": "theo.dora@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


# create a post route
@app.route("/create-user", methods=["POST"])
def create_user():
   data = request.ger_json()

   return jsonify(), 201



if __name__ == "__main__":
    app.run(debug=True)