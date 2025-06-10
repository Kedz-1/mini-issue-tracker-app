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


def test_delete_issue_deletes_by_id(client, example):
    result1 = client.post('/issues', json={
        'title': 'Delete',
        'description': 'This is the ticket we want to delete'
    })
    result2 = client.post('/issues', json=example)
    result3 = client.post('/issues', json=example)

    result1_id = result1.json()['id']

    client.delete(f'/issues/{result1_id}')

    total_issues = client.get('/issues')

    assert len(total_issues.json()) == 2
    assert result1_id not in total_issues.json()


def test_delete_issue_raises_404_when_issue_not_found(client, example):
    result1 = client.post('/issues', json=example)
    result2 = client.post('/issues', json=example)
    result3 = client.post('/issues', json=example)

    result1_id = result1.json()['id']

    response = client.delete('/issues/this_is_not_a_valid_id')

    assert response.status_code == 404


def test_delete_issue_returns_a_message_with_id_number(client, example):
    result1 = client.post('/issues', json={
        'title': 'Delete',
        'description': 'This is the ticket we want to delete'
    })
    result2 = client.post('/issues', json=example)
    result3 = client.post('/issues', json=example)

    result1_id = result1.json()['id']

    response = client.delete(f'/issues/{result1_id}')
    print(response.json())

    assert response.json()['message'] == f'Ticket has been deleted: {result1_id}'