# FRAMEWORK FLASK PARA HOME-PAGE


## HTML
OBS. você precisa colocar todo os seus arquivos HTML dentro de uma pasta chamada templates, caso isso não seja feito o html não irá funcionar.
O motivo disso e que o flask é um framework que precisa ser seguido passo a passo.

OBS. vc pode criar varias pastas dentro da pasta templates, isso não vai afetar o codigo.

## CSS, IMAGENS

Para você ter CSS nas suas paginas html usando o FLASK vc precisa criar uma pasta chamada static, nela tmb poderá ser inseridas imagens, isso porque essa pasta recebe arquivos estáticos.

## PASSAR VARIAVEIS PARA AS ROTAS

# EXEMPLO.

app.route('/lista')
def lista():
    usuarios
    return render_template("home/lista.html",usuarios=usuarios)

Para passar as variaveis para a homepage elas precisam receber elas mesmas, essa parte ficou confusa para mim pórem funciona assim, depois as variaveis são passadas através do return junto com template, dessa forma elas estaram lá para serem usadas.

# NO HTML

{% for usuario in usuarios%}
    <p>{{usuario.nome}}</p>
    {% endfor %}

Primeira coisa quando você abre chaves é coloca o símbolo da porcentagem você pode escrever codigos python no HTML, isso acaba ajudando, o exemplo que eu usei foi uma lista onde eu queria apenas o nome dos usuarios, lembrando que e preciso passar duas chaves, uma dentro da outra, para qualquer varíavel seja ela lista ou não, Ex. {{usuario.nome}}.
