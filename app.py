from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('sobre.html', jogos=jogos)

@app.route("/boletim")
def boletim():
    return render_template('boletim.html')

if __name__ == "__main__":
    app.run(debug=True)
