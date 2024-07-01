from flask import Blueprint, render_template, url_for, request, jsonify, redirect, session, abort
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector as mysql
from os import getenv
from ..models import cursor, db

#utils
from ..models.personUtils import * 

apis = Blueprint(
    'apis', __name__,
    template_folder="../templates",
    static_folder="../static"
)


    
# login
@apis.route('/')
def index():
    return redirect(url_for('apis.login'))

@apis.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('user/login/login.html')
    if request.method == 'POST':
        data = request.get_json()
        print(data['email_address'])
        # Check if the user exists in the database
        try:
            # check if the user is the admin
            if data['email_address'] == getenv('ADMIN_EMAIL') and data['password'] == getenv('ADMIN_PASSWORD'):
                print('goes here')
                session['role'] = 'admin'
                return redirect(url_for('admin.index'))

            # check if the user is in the personal_information table
            select_query = """
                SELECT * FROM personal_information WHERE Email_Address = %s
            """
            cursor.execute(select_query, (data['email_address'],))
            user = cursor.fetchone()
            print(user)
            if not user:
                return jsonify({'error': 'User does not exist'}), 418
            
            # Check if the password is correct
            if not check_password_hash(user[-1], data['password']):
                return jsonify({'error': 'Invalid password'}), 418
            
            #redirect to the forms page
            session['name'], session['id'], session['role'] = user[1], user[0], 'user'
            return redirect(url_for('user.form'))
            
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'error': str(e)}), 418
        

#signup
@apis.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('user/login/signup.html')
    
    if request.method == 'POST':
        data = request.get_json()
        print(data['fullName'])
        hash_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

        # Insert the data into the database
        try:
            # check if the email is already in the personal_infomation table
            select_query = """
                SELECT * FROM personal_information WHERE 
                Email_Address = %s OR
                Date_Of_Birth = %s
                """
            cursor.execute(select_query, (data['email_address'], data['dateOfBirth']))

            # check if the exist or reserved to admin
            if(cursor.fetchall()) or (data['email_address'] == getenv('ADMIN_EMAIL')):
                return jsonify({'error': 'User already exists'}), 418
            
            # add entry to the personal_information table if there is no user with the same email and date of birth
            insert_query = """
                INSERT INTO personal_information (Full_Name, Date_Of_Birth, Email_Address, password)
                VALUES (%s, %s, %s, %s)
            """
            insert_values = (data['fullName'], data['dateOfBirth'], data['email_address'], hash_password)
            cursor.execute(insert_query, insert_values)
            db.commit()
            
        except Exception as e:
            print(f"Error: {e}")  # Print the error for debugging
            return jsonify({'error': str(e)}), 418
        
        return jsonify({'status' : 'success'}), 200
    

#logout
@apis.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('apis.login'))


# retrieve the user's information
@apis.get('/user/data')
def get_user():
    if session.get('role') == 'user':
        select_query = """
            SELECT * FROM personal_information WHERE CSC_ID_No = %s
        """
        cursor.execute(select_query, (session.get('id'),))
        user = cursor.fetchone()
        return jsonify(personInformation('success', user)), 200
    return abort(418)

# forgot password
@apis.route('/retrieve', methods=['GET', 'PUT'])
def forgotPassword():
    if request.method == 'GET':
        return render_template('user/login/forgotpw.html')
    
    if request.method == 'PUT':
        data = request.get_json()
        # retrieve the information
        cursor.execute("SELECT * FROM personal_information WHERE Email_Address = %s AND Date_Of_Birth = %s", 
        (data['email_address'], data['dataOfBirth']))
        user = cursor.fetchone()
        print(user is None)
        if user is None:
            return jsonify({'error': 'User does not exist with the email nor date of birth'}), 404
        
        # update the password
        if check_password_hash(user[-1], data['password']):
            return jsonify({'error': 'New password cannot be the same as the old password'}), 418
        
        hash_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        cursor.execute("UPDATE personal_information SET password = %s WHERE CSC_ID_No= %s", (hash_password, user[0]))
        return jsonify({'status': 'success'})

    
