import pytest
from src.main import create_issue, app
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient


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



def test_create_issue_returns_200_status_code(client, example):
    response = client.post('/issues', json=example)

    print(response)
    assert response.status_code == 200


def test_create_issue_has_correct_fields(client, example):
    response = client.post('/issues', json=example)

    expected_fields = ['id', 'title', 'description', 'status']

    for fields in expected_fields:
        assert fields in response.json()


def test_create_issue_returns_status_open_when_no_input(client):

    response = client.post('issues', json={"title": "Example bug",
        "description": "This is a test bug"})

    result = response.json()

    assert result['status'] == 'Open'


def test_create_issue_returns_422_on_missing_fields(client):
    response = client.post('/issues', json={
        'description': 'Missing title'
        }
    )

    print(response)

    assert response.status_code == 422


def test_create_issue_returns_422_on_invalid_data_type(client):
    response = client.post('/issues', json={
        "title": 312,
        "description": 1,
        "status": "Open"
    })

    assert response.status_code == 422


def test_create_issue_has_unique_id(client, example):
    response1 = client.post('/issues', json=example)
    response2 = client.post('/issues', json=example)

    id1 = response1.json()['id']
    id2 = response2.json()['id']

    assert id1 != id2