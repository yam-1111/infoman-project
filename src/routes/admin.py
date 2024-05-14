from flask import Blueprint, render_template, url_for


admin = Blueprint(
    'admin', __name__
)


@admin.route('/')
def index():
    return "Welcome to admin page!"