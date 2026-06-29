from urllib.parse import quote

from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant():
    # Arrange
    activity_name = "Chess Club"
    email = "test.student@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{quote(activity_name)}/signup?email={quote(email)}"
    )
    unregister_response = client.delete(
        f"/activities/{quote(activity_name)}/participants/{quote(email)}"
    )
    activities_response = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200

    activities = activities_response.json()
    assert email not in activities[activity_name]["participants"]
