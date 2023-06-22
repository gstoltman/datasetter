import csv
import pandas as pd
from faker import Faker

fake = Faker()

def generate_data(column_list):
    row_list = []
    for i in range(len(column_list)):
        method = getattr(fake, column_list[i])
        generated_value = method()
        row_list.append(generated_value)
    return row_list