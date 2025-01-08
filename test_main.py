from fastapi.testclient import TestClient
from api_check import app

client = TestClient(app)

def test_get_version():
    response = client.get("/version")
    assert response.status_code == 200, "Status code mismatch"
    assert response.json() == {"version": "1.0.0"}, "Version mismatch"

def test_prime_numbers():
    test_cases = [
        (0, False),
        (1, False),
        (2, True),
        (9, False),
        (17, True),
        (25, False),
        (89, True),
        (-11, False),
        (1001, False),
    ]
    for number, expected in test_cases:
        response = client.post("/check_prime", json={"value": number})
        assert response.status_code == 200, f"Status code mismatch for value {number}"
        assert response.json() == {"is_prime": expected}, f"Prime check mismatch for value {number}"

def test_invalid_inputs():
    invalid_inputs = ["hello", 3.5, None, {}, []]
    for invalid in invalid_inputs:
        response = client.post("/check_prime", json={"value": invalid})
        assert response.status_code == 422, f"Expected 422 for input {invalid}"

# Run tests
def run_tests():
    test_get_version()
    test_prime_numbers()
    test_invalid_inputs()

run_tests()
