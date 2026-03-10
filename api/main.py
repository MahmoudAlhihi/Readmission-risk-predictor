from fastapi import FastAPI, HTTPException
from api.schema import PredictionRequest, PredictionResponse
from api.predictor import predict_readmission

app = FastAPI(
    title="Readmission Risk Predictor API",
    description="API for predicting 30-day hospital readmission risk",
    version="1.0.0"
)

@app.get("/")
def root():
    return{
        "message" : "Readmission Risk Predictor API is runnig",
        "docs" : "/docs"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        result = predict_readmission(request.features)
        return PredictionResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))