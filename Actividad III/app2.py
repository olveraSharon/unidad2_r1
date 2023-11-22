import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('idP')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Pedidos')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    insert = ' INSERT INTO Pedidos(idP, cliente, fechaPedido, cantidad, total, telefono, direccion, idU) VALUES(?,?,?,?,?,?,?,?)'
    cursor.execute(insert, [record['idP'], record['cliente'], record['fechaPedido'], record['cantidad'], record['total'], record['telefono'], record['direccion'], record['idU']])
    conn.commit()
    conn.close()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE Pedidos SET cantidad = ? WHERE idP= ?'
    cursor.execute(delete, [record['cantidad'], record['idP']])
    conn.commit()
    conn.close()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Pedidos WHERE idP= ?'
    cursor.execute(delete, [record['idP']])
    conn.commit()
    conn.close()
    return jsonify(record)

app.run(debug=True)