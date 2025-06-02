import os
import csv
from flask import Flask
from flask import render_template, request, redirect, url_for
import google.generativeai as gemini
import markdown

app = Flask(__name__)

os.environ['FLASK_DEBUG'] = 'True'
app.debug = os.environ.get('FLASK_DEGUB') == 'True'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dicionario')
def dicionario():
    glossario_de_termos = []
    with open('glossario.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for line in reader:
            glossario_de_termos.append(line)

    return render_template(
        'dicionario.html',
        glossario_de_termos=glossario_de_termos)


@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')


@app.route('/sobre')
def sobre():
    import requests
    users_1 = requests.get('https://api.github.com/users/leticiassoares')
    users_2 = requests.get('https://api.github.com/users/gabrielfgomss')
    if users_1.status_code == 200 and users_2.status_code == 200:
        users = [users_1.json(), users_2.json()]
    else:
        users = []
    return render_template('sobre.html', users=users)


@app.route('/criar_termo', methods=['POST', ])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']
    with open('glossario.csv', 'a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow([termo, definicao])
    return redirect(url_for('dicionario'))


@app.route('/deletar_termo/<int:termo_id>', methods=['POST', ])
def deletar_termo(termo_id):
    with open('glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        linhas = list(leitor)
    for i, linha in enumerate(linhas):
        if i == termo_id:
            del linhas[i]
            break
    with open('glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(linhas)
    return redirect(url_for('dicionario'))


@app.route('/editar_termo/<int:termo_id>', methods=['GET', 'POST'])
def editar_termo(termo_id):
    with open('glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        linhas = list(leitor)
    if request.method == 'POST':
        novo_termo = request.form['termo_alt']
        nova_definicao = request.form['definicao_alt']
        linhas[termo_id] = [novo_termo, nova_definicao]
        with open('glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';')
            escritor.writerows(linhas)
        return redirect(url_for('dicionario'))
    termo = linhas[termo_id][0]
    definicao = linhas[termo_id][1]
    return render_template('editar_termo.html', termo=termo, definicao=definicao, termo_id=termo_id)


@app.route('/duvidas', methods=['GET', 'POST'])
def duvidas():
    pergunta = None
    resposta = None
    
    if request.method == 'POST':
        pergunta = request.form['pergunta']
        gemini.configure(api_key='')
        model = gemini.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(pergunta)
        resposta = markdown.markdown(response.text)
    return render_template('duvidas.html', pergunta=pergunta, resposta=resposta)


if __name__ == '__main__':
    app.run()
