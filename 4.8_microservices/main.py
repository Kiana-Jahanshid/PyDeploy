import os
import requests
from flask import Flask , jsonify , send_file


os.environ['NO_PROXY'] = '127.0.0.1'
NO_PROXY = {
    'no': 'pass',
}


app = Flask(__name__)


@app.route("/generate" , methods=["GET", "POST"])
def result():
    fal =   requests.get("http://127.0.0.1:8081/fal")#, verify=False , proxies=NO_PROXY ,allow_redirects=False
    today =  requests.get("http://127.0.0.1:8082/today")
    # fal = fal.json()
    # today = today.json()
    return jsonify({"fal":fal.text , "today":today.text})


@app.route("/" , methods=["GET"])
def qrcode_result():
    qrcode_image = requests.get("http://127.0.0.1:8083/")
    return jsonify({"qrcode_image" : qrcode_image})


if __name__ == "__main__" :
    app.run(port=8080)