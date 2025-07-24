import pytest
from src.main import app
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


def test_update_issue_raises_404_on_non_existent_issue(client, example):
    result = client.post('/issues', json=example)

    response = client.patch('/issues/this_id_does_not_exist', json={'status':'Closed'})

    assert response.status_code == 404 
    assert response.json()['detail'] == 'Issue not found'


def test_update_issue_updates_single_field(client, example):
    result = client.post('/issues', json = example)

    result_id = result.json()['id']

    response = client.patch(f'/issues/{result_id}', json={'status': 'Closed'})

    assert response.status_code == 200
    assert response.json()['status'] == 'Closed'


def test_update_issue_updates_in_memory(client, example):
    result = client.post('/issues', json=example)

    result_id = result.json()['id']

    response = client.patch(f'/issues/{result_id}', json={'status':'Closed'})

    status = client.get(f'/issues/{result_id}').json()['status']
    expected = 'Closed'

    assert status == expected