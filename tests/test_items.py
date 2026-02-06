# Helper to get JWT token
def login_and_get_token(client):
    client.post("/register", json={
        "username": "vaishnavi",
        "password": "1234"
    })
    login = client.post("/login", data={
        "username": "vaishnavi",
        "password": "1234"
    })
    return login.json()["access_token"]


def test_create_item(client):
    token = login_and_get_token(client)

    response = client.post(
        "/items/",
        json={"name": "Laptop", "price": 250},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"


def test_get_items(client):
    token = login_and_get_token(client)

    response = client.get(
        "/items/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_item(client):
    token = login_and_get_token(client)

    # Create item
    create = client.post(
        "/items/",
        json={"name": "Phone", "price": 100},
        headers={"Authorization": f"Bearer {token}"}
    )
    item_id = create.json()["id"]

    # Update item
    response = client.put(
        f"/items/{item_id}",
        json={"name": "SmartPhone", "price": 150},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "SmartPhone"


def test_delete_item(client):
    token = login_and_get_token(client)

    # Create item
    create = client.post(
        "/items/",
        json={"name": "Tablet", "price": 300},
        headers={"Authorization": f"Bearer {token}"}
    )
    item_id = create.json()["id"]

    # Delete
    response = client.delete(
        f"/items/{item_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
