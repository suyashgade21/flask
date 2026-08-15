from app.app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_get_employees():
    client = app.test_client()

    response = client.get("/employees")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) > 0


def test_get_employee():
    client = app.test_client()

    response = client.get("/employees/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1


def test_employee_not_found():
    client = app.test_client()

    response = client.get("/employees/999")

    assert response.status_code == 404
