import csv
import pandas as pd
from faker import Faker

fake = Faker()

# ADD CATEGORIES TO DICT AND FAKE DATA CALL !!!

# placeholder, need to create code to intake data from GUI
columns_info = {'id': 'integer', 'name': 'text', 'salary': 'float'}
column_names = list(columns_info.keys())

# placeholder, need to create code to intake data from GUI
rows_info = 20

df = pd.DataFrame(columns=column_names)

def create_fake_data():
    for i in df.columns:
        fake_data = [fake.name() for _ in range(rows_info)]
        df[i] = fake_data
    print(df)

create_fake_data()
