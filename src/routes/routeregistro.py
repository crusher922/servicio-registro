from io import BytesIO

import numpy as np
from flask import Blueprint
from flask import jsonify, request

import uuid

from keras.models import load_model
from keras.preprocessing import image

from src.models.modeloregistro import ModeloRegistro
from src.models.entities.registro import Registro

main = Blueprint('registro_blueprint', __name__)
model = load_model('D:/Dev/Python/Rest-api-flask/src/modeloInceptionV3.h5')

@main.route('/')
def get_registros():
    try:
        registros = ModeloRegistro.get_registros()
        return jsonify(registros)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_registro(id):
    try:
        registros = ModeloRegistro.get_registro(id)
        if registros != None:
            return jsonify(registros)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_registro():
    try:
        if request.method == 'POST':
            if request.content_type == 'application/json':
                data = request.json
            else:
                data = request.form

            id_paciente = data.get('id_paciente')
            id_medico = data.get('id_medico')
            img = request.files['image']
            preprocessed_image = preprocess_image(img)

            predictions = model.predict(np.expand_dims(preprocessed_image, axis=0))

            class_names = ['result_tb', 'result_no_tb', 'result_normal']

            results = {
                class_names[i]: float(predictions[0][i]) for i in range(len(class_names))
            }
            result_tb = results['result_tb']
            result_no_tb = results['result_no_tb']
            result_normal = results['result_normal']
            print(result_normal)
            registro = Registro(id_paciente, id_medico, float(result_tb), float(result_no_tb), float(result_normal))

            ModeloRegistro.add_registro(registro)
            print(data)
            return jsonify(results)
        else:
            return jsonify({'message': 'Unsupported method'}), 405
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

def preprocess_image(img):
    img_stream = BytesIO(img.read())

    img = image.load_img(img_stream, target_size=(300, 300))

    img_array = image.img_to_array(img)

    img_array /= 255.0
    return img_array
