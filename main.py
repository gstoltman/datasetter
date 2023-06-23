import csv
import pandas as pd
from faker import Faker

fake = Faker()

category_dict = {
    'random_int': 'ID',
    'name': 'Name',
    'country': 'Country',
    'address': 'Address',
    'job': 'Job',
    'phone_number': 'Phone Number'
}

def generate_data(column_list):
    row_list = []
    for i in range(len(column_list)):
        method = getattr(fake, column_list[i])
        generated_value = method()
        row_list.append(generated_value)
    return row_list