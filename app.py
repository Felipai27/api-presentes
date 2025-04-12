from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista inicial de presentes
lista_presentes = []
next_id = 1


# Lista inicial de presentes
lista_presentes = [
    {"id": 1, "nome": "Bicicleta", "preco": 350.0}
]
proximo_id = 2

# Rota para listar todos os presentes
@app.route("/presentes", methods=["GET"])
def listar_presentes():
    return jsonify(lista_presentes)


# Rota para adicionar um novo presente
@app.route("/presentes", methods=["POST"])
def adicionar_presente():
    global proximo_id
    dados = request.get_json()
    presente = {
        "id": proximo_id,
        "nome": dados["nome"],
        "preco": dados["preco"]
    }
    lista_presentes.append(presente)
    proximo_id += 1
    return jsonify(presente), 201

# Buscar um presente pelo ID
@app.route("/presentes/<int:id_presente>", methods=["GET"])
def buscar_presente_por_id(id_presente):
    for presente in lista_presentes:
        if presente["id"] == id_presente:
            return jsonify(presente)
    return jsonify({"erro": "Presente não encontrado"}), 404


# Atualizar um presente existente
@app.route("/presentes/<int:id_presente>", methods=["PUT"])
def atualizar_presente(id_presente):
    dados = request.get_json()
    for presente in lista_presentes:
        if presente["id"] == id_presente:
            presente["nome"] = dados.get("nome", presente["nome"])
            presente["preco"] = dados.get("preco", presente["preco"])
            return jsonify(presente)
    return jsonify({"erro": "Presente não encontrado"}), 404


# Remover um presente
@app.route("/presentes/<int:id_presente>", methods=["DELETE"])
def remover_presente(id_presente):
    for presente in lista_presentes:
        if presente["id"] == id_presente:
            lista_presentes.remove(presente)
            return jsonify({"mensagem": "Presente removido com sucesso"})
    return jsonify({"erro": "Presente não encontrado"}), 404



if __name__ == "__main__":
    app.run(debug=True)