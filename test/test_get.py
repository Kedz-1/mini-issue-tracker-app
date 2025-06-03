import pytest
from src.main import create_issue, app
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from src.main import issues


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def example():
    return {
        "title": "Example bug",
        "description": "This is a test bug",
        "status": "Open"
    }


def test_get_issues_200_status_code(client, example):
    client.post('/issues', json=example)

    response = client.get('/issues')

    assert response.status_code == 200


def test_get_issues_returns_a_list(client, example):
    client.post('/issues', json=example)

    response = client.get('/issues')

    assert isinstance(response.json(), list)

def test_get_issues_returns_correct_fields(client, example):
    client.post('/issues', json=example)

    response = client.get('/issues')

    fields = ['id', 'title', 'description', 'status']

    for field in fields:
        assert field in response.json()[0]


def test_get_issues_returns_multiple_issues(client, example):

    client.post('/issues', json=example)
    client.post('/issues', json=example)

    response = client.get('/issues')

    assert len(response.json()) >= 2


def test_get_issues_returns_empty_list_when_no_post(client):
    issues.clear()

    response = client.get('/issues')
    
    assert response.status_code == 200
    assert response.json() == []