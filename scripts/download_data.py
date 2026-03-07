from pathlib import Path
import pandas as pd
import openml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# OpenML dataset: "Diabetes130US"
# Source description: https://www.openml.org/d/4541
DATASET_ID = 4541

def main():
    ds = openml.datasets.get_dataset(DATASET_ID)

    #Return as pandas DataFrame
    X, y, categorical_indicator, attribute_names = ds.get_data(
        dataset_format="dataframe",
        target=ds.default_target_attribute, #should be "readmitted"
    )

    df = X.copy()
    if y is not None:
        df[ds.default_target_attribute] = y

    out_path = RAW_DIR / "diabetes130us_openml.csv"
    df.to_csv(out_path, index=False)

    print("Saved:", out_path)
    print("Shape:", df.shape)
    print("Target:", ds.default_target_attribute)
    print("Target distribution: \n", df[ds.default_target_attribute].value_counts(dropna=False))

if __name__ == "__main__":
    main()