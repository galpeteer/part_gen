import cadquery as cq
import os


"""
This file contains the generation logic for different parts.
Currently:
- Washer
- Bolt
Used by main.py api endpoints, input validated by pydantic schemas in schemas.py

TODO:
- Add more fastener types (e.g. nuts, screws)
- Describe exact standards to follow (e.g. DIN, ISO) for each part type
- Logging
"""


def generate_washer(_outer_diameter, _inner_diameter, _thickness):
    if _outer_diameter <= 0:
        raise ValueError("Outer diameter must be positive")
    if _inner_diameter <= 0:
        raise ValueError("Inner diameter must be positive")
    if _thickness <= 0:
        raise ValueError("Thickness must be positive")
    if _inner_diameter >= _outer_diameter:
        raise ValueError("Inner diameter must be smaller than outer diameter")
    
    #choose workplane . outer diam . extrude thickness . select top face . hole diam

    _result= cq.Workplane("XY").circle(_outer_diameter / 2).extrude(_thickness).faces(">Z").hole(_inner_diameter)

    return _result
    

def generate_bolt(_diameter, _length):
    if _diameter <= 0:
        raise ValueError("Diameter must be positive")
    if _length <= 0:
        raise ValueError("Length must be positive")
    # calculations up for discussion, also I think pitch diameter should be used
    # instead of outer diameter for thread, but for now we can just use diameter as a placeholder

    _head_diameter = _diameter * 1.5         
    _head_thickness = _diameter * 0.8

    _bolt_diameter = _diameter

    # choose workplane . head diam . extrude head . select top face . bolt diam . extrude length

    _result = cq.Workplane("XY").circle(_head_diameter/2).extrude(_head_thickness).faces(">Z").circle(_bolt_diameter/2).extrude(_length)

    return _result


def export_result(_result, _filename):
    _result.export(_filename)
    return _filename


if __name__ == "__main__":
    
    DIR = os.path.dirname(__file__)

    result_w =generate_washer(20, 10, 5)
    export_result(result_w, DIR + "/result_washer.step")

    result_b = generate_bolt(10, 50)
    export_result(result_b, DIR + "/result_bolt.step")