# utils.py
from functools import wraps
from flask import session, jsonify, abort

def admin_required(f):
    """
    function wrapper for admin routes
    redirect to 403 if user is not an admin checks via session

    Returns:
        function : decorated function with admin lock
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('role') != 'admin':
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


