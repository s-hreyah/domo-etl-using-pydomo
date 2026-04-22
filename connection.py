import mysql.connector
from config.env import DB_CONFIG

def connect_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("Connected successfully")
        return conn
    except Exception as e:
        print("Connection error:", e)
        return None




