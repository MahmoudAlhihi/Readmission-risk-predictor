# Exploratory Data Analysis

EDA was performed in the notebooks:

- `01_eda.ipynb`
- `02_eda.ipynb`

## Dataset Size

- Observations: 101,766
- Features: 50

## Features Types

The dataset contains a mixture of numerical and categorical variables.

- Numerical features: 13
- Categorical features: 36

Most variables are categorical hospital record attributes.

## Missing Values

Missing values were identified in **9 features** with varying percentages.

Some missing values are represented as `"?"` in the raw dataset.

## Class Distribution

The target variable `readmitted` contatins three categories:

- `NO`
- `>30`
- `<30`

The `<30` class represents readmission within 30 days and will be used as the positive class in the prediction task.

The dataset shows **class imbalance**, with significantly fewer `<30` cases.

## Key Observations

- The dataset is mostly categorical.
- Several features contain missing values.
- Some categorical variables have high cardinality.
- The dataset exhibits class imbalance.