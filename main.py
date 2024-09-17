from flask import Flask, render_template, Response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import threading
import time
import json

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
    cfg = {"IPS": [["Local", "127.0.0.1:3545"]]}
    with open("config.json", "w") as f:
        json.dump(cfg, f)

@app.route("/")
# @auth.login_required
def main():
    with open("index.html", "r") as f:
        file = f.read().replace("{{CFG}}", str(cfg))
    return file

@app.route("/RobotoMono-Regular.ttf")
def font():
    with open("RobotoMono-Regular.ttf", "rb") as f:
        file = Response(f.read(), mimetype='font/tff')
    return file

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3546)
