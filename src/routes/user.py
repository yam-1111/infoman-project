from flask import Blueprint, render_template, url_for, request, jsonify, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector as mysql
from os import getenv
from ..models import cursor, db

#utils
from ..models.personUtils import *
from ..models.person import personalInformation

user = Blueprint(
    'user', __name__,
    template_folder="../templates",
    static_folder="../static"
)


@user.route('/forms')
def form():
    if session.get('role') == 'user':
        return render_template('user/formParent.html', user_info = session)
    
    return redirect(url_for('apis.login'))

@user.post('/submit')
def submit():
    data = request.get_json()
    personalInformation(**data['formData']).update(f"CSC_ID_No = {session['id']}")


    return jsonify({'status': 'success'})



