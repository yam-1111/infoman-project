from flask import Blueprint, render_template, url_for, session, abort, redirect, jsonify
from ..models import db, cursor
from ..models.person import personalInformation

admin = Blueprint(
    'admin', __name__,
    template_folder="../templates",
    static_folder="../static"
)


@admin.route('/')
def index():
    if session.get('role') == 'admin':
        return render_template('admin/adminParent.html')
    abort(403)

@admin.route('/test')
def test():
   return jsonify(personalInformation().fetch(query_limit=2))

@admin.route('/test2')
def test2():
   return personalInformation().fetchone(
                query="SELECT * FROM personal_information WHERE Email_Address = %s",
                query_args=(('jd.santos@gmail.com',))
            )