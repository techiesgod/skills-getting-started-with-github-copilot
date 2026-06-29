from urllib.parse import quote

from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant():
    activity_name = "Chess Club"
    email = "test.student@mergington.edu"

    signup_response = client.post(
        f"/activities/{quote(activity_name)}/signup?email={quote(email)}"
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        f"/activities/{quote(activity_name)}/participants/{quote(email)}"
    )
    assert unregister_response.status_code == 200

    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert email not in activities[activity_name]["participants"]
