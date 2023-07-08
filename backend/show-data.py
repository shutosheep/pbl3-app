import sqlite3
import pandas as pd

pd.set_option('display.max_rows', None)

# read database data with pandas
connection = sqlite3.connect("data.db")
v_df = pd.read_sql('SELECT * FROM vendingmachine', connection)
m_df = pd.read_sql('SELECT * FROM menu', connection)

print(v_df)
print("==========")
print(m_df)
