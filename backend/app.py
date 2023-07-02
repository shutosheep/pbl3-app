from flask import Flask, jsonify, request
import sqlite3
import pandas as pd

# read database data with pandas
connection = sqlite3.connect("data.db")
df = pd.read_sql('SELECT * FROM vendingmachine', connection)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get():
    data = []

    for i in df.index:
        vending_machine = {
            "id": int(df.id[i]),
            "latitude": float(df.latitude[i]),
            "longtitude": float(df.longtitude[i]),
            "cacheless_avilable": int(df.is_cacheless[i])
        }

        data.append(vending_machine)

    return jsonify(data)

if __name__ == "__main__":
    app.run()
