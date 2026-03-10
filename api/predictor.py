from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

MODEL_PATH = MODELS_DIR / "xgboost_readmission_model.pkl"
FEATURES_PATH = MODELS_DIR / "feature_names.pkl"

THRESHOLD = 0.40

model = joblib.load(MODEL_PATH)
features_names = joblib.load(FEATURES_PATH)

def prepare_features(input_features: dict) -> pd.DataFrame:
    """
    Convert incoming feature dict inot a one-row DataFrame with 
    the exact same columns and orders using during taining.
    Missing features filled with 0.
    Extra features are ignored.
    """

    row = {feature: input_features.get(feature, 0.0) for feature in features_names}
    df = pd.DataFrame([row], columns=features_names)
    return df

def predict_readmission(input_features: dict) -> dict:
    """
    Return Predicted probability and class label
    """
    X_input = prepare_features(input_features)
    probability = float(model.predict_proba(X_input)[0,1])
    prediction = int(probability >= THRESHOLD)

    return {
        "readmission_probability" : probability,
        "prediction": prediction,
        "threshold": THRESHOLD,
    }