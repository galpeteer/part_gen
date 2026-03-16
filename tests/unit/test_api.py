import unittest
from fastapi.testclient import TestClient

from part_generator.main import app

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

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), 0)

    def test_generate_bolt(self):
        response = self.client.post(
            "/v1/generate/bolt",
            json={
                "diameter": 10,
                "length": 50
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), 0)

    def test_generate_washer_invalid_input(self):
        response = self.client.post(
            "/v1/generate/washer",
            json={
                "outer_diameter": -20,
                "inner_diameter": 10,
                "thickness": 5
            }
        )

        self.assertEqual(response.status_code, 422)
    
    def test_generate_bolt_invalid_input(self):
        response = self.client.post(
            "/v1/generate/bolt",
            json={
                "diameter": -10,
                "length": 50
            }
        )

        self.assertEqual(response.status_code, 422)

if __name__ == "__main__":
    unittest.main()