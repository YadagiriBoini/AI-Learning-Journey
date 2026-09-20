import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "age": [20, 21, 22, 23, 24, 21, 22, 25],
    "study_hours": [2, 3, 4, 5, 6, 3, 5, 7],
    "attendance": [70, 75, 80, 85, 90, 78, 88, 95],
    "department": ["AI", "CSE", "AI", "ECE","CSE", "AI", "ECE", "CSE"],
    "passed": [0, 0, 1, 1, 1, 0, 1, 1]
})


print(df.head()) 
print(df.tail())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print(df.info())
print(df.describe())
print(df.describe(include="object"))
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["department"].unique())
print(df["department"].nunique())
print(df["department"].value_counts())
print(df["passed"].value_counts(normalize=True))
plt.hist(df["study_hours"])
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.title("Study Hours Distribution")
plt.show()
plt.boxplot(df["attendance"])
plt.ylabel("Attendance")
plt.title("Attendance Distribution")
plt.show()
print(df["study_hours"].corr(df["attendance"]))
print(df.corr())
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
plt.scatter(df["study_hours"], df["attendance"])
plt.xlabel("Study Hours")
plt.ylabel("Attendence")
plt.show()
df["department"].value_counts().plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Count")
plt.title("Students by Department")
plt.show()
print(pd.crosstab( df["department"], df["passed"]))
print(df.groupby("department")["study_hours"].mean())
print(df.groupby("department")["attendance"].agg(["mean", "median", "max"]))
df["age"].describe()
plt.hist(df["age"])
plt.show()
plt.scatter(df["study_hours"], df["attendance"])
plt.show()
sns.pairplot(df, hue="passed")
plt.show()
print(df["attendance"].skew())
