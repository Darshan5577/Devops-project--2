import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import app

def test_home():
    app.testing = True
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Welcome to DevOps Project 2!"
    assert response.json["status"] == "Running"

def test_health():
    app.testing = True
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "Healthy"
