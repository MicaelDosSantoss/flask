from flask import Flask, render_template
from lista.lista import usuarios

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home/index.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro/cadastro.html")

@app.route('/lista')
def lista():
    usuarios
    return render_template("home/lista.html",usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)

# Esse if __name__ vai me impedir de ter que ficar rodando o codigo todo a vez

#OBS. você precisa colocar todo os seus arquivos HTML dentro de uma pasta chamada templates, caso isso não seja feito o html não irá funcionar
# O motivo disso e que o flask é um framework que precisa ser seguido passo a passo.

#OBS. vc pode criar varias pastas dentro da pasta templates, isso não vai afetar o codigo.