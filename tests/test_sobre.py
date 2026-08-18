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


def test_boletim_is_back_to_original_layout():
    client = app.test_client()
    response = client.get('/boletim')

    assert response.status_code == 200

    html = response.get_data(as_text=True)
    assert 'Boletim Escolar' in html
    assert 'Português' in html
    assert 'Média geral' in html
    assert 'Situação' in html
    assert 'Preencher dados' not in html
    assert 'Pode votar' not in html


def test_informacoes_page_exists_and_has_validation_content():
    client = app.test_client()
    response = client.get('/informacoes')

    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Informações' in html
    assert 'Nome' in html
    assert 'Idade' in html
    assert 'Pode votar' in html
