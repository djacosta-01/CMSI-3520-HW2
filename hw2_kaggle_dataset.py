import pandas as pd
import sqlite3

df = pd.read_csv("# DATA FILE")
print(df.head())
print(df.tail())


connection = sqlite3.connect("# DATABASE FILENAME")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS #[table name]")

df.to_sql("#[table name]", connection)
connection.close()