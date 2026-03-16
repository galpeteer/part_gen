import unittest
from fastapi.testclient import TestClient

from part_generator.main import app

"""
Unit testing for API endpoints in main.py. Tests include:
- Successful generation of washer and bolt with valid input (checking for 200 status code and non-empty response content)
- Handling of invalid input (e.g. negative dimensions, zero dimensions) - should return 422 status code for validation errors
"""

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_generate_washer(self):
        response = self.client.post(
            "/v1/generate/washer",
            json={
                "outer_diameter": 20,
                "inner_diameter": 10,
                "thickness": 5
            }
        )

        self.assertEqual(response.status_code, 200) #Successful response
        self.assertGreater(len(response.content), 0) # Response content not be empty

    def test_generate_bolt(self):
        response = self.client.post(
            "/v1/generate/bolt",
            json={
                "diameter": 10,
                "length": 50
            }
        )

        self.assertEqual(response.status_code, 200) #Successful response
        self.assertGreater(len(response.content), 0) # Response content not be empty

    def test_generate_washer_invalid_input(self):
        response = self.client.post(
            "/v1/generate/washer",
            json={
                "outer_diameter": -20,
                "inner_diameter": 10,
                "thickness": 5
            }
        )

        self.assertEqual(response.status_code, 422) #ValidationError
    
    def test_generate_bolt_invalid_input(self):
        response = self.client.post(
            "/v1/generate/bolt",
            json={
                "diameter": -10,
                "length": 50
            }
        )

        self.assertEqual(response.status_code, 422) #ValidationError

if __name__ == "__main__":
    unittest.main()