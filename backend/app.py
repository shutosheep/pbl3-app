from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import pandas as pd

# read database data with pandas
connection = sqlite3.connect("data.db")
v_df = pd.read_sql('SELECT * FROM vendingmachine', connection)
m_df = pd.read_sql('SELECT * FROM menu', connection)

# https://zenn.dev/straydog/articles/5ba6d234c7e72f886a5e
app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)

@app.route("/", methods=["GET"])
def get():
    data = []

    for i in v_df.index:
        location = [float(v_df.latitude[i]), float(v_df.longtitude[i])]
        vending_machine = {
            "id": int(v_df.id[i]),
            "location": location,
        }

        data.append(vending_machine)

    return jsonify(data)

@app.route("/menu", methods=["GET"])
def get_menu():
    id = request.args.get("id")
    data = []

    for i in m_df.index:
        if int(m_df.id[i]) == int(id):
            menu = {
                "name": str(m_df.name[i]),
                "price": int(m_df.price[i]),
            }

            data.append(menu)

    return jsonify(data)

@app.route("/location", methods=["GET"])
def get_location():
    id = request.args.get("id")
    data = []

    for i in v_df.index:
        if int(v_df.id[i]) == int(id):
            location = {
                "location": [float(v_df.latitude[i]), float(v_df.longtitude[i])],
            }
            data.append(location)

    return jsonify(data)

@app.route("/filter", methods=["GET"])
def get_filter():
    filter_type = request.args.get("filter_type")
    filter_value = request.args.get("filter_value") # optional, mandatory for filter_type is name or price
    data = []

    if filter_type == "name":
        for i in m_df.index:
            j = m_df.id[i]
            if str(m_df.name[i]) == str(filter_value):
                location = [float(v_df.latitude[j - 1]), float(v_df.longtitude[j - 1])]
                vending_machine = {
                    "id": int(j),
                    "location": location,
                }

                data.append(vending_machine)
    elif filter_type == "ict":
        for i in v_df.index:
            if int(v_df.is_cacheless[i]) == int(1):
                location = [float(v_df.latitude[i]), float(v_df.longtitude[i])]
                vending_machine = {
                    "id": int(v_df.id[i]),
                    "location": location,
                }

                data.append(vending_machine)
    elif filter_type == "price":
        for i in m_df.index:
            j = m_df.id[i]
            if int(m_df.price[i]) <= int(filter_value):
                location = [float(v_df.latitude[j - 1]), float(v_df.longtitude[j - 1])]
                vending_machine = {
                    "id": int(j),
                    "location": location,
                }

                data.append(vending_machine)

    return jsonify(data)

if __name__ == "__main__":
    app.run()
