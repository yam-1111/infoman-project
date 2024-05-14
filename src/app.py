from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv('.env')

def config_app():
    app = Flask(__name__)

    return app
