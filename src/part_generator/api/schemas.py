from pydantic import BaseClass

class WasherRequest(BaseClass):
    inner_diameter: float
    outer_diameter: float
    thickness: float

class BoltRequest(BaseClass):
    diameter: float
    length: float