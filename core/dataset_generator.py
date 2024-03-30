import pandas as pd
import numpy as np
from faker import Faker
import os

def generate_ecommerce_data(n):
    # Initialize the Faker library for generating realistic data
    fake = Faker()

    # Define the columns and generate data for each column
    data = {
        'username': [fake.user_name() for _ in range(n)],
        'gender': [np.random.choice(['male', 'female', 'unisex']) for _ in range(n)],
        'age': [fake.random_int(min=18, max=80) for _ in range(n)],
        'city': [fake.city() for _ in range(n)],
        'country': [fake.country() for _ in range(n)],
        'product name': [fake.word().title() for _ in range(n)],
        'product details': [fake.text(max_nb_chars=100) for _ in range(n)],
        'product category': [fake.word().title() for _ in range(n)],
        'product sub category': [fake.word().title() for _ in range(n)],
        'price': [round(fake.random_number(digits=5), 2) for _ in range(n)],
        'stock available': [fake.random_int(min=0, max=1000) for _ in range(n)],
        'delivery time': [f"{fake.random_int(min=1, max=14)} days" for _ in range(n)]
    }

    # Create the DataFrame
    df = pd.DataFrame(data)

    # Define the directory and file path
    dir_path = './data'
    file_name = 'ecommerce_data.csv'
    save_path = os.path.join(dir_path, file_name)

    # Check if the directory exists, create it if it does not
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Handle possible errors in file saving
    try:
        df.to_csv(save_path, index=False)
        return f"Data generated successfully and saved to {save_path}"
    except Exception as e:
        return f"Error saving file: {str(e)}"

# Generate a DataFrame with 100 synthetic data records for an e-commerce site
generate_ecommerce_data(100)
