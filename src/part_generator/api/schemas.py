from pydantic import BaseModel, ConfigDict, StrictFloat, Field

"""
This file contains pydantic schemas for validating input data for part generation.
Currently:
- WasherRequest: for validating input data for washer generation (outer_diameter, inner_diameter, thickness)
- BoltRequest: for validating input data for bolt generation (diameter, length)
Used by main.py api endpoints to validate incoming JSON data before processing.
"""

#Washer input data schema
class WasherRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")  # Forbid extra fields
    inner_diameter: StrictFloat = Field(gt=0, le=100) #0<=inner_diameter<100, only float values allowed
    outer_diameter: StrictFloat = Field(gt=0, le=100) #0<=outer_diameter<100, only float values allowed
    thickness: StrictFloat = Field(gt=0, le=10) #0<=thickness<10, only float values allowed

class BoltRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")  # Forbid extra fields
    diameter: StrictFloat = Field(gt=0, le=50) #0<=diameter<50, only float values allowed
    length: StrictFloat = Field(gt=0, le=100) #0<=length<100, only float values allowed