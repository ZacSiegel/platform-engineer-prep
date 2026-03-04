from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_add_two_services():
    response = client.post("/services/add_service", json={
        "name": "simple bebe kyuts",
        "owner": "lil bebe cb",
        "version": "1.0.2"
    })

    assert response.status_code == 200
    assert response.json()[0]["name"] == "simple bebe kyuts"

    response_2 = client.post("/services/add_service", json={
        "name": "big floofs",
        "owner": "dukey bubba",
        "version": "0.0.8"
    })

    assert response_2.status_code == 200
    assert response_2.json()[1]["name"] == "big floofs"


def test_list_all_services():
    response = client.get("/services")
    assert response.status_code == 200
    assert response.json()
