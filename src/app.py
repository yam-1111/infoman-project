from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv('.env')

db = SQLAlchemy()
def config_app():
    app = Flask(__name__)
    print(f'Detected : {os.getenv('DATABASE_URI')}')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional but recommended
    db.init_app(app)

    return app, db
