from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "OK"


def test_teste():
    client = app.test_client()

    response = client.get("/teste")

    assert response.status_code == 200
    assert response.json["teste"] == "CI/CD funcionando!"
