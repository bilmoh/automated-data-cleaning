import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '../data/data.csv' 
df = pd.read_csv(file_path)

print("Initial Data:")
print(df.head())


def handle_missing_values(df):
    num_imputer = SimpleImputer(strategy='mean')
    df[df.select_dtypes(include=[np.number]).columns] = num_imputer.fit_transform(df.select_dtypes(include=[np.number]))

    cat_imputer = SimpleImputer(strategy='most_frequent')
    df[df.select_dtypes(include=[object]).columns] = cat_imputer.fit_transform(df.select_dtypes(include=[object]))
    
    return df

df_cleaned = handle_missing_values(df)
print("Data after handling missing values:")
print(df_cleaned.head())

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

df_cleaned = remove_duplicates(df_cleaned)
print("Data after removing duplicates:")
print(df_cleaned.head())

output_path = '../reports/cleaned_data.csv'
df_cleaned.to_csv(output_path, index=False)

print(f"Cleaned data saved to {output_path}")
