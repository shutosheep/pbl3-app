from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import pandas as pd

# read database data with pandas
connection = sqlite3.connect("data.db")
df = pd.read_sql('SELECT * FROM vendingmachine', connection)

# https://zenn.dev/straydog/articles/5ba6d234c7e72f886a5e

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)

@app.route("/", methods=["GET"])
def get():
    data = []

    for i in df.index:
        location = [float(df.latitude[i]), float(df.longtitude[i])]
        vending_machine = {
            "id": int(df.id[i]),
            "location": location,
            "cacheless_avilable": int(df.is_cacheless[i]),
        }

        data.append(vending_machine)

    return jsonify(data)

if __name__ == "__main__":
    app.run()
