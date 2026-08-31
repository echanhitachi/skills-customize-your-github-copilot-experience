import importlib.util
import os
import sys

import pytest
from fastapi.testclient import TestClient

MODULE_PATH = os.path.join(os.path.dirname(__file__), "starter-code.py")
spec = importlib.util.spec_from_file_location("starter_code", MODULE_PATH)
starter_code = importlib.util.module_from_spec(spec)
sys.modules["starter_code"] = starter_code
spec.loader.exec_module(starter_code)


@pytest.fixture
def client():
    starter_code.items.clear()
    return TestClient(starter_code.app)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI REST API!"}


def test_read_item(client):
    client.post("/items", json={"name": "Widget", "price": 9.99})
    response = client.get("/items/0")
    assert response.status_code == 200
    assert response.json() == {"name": "Widget", "price": 9.99, "in_stock": True}


def test_read_item_not_found_returns_404(client):
    response = client.get("/items/42")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_create_item(client):
    payload = {"name": "Widget", "price": 9.99, "in_stock": True}
    response = client.post("/items", json=payload)
    assert response.status_code == 200
    assert response.json() == payload


def test_create_item_invalid_payload_returns_422(client):
    response = client.post("/items", json={"name": "Widget"})
    assert response.status_code == 422


def test_list_items(client):
    client.post("/items", json={"name": "Widget", "price": 9.99})
    client.post("/items", json={"name": "Gadget", "price": 19.99, "in_stock": False})
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_delete_item(client):
    client.post("/items", json={"name": "Widget", "price": 9.99})
    response = client.delete("/items/0")
    assert response.status_code == 200
    assert response.json()["name"] == "Widget"
    assert client.get("/items").json() == []


def test_delete_item_not_found_returns_404(client):
    response = client.delete("/items/0")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
