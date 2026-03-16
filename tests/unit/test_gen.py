import unittest
import os 

from part_generator.services.gen_fastener import generate_washer, generate_bolt, export_result

"""
Unit testing for generation logic in services/gen_fastener.py. Tests include:
- Generation of washer and bolt objects (checking that they are not None)
- Invalid inputs (e.g. negative dimensions, zero dimensions) - should raise exceptions
- Exporting generated objects to STEP files (checking that files are created)
- Check model e.g.volume
)
"""

class TestGenFastener(unittest.TestCase):

    def test_generate_washer(self):
        result = generate_washer(20, 10, 5)
        self.assertIsNotNone(result)

    def test_generate_bolt(self):
        result = generate_bolt(10, 50)
        self.assertIsNotNone(result)

    def test_generate_washer_invalid_input(self):
        with self.assertRaises(ValueError):
            generate_washer(-20, 10, 5)
        with self.assertRaises(ValueError):
            generate_washer(20, -10, 5)
        with self.assertRaises(ValueError):
            generate_washer(20, 10, -5)
        with self.assertRaises(ValueError):
            generate_washer(0, 10, 5)
        with self.assertRaises(ValueError):
            generate_washer(20, 10, 0)
        with self.assertRaises(ValueError):
            generate_washer(20, 0, 5)
        with self.assertRaises(ValueError):
            generate_washer(20, 0, 5)
        with self.assertRaises(ValueError):
            generate_washer(10, 20, 5)

    def test_generate_bolt_invalid_input(self):
        with self.assertRaises(ValueError):
            generate_bolt(-10, 50)
        with self.assertRaises(ValueError):
            generate_bolt(10, -50)
        with self.assertRaises(ValueError):
            generate_bolt(0, 50)
        with self.assertRaises(ValueError):
            generate_bolt(10, 0)

    def test_generated_washer_volume(self):
        result = generate_washer(20, 10, 5)
        expected_volume = (3.14159 * (20**2 - 10**2) * 5) / 4
        self.assertAlmostEqual(result.val().Volume(), expected_volume, places=2)

    def test_generated_bolt_volume(self):
        result = generate_bolt(10, 50)
        expected_head_volume = (3.14159 * (15**2) * 8) / 4
        expected_shaft_volume = (3.14159 * (10**2) * 50) / 4
        expected_total_volume = expected_head_volume + expected_shaft_volume
        self.assertAlmostEqual(result.val().Volume(), expected_total_volume, places=2)

    def test_export_washer(self):
        DIR = os.path.dirname(__file__)
        result = generate_washer(20, 10, 5)
        export_result(result, DIR + "/test_washer.step")
        self.assertTrue(os.path.exists(DIR + "/test_washer.step"))
    
    def test_export_bolt(self):
        DIR = os.path.dirname(__file__)
        result = generate_bolt(10, 50)
        export_result(result, DIR + "/test_bolt.step")
        self.assertTrue(os.path.exists(DIR + "/test_bolt.step"))

if __name__ == "__main__":
    unittest.main()