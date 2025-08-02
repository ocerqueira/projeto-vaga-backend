from http import HTTPStatus

from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)


def test_listar_departamentos():
    response = client.get('/departamentos')
    assert response.status_code == HTTPStatus.OK
    dados = response.json()
    assert isinstance(dados, list)
    nomes_departamentos = [d['nome'] for d in dados]
    assert 'RH' in nomes_departamentos


def test_listar_colaboradores_por_departamento_existente():
    response = client.get('/departamentos/1/colaboradores')
    assert response.status_code == HTTPStatus.OK
    dados = response.json()
    assert isinstance(dados, list)
    assert any(c['tem_dependentes'] is True for c in dados)
    assert any(c['tem_dependentes'] is False for c in dados)
