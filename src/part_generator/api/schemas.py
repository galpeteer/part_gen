from pydantic import BaseModel, ConfigDict, StrictFloat, Field

class WasherRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")  # Forbid extra fields
    inner_diameter: StrictFloat = Field(gt=0, le=100)
    outer_diameter: StrictFloat = Field(gt=0, le=100)
    thickness: StrictFloat = Field(gt=0, le=10)

class BoltRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")  # Forbid extra fields
    diameter: StrictFloat = Field(gt=0, le=50)
    length: StrictFloat = Field(gt=0, le=100)