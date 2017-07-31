from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!11111"


@app.route("/<datestr>")
def timestamp(datestr):
    try:
        times = int(datestr)
        return jsonify({"status": "OK",
                        "date": datetime.utcfromtimestamp(times).strftime('%Y-%m-%dT%H:%M:%SZ'),
                        "timestamp": times})
    except ValueError:
        return jsonify({"status": "INVALID_REQUEST"})
