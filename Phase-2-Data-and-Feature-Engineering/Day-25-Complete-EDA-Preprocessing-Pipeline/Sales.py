# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Load Datset
df = pd.read_csv("Day-25-Complete-EDA-Preprocessing-Pipeline\Sales_Dataset.csv")

# Basic Inspection
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.describe())
print(df.dtypes)
print(df.columns.tolist())

# Checking missing values
print("Missing Values:\n", df.isnull().sum())

# Missing values percentage
missing_percentage = (df.isnull().sum() / len(df))*100
print("Missing Values Percentage:\n", missing_percentage)

# Checking duplicates
print("Duplicates:", df.duplicated().sum())

# Checking missing values
print( df["gender"].unique())
print( df["country"].unique())
print( df["subscription_type"].unique())

# Value count
print( df["gender"].value_counts())
print( df["country"].value_counts())
print( df["subscription_type"].value_counts())

print( df['churn'].value_counts())
print(df['churn'].value_counts(normalize=True))

# Visualize the target
sns.countplot( df, x="churn")
plt.title("Customer Churn Distribution")
plt.show()

# Converting dates
df['signup_date'] = pd.to_datetime( df["signup_date"] )
df["last_purchase_date"] = pd.to_datetime( df["last_purchase_date"] )

# Removing unnecessary columns
df = df.drop("customer_id", axis=1)

# Customer_tenure_days
df["customer_tenure_days"] = (
    df["last_purchase_date"] - df["signup_date"]
).dt.days

numerical_features = [
    "age",
    "is_premium_user",
    "total_visits",
    "avg_session_time",
    "pages_per_session",
    "email_open_rate",
    "email_click_rate",
    "total_spent",
    "avg_order_value",
    "discount_used",
    "support_tickets",
    "refund_requested",
    "delivery_delay_days",
    "satisfaction_score",
    "nps_score",
    "marketing_spend_per_user",
    "lifetime_value",
    "last_3_month_purchase_freq",
    "customer_tenure_days"
]

categorical_features = [
    "gender",
    "country",
    "city",
    "acquisition_channel",
    "device_type",
    "subscription_type",
    "coupon_code",
    "payment_method"
]


# # Imputing missing values
# numeric_imputer = SimpleImputer(strategy="mean")
# categorical_imputer = SimpleImputer(strategy="most_frequent")


# # Numeric Scaling
# scaler = StandardScaler()
# encoder = OneHotEncoder(handle_unknown="ignore")


# Numeric Pipeline
numeric_pipeline = Pipeline(steps=[
    ("imputer",SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())    
])

# Categorical Pipeline
Categorical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            numeric_pipeline,
            numerical_features
        ),
        (
            "cat",
            Categorical_pipeline,
            categorical_features
        )
    ]
)

# Separate features and target
X = df.drop("churn", axis=1)
y = df["churn"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split( X,y, test_size=0.2, random_state=42)

# Fit on training data
X_train_processed = preprocessor.fit_transform(X_train)

# Fit on Testing data
X_test_processed = preprocessor.transform(X_test)


# Checking the shape
print("Features Shape:", X.shape)
print("Target Shape:", y.shape)


# Final shape
print("Training_shape:", X_train_processed.shape)
print("Tesing_shape:",X_test_processed.shape)

# Target shape
print("y_train:",y_train.shape)
print("y_test:",y_test.shape)