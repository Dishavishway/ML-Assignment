import random
from faker import Faker
import pandas as pd
import numpy as np

fake = Faker()


# Function to generate random occupation
def generate_occupation():
    occupations = ['Engineer', 'Artist', 'Teacher', 'Doctor', 'Lawyer', 'Nurse']
    return random.choice(occupations)

# Function to generate income based on occupation
def generate_income(occupation):
    income_ranges = {
    'Engineer': (60000, 100000),
    'Artist': (40000, 70000),
    'Teacher': (35000, 60000),
    'Doctor': (80000, 150000),
    'Lawyer': (70000, 120000),
    'Nurse': (50000, 80000)
    }
    return random.randint(*income_ranges[occupation])

# Function to generate purchase decision
def generate_purchase():
    return random.choice(['Yes', 'No'])

# Generate the dataset
def generate_dataset(num_records):
    data = []
    for _ in range(num_records):
        name = fake.first_name()
        age = random.randint(22, 60)
        gender = random.choice(['Male', 'Female'])
        occupation = generate_occupation()
        income = generate_income(occupation)
        purchased = generate_purchase()
        data.append([name, age, gender, occupation, income, purchased])
    return pd.DataFrame(data, columns=['Name', 'Age', 'Gender', 'Occupation', 'Income', 'Purchased'])

def add_null(data, null_fraction=0.1):
    for col in data.columns:
        if col != 'Purchased':
            data.loc[data.sample(frac=null_fraction).index, col] = np.nan


df = generate_dataset(5000)
add_null(df, null_fraction=0.1)

print(df.head())

# Save the dataset to a CSV file
df.to_csv('generated_dataset.csv', index=False)