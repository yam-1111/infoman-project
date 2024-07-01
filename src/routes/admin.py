from flask import Blueprint, render_template, url_for, session, abort, redirect


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