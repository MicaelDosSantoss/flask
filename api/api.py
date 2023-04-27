from flask import Flask, jsonify, request

# Flask é uma biblioteca que oferece uma estrutura web
#Jsonify serve para retornar uma resposta HTTP
#request usado par requisitar uma solicitação HTTP

app = Flask(__name__) #Através desse app poderei criar as minhas rotas

usuarios = [
    {
        'id': 1,
        'nome': 'Micael',
        'idade': 18,
        'Sexo': 'M'
    },
    {
        'id': 2,
        'nome': 'Ana',
        'idade': 14,
        'Sexo': 'F'
    },

    {
        'id': 3,
        'nome': 'Ana Paula',
        'idade': 41,
        'Sexo': 'F'
    }
]

# GET

@app.route('/usuarios', methods=['GET']) # Rotas com o Python / essa rota Pega todos dos usuarios

def obter_usuarios():
    return jsonify(usuarios)

#GET por id

@app.route('/usuarios/<int:id>', methods=['GET']) # Essa rota pega o usuario por id
def obter_usuario_por_id(id):
    for usuario in usuarios:
        if usuario.get('id') == id:
            return jsonify(usuario)

#Editar por ID

@app.route('/usuarios/<int:id>',methods=['PUT']) # Essa rota atualiza o usuario 

def editar_usuario_por_id(id):
    usuario_alterado = request.get_json()
    
    for indice,livro in enumerate(usuarios): # o enumerate vai númerar os itens. Ex. (0{...}), (1{...})
        if livro.get('id') == id:
            usuarios[indice].update(usuario_alterado)
            return jsonify(usuarios[indice])

#Criar Usuario

@app.route('/usuarios',methods=['POST']) # rota para a criação de novos usuarios
def novo_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)

    return jsonify(usuarios)

# Deletar usuario

@app.route('/usuarios/<int:id>',methods=['DELETE']) # rota para deletar usuario por ID
def excluir_usuario(id):
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            del usuarios[indice]



app.run(port=5000,host='localhost',debug=True) # Aqui e onde eu irei rodar o meu servidor, a porta dela será 5000, o lugar de hospertar é o meu pc, o localhost