##generic work like reading the data base
import os 
import pandas as pd
from src.mlproject.logger import logging
from src.mlproject.expection import CustomException
import sys
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
pswd = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
        host=host,
        user=user,
        password=pswd,
        db=db
        )
        logging.info("connection established",mydb)
        df = pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df
    except Exception as e:
        raise CustomException

