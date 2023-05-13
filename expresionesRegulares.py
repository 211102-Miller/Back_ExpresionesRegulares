from flask import Flask, jsonify, request
import pandas as pd
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


dataframe_clientes = pd.read_excel('registros.xlsx', engine='openpyxl')
dataframe_clientes = dataframe_clientes.fillna("")  
clientes = dataframe_clientes.to_dict('records')

def buscar(palabra):
    patron_regex = f"({re.escape(palabra)})"

    patron = re.compile(patron_regex, re.IGNORECASE)

    coincidencias = [cliente for cliente in clientes if any(patron.search(str(valor)) for valor in cliente.values())]

    return coincidencias

@app.route('/buscar/<string:palabra>', methods=['GET'])
def obtener_coincidencias(palabra):

    coincidencias = buscar(palabra)

    return jsonify(coincidencias)


if __name__ == '__main__':
    app.run(debug=True)
