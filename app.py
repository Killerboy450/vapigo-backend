from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    host="yamabiko.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="dFciWJiyDmyVPuspBZqfatWOBpPvELEn",
    port="52932"
)

cursor = conn.cursor()

@app.route("/book_cab", methods=["POST"])
def book_cab():

    data = request.json

    cursor.execute(
        "INSERT INTO cab_booking (customer_name, mobile, pickup_location, drop_location) VALUES (%s,%s,%s,%s)",
        (data["name"], data["mobile"], data["pickup"], data["drop"])
    )

    conn.commit()

    return jsonify({"status":"success"})

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
