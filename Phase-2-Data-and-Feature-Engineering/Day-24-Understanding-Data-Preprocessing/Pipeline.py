import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

df = pd.read_csv("Day-24-Understanding-Data-Preprocessing\Sales_Dataset.csv")

df["last_purchase_date"] = pd.to_datetime(df["last_purchase_date"])
df["signup_date"] = pd.to_datetime(df["signup_date"])

df["customer_tenure_days"] = ( df["last_purchase_date"] - df["signup_date"]).dt.days

numeric_features = [
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

category_features = [
    "gender",
    "country",
    "city",
    "acquisition_channel",
    "device_type",
    "subscription_type",
    "coupon_code",
    "payment_method"
]

# Numeric Pipeline
numeric_pipleline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler",StandardScaler())
    ]
)

# Category Pipeline
category_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("Encoder", OneHotEncoder(handle_unknown="ignore"))
    ]
)

# Combining both -  Column Transformer
preprocessor = ColumnTransformer(
    transformers=[
        ("num",numeric_pipleline, numeric_features),
        ("cat", category_pipeline, category_features)
    ]
)


X = df.drop('churn', axis=1)
y = df['churn']


X_train, X_test, y_train, y_test = train_test_split( X,y, test_size=0.2, random_state=42, stratify=y)

X_trained_processor = preprocessor.fit_transform(X_train)
X_tested_processor = preprocessor.transform(X_test)


print("X_train:",X_train.shape)
print("X_test:",X_test.shape)
print("y_train:",y_train.shape)
print("y_test:",y_test.shape)

print()

print("X_train_processor:",X_trained_processor.shape)
print("X_test_processor:",X_tested_processor.shape)