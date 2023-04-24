import json
from fastapi import status

def test_create_post(client):
    # Prepare test data
    post_data = {
        "title": "test post",
        "description": "test content",
        "date_posted": "2021-01-01",
    }

    # Send the test request to create the post
    response = client.post("/posts/create-post/", json=post_data)

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response JSON data
    response_data = response.json()
    assert response_data["title"] == post_data["title"]
    assert response_data["description"] == post_data["description"]
    assert response_data["date_posted"] == post_data["date_posted"]
    
    # Assert that the password is not returned in the response
    assert "password" not in response_data

def test_get_post(client):
    # Prepare test data
    post_data = {
        "title": "test post",
        "description": "test content",
        "date_posted": "2021-01-01",
    }

    # Send the test request to create the post
    response = client.post("/posts/create-post/", json=post_data)

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response JSON data
    response_data = response.json()
    assert response_data["title"] == post_data["title"]
    assert response_data["description"] == post_data["description"]
    assert response_data["date_posted"] == post_data["date_posted"]
    
    # Assert that the password is not returned in the response
    assert "password" not in response_data

    # Send the test request to get the post
    response = client.get("/posts/get/1")

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response JSON data
    response_data = response.json()
    assert response_data["title"] == post_data["title"]
    
    # Assert that the password is not returned in the response
    assert "password" not in response_data

def test_get_all_posts(client, db_session):
    # Create a test post
    post_data = {
        "title": "test post",
        "description": "test content",
        "date_posted": "2021-01-01",
    }
    response = client.post("/posts/create-post/", json=post_data)
    assert response.status_code == 200

    # Retrieve all posts
    response = client.get("/posts/all/")
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) == 1
    assert response_data[0]["title"] == post_data["title"]
    assert response_data[0]["description"] == post_data["description"]
    assert response_data[0]["date_posted"] == post_data["date_posted"]

    # Assert that the password is not returned in the response
    assert "password" not in response_data[0]

def test_update_a_post(client, db_session):
    # Create a test post
    post_data = {
        "title": "test post",
        "description": "test content",
        "date_posted": "2021-01-01",
    }
    response = client.post("/posts/create-post/", json=post_data)
    assert response.status_code == 200

    # Update the test post
    updated_post_data = {
        "title": "updated title",
        "description": "updated content",
        "date_posted": "2021-01-02",
    }
    response = client.put("/posts/update/1", json=updated_post_data)
    assert response.status_code == 200
    assert response.json()["msg"] == "Successfully updated data."

    # Verify that the test post has been updated
    response = client.get("/posts/get/1")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == updated_post_data["title"]
    assert response_data["description"] == updated_post_data["description"]
    assert response_data["date_posted"] == updated_post_data["date_posted"]

    # Assert that the password is not returned in the response
    assert "password" not in response_data


def test_delete_a_post(client, db_session):
    # Create a test post
    post_data = {
        "title": "test post",
        "description": "test content",
        "date_posted": "2021-01-01",
    }
    response = client.post("/posts/create-post/", json=post_data)
    assert response.status_code == status.HTTP_200_OK

    # Delete the test post
    response = client.delete("/posts/delete/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["msg"] == "Successfully deleted data."

    # Verify that the test post has been deleted
    response = client.get("/posts/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
