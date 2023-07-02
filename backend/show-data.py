import sqlite3
import pandas as pd

# read database data with pandas
connection = sqlite3.connect("data.db")
df = pd.read_sql('SELECT * FROM vendingmachine', connection)

print(df)
