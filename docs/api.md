# API Documentation

## Overview
The Readmission Risk Predictor API serves the trained XGBoost model through a FastAPI backend. It allows users to submit processed patient features and recieve a predicted probability of 30-day hospital readmission.
The API is designed for inference only and uses the final saved model artifact from the machine learning pipeline.

Interactive docs are available at:

http://127.0.0.1:8000/docs

## Endpoints

### GET / 
Health check endpoint.

Example response:
```json
{
    "message": "Readmission Risk Predictor API is running"
}
```

### POST /predict
Returns readmission probability and prediction
Example request:
```json
{
    "features":{
        "number_inpatient": 2,
        "number_emergency": 0,
        "number_diagnoses" : 8,
        "insulin": 1
    } 
}
```
Example response:
```json
{
    "readmission_probability": 0.33,
    "predicted": 0,
    "threshold":0.4
}
```