from flask import Blueprint
from flask import jsonify

from src.models.modeloregistro import ModeloRegistro

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_registros():
    try:
        registros = ModeloRegistro.get_registros()
        return jsonify(registros)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/<id>')
def get_registro(id):
    try:
        registros = ModeloRegistro.get_registro(id)
        if registros != None:
            return jsonify(registros)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
