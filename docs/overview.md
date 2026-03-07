# Project goal
- This project predicts the risk of hospital readmission within 30 days using the UCI diabetes 130-US hospitals dataset.
- The goal is to build a machine learning system that can help hospital identify patients at high risk of readmission and potentially intervene earlier.

## Dataset summary
- Dataset size : 101,766 hospital encounters
- Total features: 50

Feature types:
- Numerical features: 13
- Categorical features: 36 

Missing values exist in 9 features with varying percentages.

The dataset contains demographic, administrative, medication, and utilization variables.

Target varibale: readmitted
Original classes:
-NO
- >30 days
- <30 days
For modeling, the target will later be converted to a binary variable indicating whether a patient was readmitted within 30 days.