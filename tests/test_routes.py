from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_square_positive():
    response = client.get("/square/5")
    assert response.status_code == 200
    assert response.json() == {"number": 5, "square": 25}

def test_square_zero():
    response = client.get("/square/0")
    assert response.json()["square"] == 0

def test_square_negative():
    response = client.get("/square/-3")
    assert response.json()["square"] == 9

def test_reverse_word():
    response = client.get("/reverse/abc")
    assert response.json()["reversed"] == "cba"

def test_reverse_palindrome():
    response = client.get("/reverse/madam")
    assert response.json()["reversed"] == "madam"

def test_hello_status():
    response = client.get("/hello")
    assert response.status_code == 200

def test_square_type():
    response = client.get("/square/7")
    assert isinstance(response.json()["square"], int)

def test_reverse_empty():
    response = client.get("/reverse/")
    assert response.status_code == 404  # no param provided