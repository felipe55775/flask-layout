import os

from flask import Flask, render_template, request

app = Flask(__name__)


def pode_votar(idade):
    return idade >= 18


def pode_dirigir(idade):
    return idade >= 18


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sobre")
def sobre():
    jogos = [
        {
            'titulo': 'GTA V',
            'imagem': 'https://upload.wikimedia.org/wikipedia/en/a/a5/Grand_Theft_Auto_V.png',
            'descricao': 'Um jogo de mundo aberto que mistura ação, liberdade e histórias memoráveis em Los Santos.'
        },
        {
            'titulo': 'Red Dead Redemption 2',
            'imagem': 'https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg',
            'descricao': 'Uma experiência de narrativa profunda, exploração incrível e um cenário belíssimo que vale cada minuto.'
        },
        {
            'titulo': 'The Last of Us Part I',
            'imagem': 'https://cdn.akamai.steamstatic.com/steam/apps/1888930/library_600x900.jpg',
            'descricao': 'Um jogo emocionante, intenso e emocional, com direção de arte impecável e uma história impactante.'
        },
        {
            'titulo': 'God of war',
            'imagem': 'https://cdn.akamai.steamstatic.com/steam/apps/1593500/library_600x900.jpg',
            'descricao': 'Uma jornada com mais emoção, desafios e um desenvolvimento de personagens muito forte.'
        },
        {
            'titulo': 'Marvel\'s Spider-Man',
            'imagem': 'https://cdn.akamai.steamstatic.com/steam/apps/1817070/library_600x900.jpg',
            'descricao': 'Um dos meus favoritos por unir ação frenética, exploração urbana e uma ótima sensação de ser o Homem-Aranha.'
        }
    ]

    filmes = [
        {
            'titulo': 'Cidade de Deus',
            'imagem': 'https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=900&q=80',
            'descricao': 'Um dos filmes mais intensos e marcantes, com história, tensão e impacto visual incríveis.'
        },
        {
            'titulo': 'Velozes e Furiosos 9',
            'imagem': 'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=900&q=80',
            'descricao': 'Ação acelerada, adrenalina e uma dose de família, velocidade e emoção em cada cena.'
        }
    ]

    series = [
        {
            'titulo': 'Impuros',
            'imagem': 'https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?auto=format&fit=crop&w=900&q=80',
            'descricao': 'Uma série envolvente, com drama, tensão e personagens muito marcantes.'
        },
        {
            'titulo': 'Tropa de Elite',
            'imagem': 'https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=900&q=80',
            'descricao': 'Um clássico do gênero, intenso, realista e cheio de situações decisivas.'
        }
    ]

    return render_template('sobre.html', jogos=jogos, filmes=filmes, series=series)

@app.route("/boletim", methods=['GET', 'POST'])
def boletim():
    nome = ''
    sobrenome = ''
    idade = 0
    resultado = {
        'nome_completo': '',
        'pode_votar': False,
        'pode_dirigir': False,
    }

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        sobrenome = request.form.get('sobrenome', '').strip()
        idade = request.form.get('idade', 0, type=int)

        if nome or sobrenome:
            resultado['nome_completo'] = f'{nome} {sobrenome}'.strip()
            resultado['pode_votar'] = pode_votar(idade)
            resultado['pode_dirigir'] = pode_dirigir(idade)

    return render_template('boletim.html', nome=nome, sobrenome=sobrenome, idade=idade, resultado=resultado)


@app.route("/informacoes", methods=['GET', 'POST'])
def informacoes():
    nome = ''
    sobrenome = ''
    idade = 0
    resultado = {
        'nome_completo': '',
        'pode_votar': False,
        'pode_dirigir': False,
    }

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        sobrenome = request.form.get('sobrenome', '').strip()
        idade = request.form.get('idade', 0, type=int)

        if nome or sobrenome:
            resultado['nome_completo'] = f'{nome} {sobrenome}'.strip()
            resultado['pode_votar'] = pode_votar(idade)
            resultado['pode_dirigir'] = pode_dirigir(idade)

    return render_template('informacoes.html', nome=nome, sobrenome=sobrenome, idade=idade, resultado=resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
