from pydantic import BaseModel, Field

class SumRequest(BaseModel):
    a: int = Field(..., ge=0)
    b: int = Field(..., ge=0)

class SumResponse(BaseModel):
    a: int
    b: int
    resultado: int
