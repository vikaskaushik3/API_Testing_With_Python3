import requests
import time


# Get request
def test_get_request():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


# Put request
def test_put_request():
    payload = {"id": 1,
               "title": "updated"
               }

    response = requests.put("https://jsonplaceholder.typicode.com/posts/1",
                            json=payload)
    assert response.status_code == 200


# Patch request
def test_patch_request():
    response = requests.patch("https://jsonplaceholder.typicode.com/posts/1",
                              json={"title": "patched title"})
    assert response.status_code == 200


# Delete request
def test_delete_request():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")


# Check response time of Get API
def test_get_response_time():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 1.0


# Request chaining
def test_title_in_chained_request():
    # Create post
    res = requests.post("https://jsonplaceholder.typicode.com/posts",
                        json={"title": "test", "body": "content", "userId": 1})
    assert res.status_code == 201
    response_data = res.json()
    print(response_data)

    assert "id" in response_data
    assert response_data["title"] == "test"
    assert response_data["userId"] == 1


# Retry mechanism
def test_retry_get_with_http_status_503():
    retries = 3
    response = None

    for attempt in range(retries):
        print(f"\n🌀 Attempt {attempt + 1} of {retries}")
        try:
            response = requests.get("https://httpbin.org/status/503")
            print(f"➡️ Status Code: {response.status_code}")

            if response.status_code == 200:
                print("✅ Successful response received")
                break
            else:
                print("❌ Not a 200 response, will retry if attempts remain...")
        except Exception as e:
            print(f"🔥 Exception occurred: {e}")
            break
        time.sleep(1)

    assert response is not None, "No response object returned"
    if response.status_code:
        if response.status_code == 503:
            print("🔔 Final Result: 503 Service Unavailable — API is not ready.")
    assert response.status_code == 503, f"Expected status 503 but got {response.status_code}"

