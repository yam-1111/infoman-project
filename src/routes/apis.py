from flask import (
    Blueprint,
    render_template,
    url_for,
    request,
    jsonify,
    redirect,
    session,
    abort,
)
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector as mysql
from os import getenv
from ..models import cursor, db

# utils
from ..models.personUtils import *
from ..models.person import personalInformation

apis = Blueprint(
    "apis", __name__, template_folder="../templates", static_folder="../static"
)


# login
@apis.route("/")
def index():
    return redirect(url_for("apis.login"))


@apis.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("user/login/login.html")
    if request.method == "POST":
        data = request.get_json()
        print(data["email_address"])
        # Check if the user exists in the database
        try:
            # check if the user is the admin
            if data["email_address"] == getenv("ADMIN_EMAIL") and data[
                "password"
            ] == getenv("ADMIN_PASSWORD"):
                print("goes here")
                session["role"], session['name'] = ("admin", "admin")
                return jsonify({key: value for key, value in session.items()}), 200

            # check if the user is in the personal_information table
            user = personalInformation().fetchone(
                query="SELECT * FROM personal_information WHERE Email_Address = %s",
                query_args=(data["email_address"],),
            )
            print(check_password_hash(user["password"], data["password"]))
            if user == {}:
                return jsonify({"error": "User does not exist"}), 404

            elif not check_password_hash(user["password"], data["password"]):
                return jsonify({"error": "Invalid password"}), 403

            # redirect to the forms page
            session["name"], session["id"], session["role"] = (
                user["fullName"],
                user["cscIdNo"],
                "user",
            )
            return jsonify({key: value for key, value in session.items()}), 200
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": str(e)}), 418


# signup
@apis.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "GET":
        return render_template("user/login/signup.html")

    if request.method == "POST":
        data = request.get_json()
        plain_password = data["password"]
        data["password"] = generate_password_hash(
            plain_password, method="pbkdf2:sha256"
        )
        print(data)
        try:
            if (
                personalInformation().fetchone(
                    query="SELECT * FROM personal_information WHERE Email_Address = %s AND Date_Of_Birth = %s",
                    query_args=(data["email_address"], data["dateOfBirth"]),
                )
            ) or data["email_address"] == getenv("ADMIN_EMAIL"):
                return jsonify({"error": "User already exists"}), 418

            personalInformation(**data).insert()
            return jsonify({"status": "success"}), 200
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": str(e)}), 418


# logout
@apis.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("apis.login"))


# retrieve the user's information
@apis.get("/user/data")
def get_user():
    if session.get("role") == "user":
        user = personalInformation().fetchone(query_args=(session.get("id"),))
        print(user)
        return jsonify({"status": "success", "formData": user}), 200
    return abort(418)


# forgot password
# TODO: Implement the forgot password bug


@apis.route("/retrieve", methods=["GET", "PUT"])
def forgotPassword():
    if request.method == "GET":
        return render_template("user/login/forgotpw.html")

    if request.method == "PUT":
        data = request.get_json()
        try:
            user = personalInformation.fetchone(
                "SELECT * FROM personal_information WHERE Email_Address = %s AND Date_Of_Birth = %s",
                ("jd.santos@gmail.com", "1995-01-01"),
            )

        except Exception as e:
            return jsonify({"error": str(e)}), 418
        print(f"{data}\n\nUser: {user}\n\n")
        # retrieve the information
        # user = personalInformation.fetchone(
        #     "SELECT * FROM personal_information WHERE Email_Address = %s AND Date_Of_Birth = %s",
        #     (data["email_address"], data["dataOfBirth"]),
        # )

        # if user == {}:
        #     return (
        #         jsonify(
        #             {"error": "User does not exist with the email nor date of birth"}
        #         ),
        #         404,
        #     )

        # # update the password
        # if check_password_hash(user[-1], data["password"]):
        #     return (
        #         jsonify(
        #             {"error": "New password cannot be the same as the old password"}
        #         ),
        #         418,
        #     )
        # personalInformation(
        #     **{
        #         "password": generate_password_hash(
        #             data["password"], method="pbkdf2:sha256"
        #         )
        #     }
        # ).update("CSC_ID_No = %s", (user["CSC_ID_No"],))
        return jsonify({"status": "fail"})
