from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para buscar os endereços no banco de dados
def buscar_enderecos(termo):
    conn = sqlite3.connect("enderecos.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT endereco FROM enderecos WHERE endereco LIKE ?", ('%' + termo + '%',))
    resultados = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    return resultados

# Rota para pesquisa
@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('q', '')
    resultados = buscar_enderecos(termo)
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
