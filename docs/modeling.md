## Baseline Models: Logistic Regression and Random Forest

Two baseline classifiers were evaluated for predicting 30-day hospital readmission:
- Logistic Regression 
- Random Forest

The goal of these baseline models is to establish initital performance and understand the predicitve signal present in the dataset

### Dataset Split

- Training set: 70%
- Validation set: 15%
- Test set: 15%

Class Distribution:
- Not readmitted: 89%
- Readmitted within 30 days: 11%

Because the dataset is highly imbalanced, evaluation focuses on precision, recall, F1 score, and ROC-AUC, rather than accuracy alone

### Model Configuration

```
LogisticRegression(
    max_iter=2500,
    class_weight="balanced",
    random_state=42
)
```
Class weighting was used to compensate for the imbalanced dataset by penalizing misclassification of the minority class.

```rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)
```
Random Forest builds an ensemble of decision trees, allowing the model to capture more complex patterns in the data than logistic regression.

### Validation Results

Two classification thresholds were evaluated for `Logistic_regression` 

Threshold = 0.40
| Metric | Value |
|------|------|
| Accuracy | 0.36 |
| Precision | 0.13 |
| Recall | 0.86 |
| F1 Score | 0.23 |
| ROC-AUC | 0.64 |

Threshold = 0.50
| Metric | Value |
|------|------|
| Accuracy | 0.65 |
| Precision | 0.17 |
| Recall | 0.55 |
| F1 Score | 0.26 |
| ROC-AUC | 0.64 |

Two classificaiton thresholds were evaluated for `Forest_Trees`

Threshold = 0.10
| Metric | Value |
|------|------|
| Accuracy | 0.51 |
| Precision | 0.15 |
| Recall | 0.72 |
| F1 Score | 0.25 |
| ROC-AUC | 0.65 |

Threshold = 0.15
| Metric | Value |
|------|------|
| Accuracy | 0.75 |
| Precision | 0.20 |
| Recall | 0.42 |
| F1 Score | 0.27 |
| ROC-AUC | 0.65 |

### Interpretation

The logistic regression model detects approximately 54% of patients who will be readmitted within 30 days at the default threshold, though precision remains relatively low due to the strong class imbalance in the dataset. Random Forest shows slightly improved performance, achieving a higher ROC-AUC and slightly better F1 score. Lower classification thresholds increase recall for both models, allowing more high-risk patients to be detected, but at the cost of additional false positives.

### Feature Insights

Logistic regression coefficients suggest that features related to certain medical specialties; such as hematology, infectious disease, oncology, and pregnancy-related diagnoses are positively associated with hospital readmission. These specialties often involve patients with complex or chronic medical conditions that may require ongoing care. Random Forest, while less directly interpretable, captures nonlinear interactions between features that may also contribute to predicting readmission risk.


### Interpretability

Logistic regression provides strong interpretability by assigning coefficients to each feature, indicating how they influence the predicted probability of readmission. Positive coefficients increase the predicted risk, while negative coefficients decrease it. Random Forest models are less transparent but can capture more complex relationships in the data through ensembles of decision trees. Feature importance methods can be used to identify which variables contribute most strongly to the model’s predictions.

### Conclusion

Logistic regression provides a useful and interpretable baseline for predicting hospital readmissions, while Random Forest improves predictive performance by capturing nonlinear relationships between features. Both models demonstrate moderate predictive ability, which is typical for healthcare readmission prediction tasks. More advanced models, such as gradient boosting methods like XGBoost, may further improve performance and will be explored in the next stage of the project.