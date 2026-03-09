## Baseline Models: Logistic Regression and Random Forest

Two baseline classifiers were evaluated for predicting 30-day hospital readmission:
- Logistic Regression 
- Random Forest

The goal of these baseline models is to establish initital performance and understand the predicitve signal present in the dataset

## Gradient Boosting Model: XGBoost

To further improve predictive performance, a gradient boosting model using XGBoost was trained. Unlike Random Forest, which builds trees independently, XGBoost builds trees sequentially, where each new tree attempts to correct the errors made by previous trees

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

```
rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)
```
Random Forest builds an ensemble of decision trees, allowing the model to capture more complex patterns in the data than logistic regression.

``` XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8, objective="binary:logistic",
    eval_metric="auc",
    scale_pos_weight=8,
    random_state=42
)
```
This configuration allows the model to caputre nonlinear relationships while addressing class imbalance through `scale_pos_weight`

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

Two classificaiton thresholds were evaluated for `XGBoost`

Threshold = 0.30
| Metric | Value |
|------|------|
| Accuracy | 0.24 |
| Precision | 0.12 |
| Recall | 0.96 |
| F1 Score | 0.22 |
| ROC-AUC | 0.68 |

Threshold = 0.50
| Metric | Value |
|------|------|
| Accuracy | 0.64 |
| Precision | 0.18 |
| Recall | 0.61 |
| F1 Score | 0.28 |
| ROC-AUC | 0.68 |



### Interpretation

The logistic regression model detects approximately 54% of patients who will be readmitted within 30 days at the default threshold, though precision remains relatively low due to the strong class imbalance in the dataset. Random Forest shows slightly improved performance, achieving a higher ROC-AUC and slightly better F1 score. Lower classification thresholds increase recall for both models, allowing more high-risk patients to be detected, but at the cost of additional false positives.

XGBoost demonstrates the strongest predicitve performance among the models tested. The model achieves higher ROC-AUC and F1 score compared to both logistic regression and random forest, indicating improved ability to rank patients according to readmission risk.

Lower thresholds significantly increase recall, capturing nearly all potential readmissions, while higher thresholds provide a better balance between precision and recall.

### Feature Insights

Logistic regression coefficients suggest that features related to certain medical specialties; such as hematology, infectious disease, oncology, and pregnancy-related diagnoses are positively associated with hospital readmission. These specialties often involve patients with complex or chronic medical conditions that may require ongoing care. Random Forest, while less directly interpretable, captures nonlinear interactions between features that may also contribute to predicting readmission risk.


### Interpretability

Logistic regression provides strong interpretability by assigning coefficients to each feature, indicating how they influence the predicted probability of readmission. Positive coefficients increase the predicted risk, while negative coefficients decrease it. Random Forest models are less transparent but can capture more complex relationships in the data through ensembles of decision trees. Feature importance methods can be used to identify which variables contribute most strongly to the model’s predictions.

### Conclusion

Logistic regression provides a useful and interpretable baseline for predicting hospital readmissions, while Random Forest improves predictive performance by capturing nonlinear relationships between features. Both models demonstrate moderate predictive ability, which is typical for healthcare readmission prediction tasks. More advanced models, such as gradient boosting methods like XGBoost, may further improve performance and will be explored in the next stage of the project.

XGBoost provides the best overall performance among the evaluated models, achieving the highest ROC-AUC and F1 score. Its ability to capture complex nonlinear relationships between features makes it particularly effective for tabular healthcare data. Based on these results, XGBoost will be selected as the final model for predicting 30-day hospital readmission risk.

### Final Model Evaluation

The final XGBoost model was evaluated on the test set to estimate performance on unseen data. Using a probability threshold of 0.40, the model achieved on ROC-AUC of 0.681, recall of 0.833, precision of 0.146, and F1 score of 0.249. These results indicate that the model is effective at identifying the majority of patients who will be readmitted within 30 days, although it produces a number of false positives. In clincal settings, this tradeoff may be acceptable since failing to identify a high-risk patient can be more costly than flagging additional patients for monitoring or intervention.

### Feature Imporatnce Analysis

Feature importance analysis from the XGBoost model reveals that prior helthcare utilization plays a major role in prediciting readmission risk. The most influential feature was `number_inpatient`, indicating that patients with more previous inpatient admissions are significantly more likely to be readmitted. Other important predictors include `discharge disposition`,  `number of emergency visits` and `number of diagnoses`,  which collectively reflect the complexity of a patient's medical condition and healthcare usage patterns. Clinical features related to diabetes treatment, such as `insulin usage` and `diabetes medication`, also contributed to the model's predictions. Additionally, diagnosis categories including circulatory diseases, mental health conditions, and neoplasms were among the most informative predictors. Overall, the model appears to capture both healthcare utilization patterns and clinical severity as key drivers of hospital readmission risk.