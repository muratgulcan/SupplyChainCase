import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('SampleDataset.csv')

df_desc = df.describe()

df_info = df.info()

null_sutunlar = df.columns[df.isnull().any()].tolist()

qualityRating = df['QualityRating']

# plt.figure(figsize=(10, 6))
# sns.histplot(df['QualityRating'], bins=20, kde=True, color='skyblue')

# # Set labels and title
# plt.xlabel('Quality Rating')
# plt.ylabel('Frequency')
# plt.title('Distribution of Quality Ratings')

# # Show the plot
# plt.show()

# supplier_sizes = df['SupplierName'].value_counts()
# supplier_sizes.plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(10, 6), cmap='Set3')
# plt.title('Supplier Distribution')
# plt.show()

# plt.hist(df['CustomerSatisfaction'], bins=20, edgecolor='black')
# plt.title('Distribution of Customer Satisfaction Scores')
# plt.xlabel('Customer Satisfaction')
# plt.ylabel('Frequency')
# plt.show()

# sns.kdeplot(df['CustomerSatisfaction'], fill=True)
# plt.title('Kernel Density Estimate of Customer Satisfaction Scores')
# plt.xlabel('Customer Satisfaction')
# plt.ylabel('Density')
# plt.show()

import pandas as pd
import numpy as np

# Function to identify outliers using IQR
# def find_outliers(column):
#     q1 = np.percentile(column, 25)
#     q3 = np.percentile(column, 75)
#     iqr = q3 - q1
#     lower_bound = q1 - 1.5 * iqr
#     upper_bound = q3 + 1.5 * iqr

#     outliers = (column < lower_bound) | (column > upper_bound)
#     return outliers

# # Identify outliers for each numeric variable
# numeric_columns = df.select_dtypes(include=np.number).columns
# outliers_dict = {col: find_outliers(df[col]) for col in numeric_columns}

# # Display the count of outliers for each variable
# for col, outliers in outliers_dict.items():
#     print(f"Variable '{col}': {outliers.sum()} outliers.")

# corr_matrix = df.corr()

# plt.figure(figsize=(8, 6))
# sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Heatmap")
# plt.show()

from sklearn.preprocessing import LabelEncoder

columns_cat = df.select_dtypes(include=['object']).columns.tolist()

df[columns_cat] = df[columns_cat].fillna(df[columns_cat].mode().iloc[0])

label_encoder = LabelEncoder()
df[columns_cat] = df[columns_cat].apply(lambda col: label_encoder.fit_transform(col))


#numeric_data = df.select_dtypes(include=['int64','float64'])
# numeric_data.hist(figsize=(10,10), bins=60, xlabelsize=6, ylabelsize=6)
# plt.savefig('histogram.png')
# plt.show()

# Assuming df is your DataFrame
sns.scatterplot(x='DefectRate', y='InventoryLevel', data=df)
plt.xticks(rotation=45)
plt.title('Box Plot of DefectRate vs InventoryLevel')
plt.show()



# corr_matrix = df.corr()

# plt.figure(figsize=(12, 12))
# sns_plot = sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
# figure = sns_plot.get_figure()    
# figure.savefig('output.png', dpi=400)
# plt.title("Heatmap")
# plt.show()


