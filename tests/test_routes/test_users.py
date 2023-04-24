import json


def test_create_user(client):
    # Prepare test data
    user_data = {
        "username": "testuser",
        "email": "testuser@nofoobar.com",
        "password": "testing",
    }

    # Send the test request to create the user
    response = client.post("/users/", json=user_data)

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response JSON data
    response_data = response.json()
    assert response_data["username"] == user_data["username"]
    assert response_data["email"] == user_data["email"]
    assert response_data["is_active"] is True

    # Assert that the password is not returned in the response
    assert "password" not in response_data
