# -*- coding: utf-8 -*-
"""PRODIGY_DS_02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fl7QzUd4Rig-loPMF3uh97xcXMpiEhjh
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train_data_path = "/content/train.csv"
df = pd.read_csv(train_data_path)

print(df.head())

missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

df['Age'].fillna(df['Age'].median(), inplace=True)

# Dropping the 'Cabin' column (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

# Filling missing 'Embarked' with the mode (most frequent value)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Verify if missing values have been handled
print("Missing values after cleaning:\n", df.isnull().sum())

# Exploratory Data Analysis (EDA)

# 1. Distribution of Survived
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.show()

# 2. Age distribution of passengers
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

# 3. Survival rate by gender
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()

# 4. Survival rate by passenger class (Pclass)
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.show()

# 5. Correlation heatmap to explore relationships
plt.figure(figsize=(10, 6))
# Select only numeric features for correlation analysis
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

