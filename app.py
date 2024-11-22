from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # essa é a primeira tela que vai aparecer (raiz)
def inicio():
    return render_template("inicio.html")

@app.route('/contato')# segunda página para informações do usuário.
def contato():
    return render_template('contato.html')

@app.route('/mensagem')# terceira página para quando o usuário enviar a menssagem
def menssagem():
    return render_template('mensagem.html')