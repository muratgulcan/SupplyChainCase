import pandas as pd
import numpy as np
import random
from faker import Faker

# Set a random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Create a Faker instance for generating fake data
fake = Faker()

# Number of records in the dataset
num_records = 1000
num_suppliers = 10

# Generate Supplier Data
supplier_data = pd.DataFrame({
    'SupplierID': [f'S{i}' for i in range(1, num_suppliers + 1)],
    'SupplierName': [f'S{i}' for i in range(1, num_suppliers + 1)],
    'SupplierLocation': [fake.city() for _ in range(num_suppliers)],
    'QualityRating': np.random.uniform(3.5, 5.0, num_suppliers).round(2),
    'LeadTimeDays': np.random.randint(7, 30, num_suppliers)
})

# Duplicate supplier rows to reach the desired total number of records
supplier_data = pd.concat([supplier_data] * (num_records // num_suppliers), ignore_index=True)

# Trim excess rows if necessary
supplier_data = supplier_data.head(num_records)

# Shuffle the rows for randomness
supplier_data = supplier_data.sample(frac=1, random_state=42).reset_index(drop=True)

# Generate Production Data
production_data = pd.DataFrame({
    'ProductionID': [f'P{str(i).zfill(4)}' for i in range(1, num_records + 1)],
    'CycleTimeHours': np.random.uniform(12, 48, num_records).round(2),
    'ProductionVolume': np.random.randint(50, 200, num_records),
    'DefectRate': np.random.uniform(0.1, 5.0, num_records).round(2)
})

# Generate Logistics Data
logistics_data = pd.DataFrame({
    'LogisticsID': [f'L{str(i).zfill(3)}' for i in range(1, num_records + 1)],
    'TransportationLeadTimeDays': np.random.randint(1, 10, num_records),
    'InventoryLevel': np.random.randint(100, 500, num_records)
})

# Generate Market Data
market_data = pd.DataFrame({
    'MarketID': [f'M{str(i).zfill(3)}' for i in range(1, num_records + 1)],
    'SalesVolume': np.random.randint(20, 150, num_records),
    'DemandForecast': np.random.randint(30, 200, num_records),
    'CustomerSatisfaction': np.random.uniform(3.5, 5.0, num_records).round(2)
})

# Merge the datasets
df = pd.merge(supplier_data, production_data, left_index=True, right_index=True)
df = pd.merge(df, logistics_data, left_index=True, right_index=True)
df = pd.merge(df, market_data, left_index=True, right_index=True)

# Save the dataset to a CSV file
df.to_csv('auto_tech_dataset.csv', index=False)

# Display the first few rows of the generated dataset
print(df.head())
