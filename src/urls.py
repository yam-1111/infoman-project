
from .routes.user import user
from .routes.admin import admin
from .routes.apis import apis

from .models import create_db
from flask_session import Session


def init_app(app):
    """
    registers the routes page to the app
    """
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(apis, url_prefix='/')

    Session(app)
    create_db()

