def test_register_user(client):
    response = client.post("/register", json={
        "username": "vaishnavi",
        "password": "1234"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "vaishnavi"


def test_login_user(client):
    response = client.post("/login", data={
        "username": "vaishnavi",
        "password": "1234"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
