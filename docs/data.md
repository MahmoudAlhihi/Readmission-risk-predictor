# The dataset contains 50 features describing hospital encounter of diabetes patients

## Features groups include:

### Demographics
- `race`
- `gender`
- `age`

### Hospital utilization 
- `time_in_hospital`
- `num_lab_procedures`
- `num_medications`
- `number_outpatient`
- `number_emergency`
- `number_inpatient`

### Administrative features
- `admission_type_id`
- `discharge_disposition_id`
- `admission_source_id`

### Diagnosis codes
- `diag_1`
- `diag_2`
- `diag_3`

### Medication features
- `insulin`
- `metformin`
- `glyburide`
- `others`

## Data preprocessing

 The raw dataset contained 50 features. Several preprocessing steps were applied before modeling

 ### Missing Values

 Columns with extremely high missing percentages were removed:
 - `weight` (97% missing)
 - `max_glu_serum` (95% missing)
 - `A1Cresult` (83% missing)

 Remaining missing values were handled using apropriate imputation

 ### Removed Identifier Columns
 The following identifier columns were removed because they do not provide predicitve information
 - `encounter_id`
 - `patient_nbr`

 ### Removed Constant Columns
 The following columns had zero variance and were removed:

 - `examide`
 - `citoglipton`

 ### Diagnosis Feature Engineering
 Diagnosis codes (`diag_1`, `diag_2`, `diag_3`) contained hundreds of ICD-9 codes.
 These were grouped into higher-level disease categories using official ICD-9 ranges such as:

 - `circulatory`
 - `respiratory`
 - `digestive`
 - `endocrine`
 - `injury`
 - `neoplasms`
 - `etc`

 This reduced hundreds of unique diagnosis codes to clincially meaningful categories

 ### Encoding
 Categorical variables were encoded using a combination of:

- binary encoding for two-value variables
- ordinal encoding for ordered variables such as age
- one-hot encoding for nominal variables

### Final Dataset
After preprocessing:
- **Rows:** 101,763
- **Features:** 173
- **Target:** `readmitted`

### Data Split
The dataset was split into:

- **Training:** 70%
- **Validation:** 15%
- **Test:** 15%

Stratified splitting was used to preserve class distribution

Class distribution:

- Not readmitted (<30 days): 88.8%
- Readmitted (<30 days): 11.2%




