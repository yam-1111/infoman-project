from flask import (
    Blueprint,
    render_template,
    url_for,
    session,
    abort,
    redirect,
    jsonify,
    request,
)
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db, cursor

# models
from ..models.person import personalInformation
from ..models.utils import admin_required

admin = Blueprint(
    "admin", __name__, template_folder="../templates", static_folder="../static"
)


@admin.route("/")
@admin_required
def index():
    return render_template("admin/adminDashboard.html")


# table redirect
@admin.route("/table")
@admin_required
def table():
    return redirect(url_for("admin.table_personal_information"))


@admin.route("/console")
@admin_required
def console():
    return redirect(url_for("admin.table_personal_information"))


# table views


@admin.route("/table/personal_information")
@admin_required
def table_personal_information():
    persons = personalInformation().fetch()
    user_count = personalInformation().count()
    return render_template(
        "admin/adminPersonTable.html", persons=persons, count=user_count
    )


@admin.post("/change_password")
@admin_required
def change_password():
    data = request.get_json()
    try:
        personalInformation(
            **{"password": generate_password_hash(data["newPassword"], 'pbkdf2:sha256')}
        ).update(f'CSC_ID_No={data["cscIdNo"]}')
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    return jsonify({"status" : "success"}), 200

# test routes
@admin.route("/test")
def test():
    data = request.get_json()


@admin.route("/test2")
def test2():
    return personalInformation().fetchone(
        query="SELECT * FROM personal_information WHERE Email_Address = %s",
        query_args=(("jd.santos@gmail.com",)),
    )
