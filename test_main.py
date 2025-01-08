from fastapi.testclient import TestClient
from api_check import app

client = TestClient(app)

def test_get_version():
    """Test the /version endpoint."""
    response = client.get("/version")
    assert response.status_code == 200, "Expected status code 200"
    assert response.json() == {"version": "1.0.0"}, "Expected version to be 1.0.0"

def test_prime_check():
    """Test the /check_prime endpoint with valid integer inputs."""
    test_cases = [
        (1, False), (2, True), (3, True),
        (4, False), (29, True), (-5, False),
        (997, True), (0, False),
    ]
    for value, expected in test_cases:
        response = client.post("/check_prime", json={"value": value})
        assert response.status_code == 200, f"Failed for value: {value} (status code)"
        assert response.json() == {"is_prime": expected}, f"Failed for value: {value} (response mismatch)"

def test_prime_invalid_input():
    """Test the /check_prime endpoint with invalid input (non-integer)."""
    response = client.post("/check_prime", json={"value": "abc"})
    assert response.status_code == 422, "Expected status code 422 for invalid input"

if __name__ == "__main__":
    print("Running tests...")

    try:
        test_get_version()
        print("test_get_version passed")
        
        test_prime_check()
        print("test_prime_check passed")
        
        test_prime_invalid_input()
        print("test_prime_invalid_input passed")
        
        print("All tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
