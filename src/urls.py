
from .routes.user import user
from .routes.admin import admin
from .routes.apis import apis


def init_app(app):
    """
    registers the routes page to the app
    """
    app.register_blueprint(user, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(apis, url_prefix='/api')

