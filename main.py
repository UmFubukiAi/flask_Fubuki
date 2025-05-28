from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/primeiro')
def primeiro():
    return render_template('./primeiro.html')

@app.route('/segundo')
def segundo():
    return render_template('./segundo.html')

@app.route('/terceiro')
def terceiro():
    return render_template('./terceiro.html')

@app.route('/quarto')
def quarto():
    return render_template('./quarto.html')

@app.route('/foto')
def foto():
    return render_template('./foto.html')

@app.route('/forms')
def forms():
    return render_template('./forms.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome=request.form['nome']
    email=request.form['email']
    estado=request.form['estado']
    formacao=request.form['formacao']
    return "{} - {} - {} - {}".format(nome, email, estado, formacao)

if __name__ == '__main__':
    app.run(debug=True)