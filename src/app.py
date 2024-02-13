from flask import Flask

from src.config import config
from keras.models import load_model
# Routes
from src.routes import routeregistro

app = Flask(__name__)

model = load_model('D:/Dev/Python/Rest-api-flask/src/modeloInceptionV3.h5')
def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(routeregistro.main, url_prefix='/api/registros')
    # error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
