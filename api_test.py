import pytest
import requests

BASE_URL = "https://reqres.in/api"

def test_get_users():
    """Test the GET /users endpoint"""
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 6
    assert "email" in response.json()["data"][0]

def test_create_user():
    """Test the POST /users endpoint"""
    payload = {
        "name": "John Doe",
        "job": "Software Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["job"] == "Software Engineer"

def test_update_user():
    """Test the PUT /users/<id> endpoint"""
    payload = {
        "name": "Jane Doe",
        "job": "Project Manager"
    }
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["job"] == "Project Manager"

def test_delete_user():
    """Test the DELETE /users/<id> endpoint"""
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204