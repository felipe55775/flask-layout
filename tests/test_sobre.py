from app import app


def test_sobre_contains_movies_and_series_sections():
    client = app.test_client()
    response = client.get('/sobre')

    assert response.status_code == 200

    html = response.get_data(as_text=True)
    assert 'Filmes' in html
    assert 'Séries' in html
    assert 'Cidade de Deus' in html
    assert 'Velozes e Furiosos 9' in html
    assert 'Impuros' in html
    assert 'Tropa de Elite' in html
