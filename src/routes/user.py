from flask import Blueprint, render_template, url_for


user = Blueprint(
    'user', __name__,
    template_folder="../templates",
    static_folder="../static"
)


@user.route('/')
def index():
    return render_template('user/loginParent.html')

@user.route('/forms')
def form():
    return render_template('user/formParent.html')
