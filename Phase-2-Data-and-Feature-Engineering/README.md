## 📅Day 16 — Feature Engineering Foundations
- Features and Targets
- X and y
- Types of Features
- Numerical Features
- Categorical Features
- Binary Features
- Ordinal Features
- Feature Engineering
- Derived Features
- Mathematical Feature Creation
- Interaction Features
- Polynomial Features
- Date/Time Feature Engineering
- Feature Selection
- Data Leakage

---

# 📅Day 17 — Handling Missing Data
- Missing Data
- `NaN`
- Detecting Missing Values
- `isnull()`
- `isna()`
- Counting Missing Values with `sum()`
- Finding Rows with Missing Values
- `dropna()`
- Imputation
- Mean Imputation
- Median Imputation
- Mode Imputation
- Constant Value Imputation
- Forward Fill (`ffill()`)
- Backward Fill (`bfill()`)
- Missing Data vs Zero
- Meaning of Missing Data
- Data Leakage During Imputation
- `SimpleImputer`
- Imputation Strategies:
  - `mean`
  - `median`
  - `most_frequent`
  - `constant`

---

# 📅Day 18 — Encoding Categorical Data
- Categorical Data
- Nominal Data
- Ordinal Data
- Encoding
- Label Encoding
- Limitations of Label Encoding
- Ordinal Encoding
- One-Hot Encoding
- One-Hot Encoding with Pandas
- One-Hot Encoding with Scikit-learn
- `drop="first"`
- Binary Encoding (`0` / `1`)
- Encoding Multiple Categorical Columns
- Handling Unknown Categories
- `handle_unknown="ignore"`
- `fit()`
- `transform()`
- `fit_transform()`
- Encoding and Data Leakage
- `OneHotEncoder`
- `OrdinalEncoder`

---

# 📅Day 19 — Feature Scaling
- Feature Scaling
- Why Feature Scaling is Important
- Distance-Based Algorithms and Feature Scale
- Standardization
- Standardization Formula
- `StandardScaler`
- Mean and Standard Deviation
- Min-Max Normalization
- Min-Max Scaling Formula
- `MinMaxScaler`
- StandardScaler vs MinMaxScaler
- Effect of Outliers on Scaling
- `fit()`
- `transform()`
- `fit_transform()`
- Scaling Training and Test Data
- Data Leakage During Scaling
- Scaling and Tree-Based Algorithms
- Scaling vs Normalization Terminology

---

## 📅Day 20 — Outliers
- Outliers
- Outlier vs Anomaly
- Importance of Outlier Detection
- Quartiles
- Q1 (First Quartile)
- Q2 (Median)
- Q3 (Third Quartile)
- Interquartile Range (IQR)
- IQR Formula
- IQR Outlier Rule (1.5 × IQR)
- Lower Bound
- Upper Bound
- Outlier Detection using IQR
- Outlier Detection using Box Plots
- Box Plot Visualization
- Z-Score
- Z-Score Formula
- Outlier Detection using Z-Score
- abs(z_score) > 3
- IQR vs Z-Score
- Boolean Masking in Pandas
- Handling Outliers
- Removing Outliers
- Correcting Outliers
- Capping / Winsorization
- Log Transformation (np.log1p)
- Effect of Outliers on Feature Scaling
- RobustScaler
- Median and IQR based Scaling
- Importance of Domain Knowledge in Outlier Handling

---

## 📅Day 21 — Duplicates & Data Cleaning
- Duplicate Data
- Causes of Duplicate Data
- Impact of Duplicate Data
- duplicated()
- Counting Duplicates with duplicated().sum()
- Viewing Duplicate Rows
- keep="first"
- keep="last"
- keep=False
- drop_duplicates()
- subset
- Removing Duplicates Based on Specific Columns
- Keeping the Last Duplicate
- Removing All Duplicate Groups
- reset_index()
- reset_index(drop=True)
- Full Row Duplicates vs Column Duplicates
- Data Cleaning
- Data Cleaning Workflow
- Dataset Inspection
- head()
- shape
- info()
- describe()
- isnull().sum()
- dtypes
- Duplicate Data Leakage
- Creating a Data Cleaning Function

---
