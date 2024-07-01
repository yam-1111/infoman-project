from flask import Blueprint, render_template, url_for, request, jsonify, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector as mysql
from os import getenv
from ..models import cursor, db
from ..models.personUtils import *

user = Blueprint(
    'user', __name__,
    template_folder="../templates",
    static_folder="../static"
)

# db = mysql.connect(
#     host=getenv('DB_HOST'),
#     user=getenv('DB_USERNAME'),
#     password=getenv('DB_PASSWORD'),
#     database=getenv('DB_NAME')
# )  

# cursor = db.cursor()



@user.route('/forms')
def form():
    if session.get('role') == 'user':
        return render_template('user/formParent.html', user_info = session)
    
    return redirect(url_for('apis.login'))

@user.post('/submit')
def submit():
    data = request.get_json()
    email_address = data.get('email_address')

    fields_to_update = {key: value for key, value in fieldToUpdate(data).items() if value is not None}

    set_clause = ", ".join([f"{key} = %s" for key in fields_to_update.keys()])
    params = list(fields_to_update.values())
    params.append(session.get('id'))

    query = f"UPDATE personal_information SET {set_clause} WHERE CSC_ID_No = %s;"
    print(set_clause)
    print(query)
    cursor.execute(query, params)
    db.commit()


    return jsonify({'status': 'success'})



