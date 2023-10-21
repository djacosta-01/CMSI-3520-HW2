import pandas as pd
import json
from sqlalchemy import create_engine, Column, String, MetaData, Table

df = pd.read_csv("fifa_dataset/male_teams.csv")
print(f"head: {df.head()}")
print(f"tail: {df.tail()}")

# Getting database credentials 
with open('db_config.json') as db_config:
    config = json.load(db_config)

db_host = config["host"]
db_user = config["user"]
db_password = config["password"]
db_name = config["database"]

# Connecting to MySQL database
db_url = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}'
engine = create_engine(db_url)

# Creating table
table_name = 'fifa_stats'

metadata = MetaData()

columns = [Column(col, String(255)) for col in df.columns]

new_table = Table(table_name, metadata, *columns)

metadata.create_all(engine)

# Uploading dataframe to MySQL
df.to_sql(table_name, engine, if_exists='append', index=False)

# Closing the connection
engine.dispose()

