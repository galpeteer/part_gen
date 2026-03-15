from pydantic import BaseModel

class WasherRequest(BaseModel):
    inner_diameter: float
    outer_diameter: float
    thickness: float

class BoltRequest(BaseModel):
    diameter: float
    length: float