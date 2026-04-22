import os

import pandas as pd

from config.env import rfam_family_ds_id, rfam_full_region_ds_id
from connection import connect_db
from pydomo_utils import upload_data_to_dataset
from utils import get_data


def fetch_full_region_ds():

    limit=100000
    offset=0

    folder_Name="rfam_output"
    os.makedirs(folder_Name,exist_ok=True)
    file_path = os.path.join(folder_Name, "rfam_full_region.csv")
    first_write=True



    while True:
        try:
            query = f"SELECT * FROM full_region limit {limit} offset {offset} "
            df = get_data(query)

            if df is None or df.empty:
                break
            df.to_csv(file_path, mode='a', index=False, header=first_write)
            print(f"Fetched rows from offset {offset}")

            first_write = False
            offset += limit
        except Exception as e:
            print(e)
            break

upload_data_to_dataset("rfam_output/rfam_full_region.csv",rfam_full_region_ds_id)
