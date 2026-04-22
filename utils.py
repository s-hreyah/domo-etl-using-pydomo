from connection import connect_db

import pandas as pd
def get_data(query):
    conn = connect_db()

    if conn:
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    return None