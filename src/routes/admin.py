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
from ..models.children import Children
from ..models.education import Education
from ..models.parser import EntityParser

admin = Blueprint(
    "admin", __name__, template_folder="../templates", static_folder="../static"
)


@admin.route("/")
@admin_required
def index():
    return redirect(url_for("admin.table_personal_information"))
    # return render_template(
    #     "admin/adminDashboard.html",
    #     personal_information_count = personalInformation().count(),
    #     child_count = Children().count(),
    #     education_count = Education().count()
    #     )


# table redirect
@admin.route("/table")
@admin_required
def table():
    return redirect(url_for("admin.table_personal_information"))


@admin.route("/console", methods=["GET", "POST"])
@admin_required
def console():
    if request.method == "POST":
        data = request.get_json()
        sql_query = data.get('sqlQuery')
        try:
            cursor.execute(sql_query)
            db.commit()
            result = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            result_with_columns = [dict(zip(column_names, row)) for row in result]
            return jsonify({"status": "success", "result": result_with_columns}), 200
        except Exception as e:
            db.rollback()
            return jsonify({"error": str(e)}), 500
        
    if request.method == "GET":
        return render_template("admin/adminConsole.html")



# table views


@admin.route("/table/personal_information")
@admin_required
def table_personal_information():
    persons = personalInformation().fetch()
    user_count = personalInformation().count()
    return render_template(
        "admin/adminPersonTable.html", persons=persons, count=user_count
    )

@admin.route("/table/children", methods=['GET', 'POST', 'PATCH'])
@admin_required
def table_children():
    if request.method == 'GET':
        children = Children().fetch()
        count = Children().count()
        print(children)
        return render_template(
            "admin/adminChildrenTable.html", children=children, count=count,
            parent = personalInformation().fetch()
        )
    
    if request.method == 'POST':
        return jsonify({
            "status": "success",
            "persons" : personalInformation().fetch()
        
        }), 200
    
    if request.method == 'PATCH':
        data = request.get_json()
        try:
            Children(
                **data
            ).update(f'Children_ID={data["Children_ID"]}')
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
        return jsonify({
            "status": "success",
        })



@admin.route("/table/education", methods=['GET', 'POST', 'PATCH'])
@admin_required
def table_education():
    if request.method == "GET":
        education = Education().fetch()
        cols_name = EntityParser().get_column_names('education')
        return render_template(
            "admin/adminEducationTable.html", 
            educ=education, cols_name=cols_name, count=Education().count(),
            parent = personalInformation().fetch()
        )
    
    if request.method == 'POST':
        return jsonify({
            "status": "success",
            "education" : Education().fetch()
        
        }), 200
    
    if request.method == 'PATCH':
        data = request.get_json()
        try:
            Education(
                **data
            ).update(f'Education_ID={data["Education_ID"]}')
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
        return jsonify({
            "status": "success",
        })


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

@admin.delete("/delete/<table_name>/")
@admin_required
def delete_user(table_name):
    id = request.get_json().get('deleteIDNo')
    try:
        if table_name == 'personal_information':
            personalInformation().delete(query_condition=f'CSC_ID_No={id}')
        elif table_name == 'children':
            Children().delete(query_condition=f'Children_ID={id}')
        elif table_name == 'education':
            Education().delete(query_condition=f'Education_ID={id}')
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    return jsonify({"status" : "success"}), 200


#adding routes
@admin.route("/add/<table_name>", methods=['POST'])
def admin_add(table_name):
    data = request.get_json()
    user_id = data.get('parentID')
    try:
        if table_name == 'personal_information':
            personalInformation(**data).insert()
        elif table_name == 'children':
            Children(**data).insert(CSC_ID_No=user_id)
        elif table_name == 'education':
            Education(**data).insert()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"status" : "success"}), 200

# test routes
@admin.route("/test")
def test():
    data = request.get_json()


@admin.get("/test2")
def get_all_data():
    datas = []
    
    # Fetch all users
    users = personalInformation().fetch()
    
    for user in users:
        CSC_ID_No = user['cscIdNo']
        
        # Fetch children data for the current user
        children = Children().fetch(query="SELECT * FROM children WHERE CSC_ID_No=%s", query_args=(CSC_ID_No,))
        
        # Fetch education data for the current user
        education_records = Education().fetch(
            query="SELECT * FROM education WHERE CSC_ID_No=%s", 
            query_args=(CSC_ID_No,)
        )
        
        # Initialize dictionary to store education levels
        education = {
            "elementary": [],
            "secondary": [],
            "college": [],
            "graduate_studies": []
        }
        
        user.pop('password', None)
        # Categorize each record based on its educationalLevel
        for record in education_records:
            record['isGraduate'] = record['yearGraduated'] not in (None, "")
            record['educationLevel'] = record['educationLevel'].replace(' ', '_')
            level = record.get("educationLevel")
            if level in education:
                education[level].append(record)
        
        # Combine data for the current user
        user_data = {
            "formData": user,
            "childData": children,
            "educationData": education
        }
        
        # Append combined data to the datas array
        datas.append(user_data)
    
    # Return the combined data as JSON
    return jsonify(datas), 200



        
