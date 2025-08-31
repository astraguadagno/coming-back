from datetime import datetime
from pydantic import BaseModel, Field

class PayslipsRequest(BaseModel):
    user_id: str
    hours: float = Field(..., ge=0)
    date: datetime 
 
class PayslipsResponse(BaseModel):
    user_id: str
    hours: float
    date: datetime
    days_worked: int
