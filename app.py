from flask import Flask, jsonify, request
from model import setup_db, User, UserToken
import hashlib
import jwt

app = Flask(__name__)
with app.app_context():
    setup_db(app)


# The next endpoint is for registering (creating an account for) a new user
@app.route("/register", methods=["POST"])
def register():
    data: dict = request.get_json()
    fullname: str = data.get("fullname")
    email: str = data.get("email")
    password: str = data.get("password")
    confirm_password: str = data.get("confirm_password")
    if not (fullname and email and password and confirm_password):
        return "Enter all data", 400

    if password != confirm_password:
        return "the password and confirmation doesn't match", 400

    if User.query.filter(email == email).first():
        return "Email is already Registered", 400

    new_user = User(fullname=fullname, email=email, password=hashlib.sha512(password.encode()).hexdigest())
    new_user.save()
    return "User Registered successfully.", 200


# The next endpoint is used for login
@app.route('/login', methods=["POST"])
def login():
    data: dict = request.get_json()
    email: str = data.get("email")
    password: str = data.get("password")
    if not (email and password):
        return "Enter username and email.", 400

    user = User.query.filter_by(email=email, password=hashlib.sha512(password.encode()).hexdigest()).first()
    if not user:
        return "Wrong username or email.", 404
    else:
        token = jwt.encode({"id": user.id, "email": user.email}, "SecRet")
        user_token = UserToken.query.filter_by(user_email=user.email, token=token).first()
        if user_token:
            user_token.delete()
        UserToken(user_email=user.email, token=token).save()
        return jsonify({
            "token": token
        }), 200


# The next endpoint is used for logout
@app.route('/logout', methods=["POST"])
def logout():
    data: dict = request.get_json()
    if not data.get("token"):
        return "not allowed", 403
    _token = data.get("token")
    decoded_token = jwt.decode(_token, "SecRet", algorithms="HS256")
    user_token = UserToken.query.filter_by(user_email=decoded_token.get("email"), token=_token).first()
    if not user_token:
        return "not allowed", 403
    user_token.delete()
    return "Logged out successfully.", 200


# The next endpoint will receive the poem and analyze it, and return a result.
@app.route('/analyze')
def analyze():
    data: dict = request.get_json()
    if not data.get("token"):
        return "not allowed", 403
    if not data.get("poem"):
        return "provide the poem to analyze it", 403
    # todo: write here the logic to analyze the poem
    #  the poem must be sent on request body along side with the token.

    # todo: when you finish analyzing, send the request back using `return value, 200`
    return data, 200  # replace `data` with the result after analyzing


if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")
