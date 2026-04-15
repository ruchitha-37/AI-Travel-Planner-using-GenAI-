from pydantic import BaseModel, Field
from typing import Optional

class TravelRequest(BaseModel):
    destination: str = Field(..., example="Goa", description="Travel destination")
    preferences: str = Field(..., example="beach, nightlife, budget", description="Travel preferences")
    days: int = Field(..., ge=1, le=30, example=3, description="Number of travel days")
    budget: str = Field(..., example="budget", description="Budget level: budget / medium / luxury")
    travelers: Optional[int] = Field(1, ge=1, le=20, example=2, description="Number of travelers")
