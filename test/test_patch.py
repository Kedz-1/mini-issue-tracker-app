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


def test_update_issue_returns_404_on_non_existent_issue(client, example):
    result = client.post('/issues', json=example)

    response = client.patch('/issues/this_id_does_not_exist', json={'status':'Closed'})

    assert response.status_code == 404 
