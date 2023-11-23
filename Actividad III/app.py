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
    name = request.args.get('idU')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Uniformes')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    insert = ' INSERT INTO Uniformes(idU, tipo, talla, color, material, precio, surtido, fechaLanzamiento) VALUES(?,?,?,?,?,?,?,?)'
    cursor.execute(insert, [record['idU'], record['tipo'], record['talla'], record['color'], record['material'], record['precio'], record['surtido'], record['fechaLanzamiento']])
    conn.commit()
    conn.close()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE uniformes SET talla = ? WHERE idU= ?'
    cursor.execute(delete, [record['talla'], record['idU']])
    conn.commit()
    conn.close()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Uniformes WHERE idU= ?'
    cursor.execute(delete, [record['idU']])
    conn.commit()
    conn.close()
    return jsonify(record)

if __name__ == '__main__':
  app.run(debug=True)



