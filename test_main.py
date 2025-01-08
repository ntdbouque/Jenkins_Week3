from fastapi.testclient import TestClient
from api_check import app

client = TestClient(app)

def test_get_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_prime():
    test_cases = [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (29, True),
        (-5, False),
        (997, True),
        (0, False),
    ]
    
    for value, expected in test_cases:
        response = client.post("/check_prime", json={"value": value})
        assert response.status_code == 200
        assert response.json() == {"is_prime": expected}

def test_prime_non_integer():
    response = client.post("/check_prime", json={"value": "abc"})
    assert response.status_code == 422

if __name__ == "__main__":
    print("Running tests...")
    
    try:
        test_get_version()
        print("test_get_version passed")
        
        test_prime()
        print("test_prime passed")
        
        test_prime_non_integer()
        print("test_prime_non_integer passed")
        
        print("All tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
