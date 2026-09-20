# AIML Roadmap — Phase 1 & Phase 2

## Phase 1 — Foundations
### Day 1 — Python Functions + Data Structures
- Python Functions
- Lists
- Dictionaries
- Sets

### Day 2 — Comprehensions + Lambda
- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- Lambda Functions

### Day 3 — Object-Oriented Programming
- Classes
- Objects
- Constructors
- Methods
- OOP Basics

### Day 4 — Exception Handling + File Handling
- Exception Handling
- `try`
- `except`
- `else`
- `finally`
- File Handling
- Reading Files
- Writing Files

### Day 5 — NumPy Foundations
- NumPy
- NumPy Arrays
- Array Creation
- Array Indexing
- Array Slicing
- Array Shapes
- Array Data Types

### Day 6 — NumPy Manipulation + Matrix Operations
- Array Reshaping
- Array Manipulation
- Array Concatenation
- Array Splitting
- Matrix Operations
- Matrix Addition
- Matrix Subtraction
- Matrix Multiplication

### Day 7 — NumPy Statistics + Broadcasting + Linear Algebra
- Mean
- Median
- Variance
- Standard Deviation
- Broadcasting
- Linear Algebra with NumPy
- Dot Product

### Day 8 — Pandas Foundations
- Pandas
- Series
- DataFrames
- Creating DataFrames
- Reading CSV Files
- Selecting Rows and Columns
- Filtering Data

### Day 9 — Pandas Data Cleaning
- Missing Values
- `isnull()`
- `fillna()`
- `dropna()`
- Duplicate Values
- `drop_duplicates()`
- Data Type Conversion

### Day 10 — Matplotlib
- Matplotlib
- Line Plot
- Bar Plot
- Scatter Plot
- Histogram
- Figure
- Labels
- Titles
- Legends

### Day 11 — Seaborn
- Seaborn
- Statistical Visualization
- Count Plot
- Box Plot
- Violin Plot
- Histogram
- Heatmap

### Day 12 — Vectors + Matrices
- Vectors
- Scalars
- Matrices
- Vector Operations
- Matrix Operations
- Dot Product
- Matrix Multiplication

### Day 13 — Probability + Conditional Probability + Bayes
- Probability
- Probability Rules
- Conditional Probability
- Independent Events
- Bayes Theorem

### Day 14 — Normal Distribution + Correlation + Covariance
- Normal Distribution
- Mean
- Standard Deviation
- Correlation
- Covariance
- Correlation vs Covariance

### Day 15 — Derivatives + Gradient + Phase 1 Review
- Derivatives
- Basic Derivative Rules
- Gradient
- Gradient Direction
- Gradient Descent Concept
- Phase 1 Review

---

## Phase 2 — Data + Feature Engineering
### Day 16 — Feature Engineering Foundations
- Features
- Targets
- `X`
- `y`
- Numerical Features
- Categorical Features
- Binary Features
- Ordinal Features
- Feature Engineering
- Derived Features
- Mathematical Features
- Interaction Features
- Polynomial Features
- Date/Time Features
- Feature Selection
- Data Leakage

### Day 17 — Handling Missing Data
- Missing Data
- `NaN`
- Detecting Missing Values
- `isnull()`
- `isna()`
- `dropna()`
- Mean Imputation
- Median Imputation
- Mode Imputation
- Constant Imputation
- Forward Fill
- Backward Fill
- Missing Data vs Zero
- Data Leakage During Imputation
- `SimpleImputer`

### Day 18 — Encoding Categorical Data
- Categorical Data
- Nominal Data
- Ordinal Data
- Encoding
- Label Encoding
- Ordinal Encoding
- One-Hot Encoding
- `OneHotEncoder`
- `OrdinalEncoder`
- `drop="first"`
- Binary Encoding
- Multiple Categorical Columns
- Unknown Categories
- `handle_unknown="ignore"`
- `fit()`
- `transform()`
- `fit_transform()`
- Encoding Data Leakage

### Day 19 — Feature Scaling
- Feature Scaling
- Why Feature Scaling is Important
- Distance-Based Algorithms
- Standardization
- `StandardScaler`
- Mean
- Standard Deviation
- Min-Max Normalization
- `MinMaxScaler`
- StandardScaler vs MinMaxScaler
- Effect of Outliers on Scaling
- `RobustScaler`
- Scaling Training Data
- Scaling Test Data
- Data Leakage During Scaling

### Day 20 — Outliers
- Outliers
- Outliers vs Anomalies
- Quartiles
- Q1
- Q2
- Q3
- IQR
- IQR Outlier Rule
- Lower and Upper Bounds
- Box Plots
- Z-Score
- Z-Score Outlier Detection
- Boolean Masking
- Handling Outliers
- Removing Outliers
- Capping/Winsorization
- Log Transformation
- `RobustScaler`
- Domain Knowledge

### Day 21 — Data Cleaning
- Data Cleaning
- Duplicate Data
- Duplicate Detection
- `duplicated()`
- `drop_duplicates()`
- Invalid Values
- Inconsistent Data
- Data Type Checking
- Data Quality

### Day 22 — Train / Validation / Test Split
- Training Data
- Validation Data
- Test Data
- Train-Test Split
- `train_test_split()`
- `test_size`
- `random_state`
- Stratified Split
- `stratify`
- `X_train`
- `X_test`
- `y_train`
- `y_test`

### Day 23 — Exploratory Data Analysis
- Exploratory Data Analysis
- Dataset Inspection
- `head()`
- `tail()`
- `shape`
- `columns`
- `dtypes`
- `info()`
- `describe()`
- Missing Value Analysis
- Duplicate Analysis
- Unique Values
- `unique()`
- `nunique()`
- `value_counts()`
- Target Distribution
- Histograms
- Box Plots
- Scatter Plots
- Correlation Analysis
- Correlation Matrix
- Heatmap
- `corr()`
- `groupby()`
- `agg()`
- `pd.crosstab()`
- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis
- `pairplot()`
- Skewness
- Data Leakage Detection

### Day 24 — Understanding Data Preprocessing
- Features and Targets
- Input Features (`X`)
- Target Variable (`y`)
- Identifying the Target Column
- Feature Selection
- Unnecessary Columns
- Identifier Columns
- Data Leakage Columns
- Feature Engineering
- Derived Features
- Customer Tenure
- Calculating Customer Tenure
- Numerical Features
- Categorical Features
- Manual Data Preprocessing with Pandas
- `fillna()`
- `SimpleImputer`
- Why Pipelines Are Used
- Numerical Pipeline
- Categorical Pipeline
- `Pipeline`
- `ColumnTransformer`
- `fit()`
- `transform()`
- `fit_transform()`
- `X_train`
- `X_test`
- `y_train`
- `y_test`
- `X_train_processed`
- Training vs Test Preprocessing
- Data Leakage During Preprocessing
- Manual Preprocessing vs Pipeline-Based Preprocessing

### Day 25 — Complete EDA + Preprocessing Pipeline
- Complete EDA Workflow
- Dataset Inspection
- Missing Value Analysis
- Duplicate Analysis
- Categorical Data Analysis
- Target Distribution Analysis
- Date Conversion
- Date-Based Feature Engineering
- Customer Tenure Feature
- Invalid Data Detection
- Numerical Feature Selection
- Categorical Feature Selection
- Feature and Target Separation
- Train-Test Split
- Numerical Data Imputation
- Categorical Data Imputation
- Numerical Feature Scaling
- One-Hot Encoding
- `Pipeline`
- `ColumnTransformer`
- `fit()`
- `transform()`
- `fit_transform()`
- Data Leakage Prevention


