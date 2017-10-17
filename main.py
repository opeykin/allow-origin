from flask import Flask, Response, request
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return "Usage: url + site api request. Will mirror request with allow origin *"


@app.route("/<path:path>")
def redirect(path):
    r = requests.get("https://" + path, params=request.args)
    resp = Response(r.text)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
