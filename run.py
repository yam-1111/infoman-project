from src.app import config_app
from src import urls

app,db = config_app()
urls.init_app(app)

if __name__ == '__main__':
    app.run(debug = True)