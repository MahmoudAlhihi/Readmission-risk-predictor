from pydantic import BaseModel, Field
from typing import Dict

class PredictionRequest(BaseModel):
    features:Dict[str, float] = Field(
        ...,
        description="Processed feature dictionary keyed by training feature names"
    )

class PredictionResponse(BaseModel):
    readmission_probability: float
    prediction: int
    threshold: float