from flask import Flask, request, jsonify
from database.connect import send_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    
    if request.method == 'GET':
        id_estacao = request.args.get('id_estacao')
        temp = request.args.get('temp')
        luminosidade = request.args.get('luminosidade')
        ultra_violeta = request.args.get('ultra_violeta')
        pressao = request.args.get('pressao') 
        umidade = request.args.get('umidade')
        
        try:
            query = f"INSERT INTO temp_data (id_coletores, temp, luminosidade, ultra_violeta, umidade,pressao) VALUES ('{id_estacao}', '{temp}' ,'{luminosidade}', {ultra_violeta},'{pressao}','{umidade}');"
            send_data(query)
            
            return jsonify({"message": "Data inserted successfully"}), 200
        except Exception as e:
            print(f"Query Executada: {query}")
            print(f"Erro: {str(e)}")
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Unsupported method"}), 405

if __name__ == '__main__':
    app.run(host='187.45.102.198', port=5000)