import csv
import pandas as pd
from faker import Faker

fake = Faker()

# ADD CATEGORIES TO DICT AND FAKE DATA CALL !!!

# placeholder, need to create code to intake data from GUI


# placeholder, need to create code to intake data from GUI


def create_fake_data(row_count):
    columns_info = {
    'random_int': {'category': 'random_int', 'datatype': 'integer'},
    'name': {'category': 'name', 'datatype': 'text'},
    'country': {'category': 'country', 'datatype': 'text'}
    }

    column_names = list(columns_info.keys())

    df = pd.DataFrame(columns=column_names)

    for outer_key, inner_dict in columns_info.items():
        method = getattr(fake, outer_key)
        fake_data = [method() for _ in range(row_count)]
        df[outer_key] = fake_data
    print(df)

create_fake_data(6)