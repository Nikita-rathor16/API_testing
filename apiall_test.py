# import pytest
import requests

BASE_URL = "https://reqres.in/api"

def test_get_users():
    """Test the GET /users endpoint"""
    response = requests.get(f"{BASE_URL}/users?page=2", timeout=10)
    assert response.status_code == 200
    assert len(response.json()["data"]) == 6
    assert "email" in response.json()["data"][0]

def test_create_user():
    """Test the POST /users endpoint"""
    payload = {
        "name": "John Doe",
        "job": "Software Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload, timeout=10)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["job"] == "Software Engineer"

def test_update_user():
    """Test the PUT /users/<id> endpoint"""
    payload = {
        "name": "Jane Doe",
        "job": "Project Manager"
    }
    response = requests.put(f"{BASE_URL}/users/2", json=payload, timeout=10)
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["job"] == "Project Manager"

def test_delete_user():
    """Test the DELETE /users/<id> endpoint"""
    response = requests.delete(f"{BASE_URL}/users/2", timeout=10)
    assert response.status_code == 204

def test_get_single_user():
    """Test the GET /users/<id> endpoint"""
    response = requests.get(f"{BASE_URL}/users/2", timeout=10)
    assert response.status_code == 200
    assert "data" in response.json()
    assert "email" in response.json()["data"]

def test_get_single_user_not_found():
    """Test the GET /users/<id> endpoint for a non-existent user"""
    response = requests.get(f"{BASE_URL}/users/23", timeout=10)
    assert response.status_code == 404

def test_get_list_resources():
    """Test the GET /unknown endpoint"""
    response = requests.get(f"{BASE_URL}/unknown", timeout=10)
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0

def test_get_single_resource():
    """Test the GET /unknown/<id> endpoint"""
    response = requests.get(f"{BASE_URL}/unknown/2", timeout=10)
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_single_resource_not_found():
    """Test the GET /unknown/<id> endpoint for a non-existent resource"""
    response = requests.get(f"{BASE_URL}/unknown/23", timeout=10)
    assert response.status_code == 404

def test_register_successful():
    """Test the POST /register endpoint with valid data"""
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(f"{BASE_URL}/register", json=payload, timeout=10)
    assert response.status_code == 200
    assert "token" in response.json()

def test_register_unsuccessful():
    """Test the POST /register endpoint with invalid data"""
    payload = {
        "email": "sydney@fife"
    }
    response = requests.post(f"{BASE_URL}/register", json=payload, timeout=10)
    assert response.status_code == 400
    assert "error" in response.json()

def test_login_successful():
    """Test the POST /login endpoint with valid data"""
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload, timeout=10)
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_unsuccessful():
    """Test the POST /login endpoint with invalid data"""
    payload = {
        "email": "peter@klaven"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload, timeout=10)
    assert response.status_code == 400
    assert "error" in response.json()

def test_delayed_response():
    """Test the GET /users endpoint with a delay"""
    response = requests.get(f"{BASE_URL}/users?delay=3", timeout=10)
    assert response.status_code == 200
    assert len(response.json()["data"]) == 6