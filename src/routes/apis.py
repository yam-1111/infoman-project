from flask import Blueprint, render_template, url_for


apis = Blueprint(
    'apis', __name__
)


@apis.route('/')
def index():
    return "Welcome to apis page!"