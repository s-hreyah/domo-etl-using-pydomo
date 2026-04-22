import os

import pandas as pd

from config.env import rfam_family_ds_id
from connection import connect_db
from pydomo_utils import generate_schema_columns, upload_data_to_dataset
from utils import get_data

def fetch_family():
    query = "SELECT * FROM family "
    folder_Name="rfam_output"
    os.makedirs(folder_Name,exist_ok=True)
    df = get_data(query)
    file_path=os.path.join(folder_Name,"rfam_family.csv")
    df.to_csv(file_path,index=False)
    print("CSV saved at:",file_path)

upload_data_to_dataset("rfam_output/rfam_family.csv",rfam_family_ds_id)


