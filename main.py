from flask import Flask, render_template, Response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import time
import json
import requests

app = Flask(__name__)
# auth = HTTPBasicAuth()
# users = {
    # "usr": generate_password_hash("pass"),
# }

# @auth.verify_password
# def verify_password(username, password):
#     if username in users and check_password_hash(users.get(username), password):
#         return username

try:
    with open("config.json", "r") as f:
        cfg = json.load(f)
except FileNotFoundError:
    cfg = {"IPs": [["Local", "127.0.0.1:3545"]]}
    with open("config.json", "w") as f:
        json.dump(cfg, f)


names = []
for k, v in cfg["IPs"]:
    names.append(k)

@app.route("/")
# @auth.login_required
def main():
    with open("index.html", "r") as f:
        file = f.read().replace("{{CFG}}", str(names))
    return file


@app.route("/<string:device>/<path:path>")
# @auth.login_required
def subDeviceRouting(device, path):
    for k, v in cfg["IPs"]:
        if k == device:
            ip = v
    if ip is None:
        return f"Device {device} not found"
    newPath = 'http://' + ip + '/' + path
    return requests.get(newPath).content

@app.route("/RobotoMono-Regular.ttf")
def font():
    with open("RobotoMono-Regular.ttf", "rb") as f:
        file = Response(f.read(), mimetype='font/tff')
    return file

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3546)
