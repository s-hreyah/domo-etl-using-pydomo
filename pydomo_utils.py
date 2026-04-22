import sys

import pandas
import pandas as pd
from pydomo import Domo, Column, ColumnType, Schema, DataSetRequest

from config.env import client_id, client_secret, domo_base_url, api_host


def create_dataset(df,ds_name):
    try:
        domo=Domo(client_id,client_secret,api_host=api_host)
        ds_id = domo.ds_create(df, ds_name)
        return ds_id
    except Exception as e:
        print("Unable to create dataset:", e)
        sys.exit(1)




def generate_schema_columns(header_with_types):
    schema_columns = []
    for column_info in header_with_types:
        col_name=column_info['column']
        col_type=column_info['type']

        if pandas.api.types.is_integer_dtype(col_type):
            if "id" in col_name.lower():
                schema_type=ColumnType.INTEGER
            else:
                schema_type=ColumnType.LONG
        elif pandas.api.types.is_float_dtype(col_type):
            schema_type=ColumnType.DOUBLE
        elif "date" in col_name.lower():
            schema_type=ColumnType.DATE
        elif "time" in col_name.lower() or col_name.lower()=="_batch_last_run":
            schema_type=ColumnType.TIME
        else:
            schema_type=ColumnType.STRING
        schema_columns.append(Column(schema_type, col_name))
    return schema_columns


def get_csv_file_header(file_path):
    dataframe=pandas.read_csv(file_path, encoding="utf-8")
    column_info=[{'column':col, 'type':dtype} for col,dtype in dataframe.dtypes.items()]
    return column_info


def update_dataset(domo,ds_id,update_headers):
    try:
        update=DataSetRequest()
        columns=generate_schema_columns(update_headers)
        print(columns)
        update.schema=Schema(columns)
        datasets=domo.datasets
        datasets.update(ds_id,update)
        print("datasets updated")
    except Exception as e:
        print("Unable to update dataset:", e)
        sys.exit(1)

def upload_data_to_dataset(csv_file_path,ds_id,method="REPLACE"):
    try:
        domo=Domo(client_id,client_secret,api_host=api_host)
        dataframe=pandas.read_csv(csv_file_path)
        headers=[{'column':col, 'type':dtype} for col,dtype in dataframe.dtypes.items()]
        update_dataset(domo,ds_id,headers)
        datasets=domo.datasets
        datasets.data_import_from_file(ds_id,csv_file_path,update_method=method)
        print(f"datasets uploaded from {csv_file_path} to {ds_id}")
        return True
    except Exception as e:
        print("Unable to upload dataset:", e)
        sys.exit(1)

if __name__ == "__main__":
    df=pd.read_csv("rfam_output/rfam_full_region.csv",nrows=100)
    id=create_dataset(df,"rfam_full_region")
    print("dataset created", id)

