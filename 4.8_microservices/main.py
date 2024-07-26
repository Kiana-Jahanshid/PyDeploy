import os
import requests
from flask import Flask , jsonify , send_file
import json 

os.environ['NO_PROXY'] = '127.0.0.1'
NO_PROXY = {
    'no': 'pass',
}


app = Flask(__name__)


@app.route("/merge" , methods=["GET", "POST"])
def result():
    fal =   requests.get("http://127.0.0.1:8081/fal")#, verify=False , proxies=NO_PROXY ,allow_redirects=False
    today =  requests.get("http://127.0.0.1:8082/today")
    # fal = fal.json()
    # today = today.json()
    text = f'{{"fal":{fal.text} , "today":{today.text} }}'
    j = json.dumps(text, indent=2)     
    j = str(json.loads(j))
    print(j)
    return j


if __name__ == "__main__" :
    app.run(port=8080)