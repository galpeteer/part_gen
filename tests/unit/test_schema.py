import unittest
import os
import sys
from pathlib import Path
from pydantic import ValidationError

root = Path(__file__).parent.parent.parent #part_generator
src_path = root / "src"
sys.path.append(str(src_path))

from part_generator.api.schemas import WasherRequest, BoltRequest

"""
Unit testing for pydantic schemas in api/schemas.py. Tests include:
- Validation of correct inputs (e.g. positive dimensions)
- Validation of incorrect inputs (e.g. negative dimensions, zero dimensions) - should raise exceptions
- Validation of missing fields - should raise exceptions
- Validation of extra fields - should raise exceptions
"""

class TestSchemas(unittest.TestCase):

    def test_washer_schema_valid_input(self):
        data = {"inner_diameter": 10, "outer_diameter": 20, "thickness": 5}
        washer = WasherRequest(**data)
        self.assertEqual(washer.inner_diameter, 10)
        self.assertEqual(washer.outer_diameter, 20)
        self.assertEqual(washer.thickness, 5)

    def test_bolt_schema_valid_input(self):
        data = {"diameter": 10, "length": 50}
        bolt = BoltRequest(**data)
        self.assertEqual(bolt.diameter, 10)
        self.assertEqual(bolt.length, 50)

    def test_washer_schema_invalid_input(self):
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=-10, outer_diameter=20, thickness=5)
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=10, outer_diameter=-20, thickness=5)
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=10, outer_diameter=20, thickness=-5)
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=0, outer_diameter=20, thickness=5)
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=10, outer_diameter=0, thickness=5)
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=10, outer_diameter=20, thickness=0)
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=10, outer_diameter="20", thickness=0)

    def test_bolt_schema_invalid_input(self):
        with self.assertRaises(ValidationError):
            BoltRequest(diameter=-10, length=50)
        with self.assertRaises(ValidationError):
            BoltRequest(diameter=10, length=-50)
        with self.assertRaises(ValidationError):
            BoltRequest(diameter=0, length=50)
        with self.assertRaises(ValidationError):
            BoltRequest(diameter=10, length=0)
        with self.assertRaises(ValidationError):
            BoltRequest(diameter="10", length=50)

    def test_washer_schema_missing_fields(self):
        with self.assertRaises(ValidationError):
            WasherRequest(outer_diameter=20, thickness=5)
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=10, thickness=5)
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=10, outer_diameter=20)
    
    def test_bolt_schema_missing_fields(self):
        with self.assertRaises(ValidationError):
            BoltRequest(length=50)
        with self.assertRaises(ValidationError):
            BoltRequest(diameter=10)

    def test_washer_schema_extra_fields(self):
        with self.assertRaises(ValidationError):
            WasherRequest(inner_diameter=10, outer_diameter=20, thickness=5, color="red")
    
    def test_bolt_schema_extra_fields(self):
        with self.assertRaises(ValidationError):
            BoltRequest(diameter=10, length=50, material="steel")
        
if __name__ == '__main__':
    unittest.main()