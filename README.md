# Readmission Risk Predictor
An end-to-end healthcare machine learning system that predicts 30-day hospital readmission risk using electronic health record (EHR) data

Hospital readmissions are a major challenge for healthcare systems. Early identification of high-risk patients allows a hospitals to allocate follow-up care, improve discharge planning, and reduce avoidable readmissions

This project builds a complete ML pipeline, from data analysis and model training to deployment as a prediction API.

## Project Goals

The objective of this project is to build a production style machine learning system that:
- Analyzes healthcare data to identify readmission patterns
- Trains multiple machine learning models
- Evaluate model performance on unseen data 
- Exposed prediction through a REST API
- Deploys the model to the cloud


## Dataset

The model is trained on the Diabetes 130-US Hospitals dataset, which contains over 100,000 hopspital encounters from multiple US healthcare institutions

The dataset includes:
- patient demographics
- diagnoses
- medications
- hospital visits
- discharge information

Target variable:
`readmitted within 30 days`
Class distribution:
`Not readmitted: 89%`
`Readmitted <30 days: 11%`

## ML pipeline
1. Exploratory Data Analysis
- feature distributions
- missing value analysis
- class imbalance investigation
- clinical feature grouping

2. Data Preprocessing
- categorical encoding
- missing value handling
- feature grouping for diagnoses
- train/val/test split

3. Baseline Model
Two baseline models were trained:
- Logistic Regression
- Random Forest

4. Advanced Model
The final model uses `XGBoost`, a gradient boosting algorithm that captures nonlinear relationships and feature interactions

5. Threshold Optimation 
Because the dataset is imbalanced, classifcation thresholds were tuned to balance:
- precision
- recall
- false positive rate

6. Final Test Evaluation
The selected model was evaluated on test set
Final performance: 
ROC-AUC:   0.681
Recall:    0.833
Precision: 0.146
F1 Score:  0.249



## Deployment
The trained model is deployed as a **production-style inference service**.

### Components

**FastAPI Backend**
- Serves predictions through a REST API
- Loads trained XGBoost model
- Returns readmission probability and classification

**Streamlit Web Interface**
- Interactive interface for submitting patient features
- Displays prediction results and probabilities

**Docker Containers**
- API and UI containerized for reproducible deployment

**AWS EC2 Deployment** 
- Both services deployed to cloud instance

## Project Structure
| api/ | FastAPI prediction service|
| src/ |ML pipeline code|
| notebooks/ | EDA and experimentation |
| models/ | trained model artifacts |
| data/ | raw and processed datasets |
| docs/ | technical documentation |
| scripts/ | data download utilities |
| tests/ | basic project tests |

## Tech Stack
- Python
- Scikit-learn
- XGBoost
- FastAPI
- Streamlit
- Docker
- AWS EC2

## Live Demo
Streamlit UI:
http://51.20.53.90:8501

API Docs: 
http://51.20.53.90:8000/docs

# Author
Mahmoud Alhihi
University of Minnesota

Github: https://github.com/MahmoudAlhihi
LinkedIn: https://www.linkedin.com/in/mahmoud-alhihi-238047254/