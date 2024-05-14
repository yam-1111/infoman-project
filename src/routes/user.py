from flask import Blueprint, render_template, url_for


user = Blueprint(
    'user', __name__
)


@user.route('/')
def index():
    return "Welcome to user page!"