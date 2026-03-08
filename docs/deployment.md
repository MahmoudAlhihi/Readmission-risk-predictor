## Baseline Model: Logistic Regression

A logistic regression model was trained as the baseline classifier.

### Dataset Split

- Training set: 70%
- Validation set: 15%
- Test set: 15%

Class Distribution:
- Not readmitted: 89%
- Readmitted within 30 days: 11%

### Model Configuration

```
LogisticRegression(
    max_iter=3000,
    class_weight="balanced",
    random_state=42
)
```
Class weighting was used to compensate for the imbalanced dataset

### Validation Results

- Accuracy: 0.65
- Precision: 0.17
- Recall: 0.55
- F1 Score: 0.26
- ROC-AUC: 0.61

### Interpretation

- The model detects approximately **54% of patients who will be readmitted within 30 days**, but produces a large number of false positives.

- While recall is moderatly high, the low precision indicates that many patients flagged as high-risk do not actually get readmitted.

### Feature Insights

Features with the strongest positive assocaition with readmission include:

- hematology specialty 
- infectious disease
- pregnancy related diagnoses
- oncology related diagnoses

These likely correspond to patients with complex medical conditions requiring follow-up care


### Interpretability

- One advantage of logistic regression is its interpretability. Unlike many complex machine learning models, logistic regression provides direct coefficients for each feature, which indicate how strongly a feature influences the probability of readmission.
- Positive coefficients increase the predicted risk of readmission, while negative coefficients decrease it. This allows clinicians and hospital administrators to understand which factors contribute most to patient readmission risk.
- In healthcare settings, interpretability is particularly valuable because medical professionals often prefer models that provide clear explanations for their predictions. The coefficients therefore offer insights into which diagnoses, treatments, or specialties are most associated with readmission risk.
- Although the overall predictive performance of the logistic regression model is limited, it provides an important baseline and offers interpretable insights that can help guide further model development.

### Conclusion

Logistic regression provides a useful baseline but demonstrates limited predictive power for this dataset. More flexible models such as tree-based methods are expected to capture nonlinear patterns and improve performance.