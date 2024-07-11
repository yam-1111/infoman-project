from flask import Blueprint, render_template, url_for, request, jsonify, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector as mysql
from os import getenv
from ..models import cursor, db

#utils
from ..models.personUtils import *
from ..models.person import personalInformation
from ..models.children import Children
from ..models.education import Education

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
    csc_id_no = session['id']

    # Update or insert personal information
    if 'formData' in data and data['formData']:
        person = personalInformation()
        existing_person = person.fetchone(query_args=(csc_id_no,))
        
        if existing_person:
            # Update the existing record
            personalInformation(**data.get('formData')).update(f"CSC_ID_No = {csc_id_no}")
        else:
            # Insert a new record
            person(**data.get('formData'))
            person.insert()

    # Insert each child in the database
    if 'childData' in data and data['childData']:
        for child in data['childData']:
            child_record = Children()
            try:
                existing_child = child_record.fetchone(
                    query='SELECT * FROM children WHERE Children_ID = %s', 
                    query_args=(child.get('Children_ID'),)
                    )
                print(f"-------\nchild id: {child.get('Children_ID')}\nExisting : {existing_child}\n\n-------")
            except Exception as e:
                print(f"-------\n{str(e)}\n-------")
                existing_child = None
                
            if existing_child:
                # Update existing child record
                print(child)
                Children(**child).update(f"Children_ID = {child.get('Children_ID')}")
            else:
                # Insert a new child record
                print(child)
                child['CSC_ID_No'] = csc_id_no
                new_child = Children(**child)
                new_child.insert(CSC_ID_No=csc_id_no)

    # Insert each education in the database
    if 'educationData' in data and data['educationData']:
        for educationLevel, educationValue in data['educationData'].items():
            for arr in educationValue:
                print(f"+++++++\n{arr}\n+++++++")
                arr['educationLevel'] = (arr.get('educationLevel')).replace('_', ' ')
                education_record = Education()
                try:
                    existing_education = education_record.fetchone(
                    query='SELECT * FROM education WHERE CSC_ID_No = %s AND  Education_ID = %s', 
                    query_args=(
                        (arr.get('CSC_ID_No'), arr.get('Education_ID'))
                        )
                    )
                except Exception as e:
                    print(f"-------\n{str(e)}\n-------")
                    existing_education = None
                    
                print(f"-------\nExisting : {existing_education}\n\n-------")
                if existing_education:
                    # Update existing education record
            
                    update_education = Education(**arr)
                    update_education.update(
                        query_condition=f"CSC_ID_No = {session.get('id')} AND Education_ID = {arr.get('Education_ID')}"
                        )
                else:
                    # Insert a new education record
                    arr['CSC_ID_No'] = session.get('id')
                    new_education = Education(**arr)
                    new_education.insert()

    return jsonify({'status': 'success'})



