from flask import Flask, request, jsonify, redirect
from flask_swagger_ui import get_swaggerui_blueprint


# Inicializa a aplicação Flask com pasta estática
app = Flask(__name__, static_folder="static")

# Configuração do Swagger UI
SWAGGER_URL = "/docs"
API_URL = "/static/openapi.yaml"
swaggerui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "API de Presentes"}
)
app.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)

# Dados em memória
lista_presentes = [
    {"id": 1, "nome": "Bicicleta", "preco": 350.0}
]
proximo_id = 2


@app.route("/")
def raiz():
    return redirect(SWAGGER_URL + "/")


# Listar presentes
@app.route("/presentes", methods=["GET"])
def listar_presentes():
    return jsonify(lista_presentes)

# Adicionar novo presente
@app.route("/presentes", methods=["POST"])
def adicionar_presente():
    global proximo_id
    dados = request.get_json()
    presente = {
        "id": proximo_id,
        "nome": dados.get("nome"),
        "preco": dados.get("preco")
    }
    lista_presentes.append(presente)
    proximo_id += 1
    return jsonify(presente), 201

# Buscar presente por ID
@app.route("/presentes/<int:id_presente>", methods=["GET"])
def buscar_presente_por_id(id_presente):
    for presente in lista_presentes:
        if presente["id"] == id_presente:
            return jsonify(presente)
    return jsonify({"erro": "Presente não encontrado"}), 404

# Atualizar presente
@app.route("/presentes/<int:id_presente>", methods=["PUT"])
def atualizar_presente(id_presente):
    dados = request.get_json()
    for presente in lista_presentes:
        if presente["id"] == id_presente:
            presente["nome"] = dados.get("nome", presente["nome"])
            presente["preco"] = dados.get("preco", presente["preco"])
            return jsonify(presente)
    return jsonify({"erro": "Presente não encontrado"}), 404

# Remover presente
@app.route("/presentes/<int:id_presente>", methods=["DELETE"])
def remover_presente(id_presente):
    for presente in lista_presentes:
        if presente["id"] == id_presente:
            lista_presentes.remove(presente)
            return jsonify({"mensagem": "Presente removido com sucesso"})
    return jsonify({"erro": "Presente não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
