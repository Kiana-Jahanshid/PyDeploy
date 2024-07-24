
from flask import Flask, jsonify
import requests
 
import os
os.environ['NO_PROXY'] = '127.0.0.1'
requests.packages.urllib3.disable_warnings()


app = Flask(__name__)
 
 
# Calling the random number generator microservice
def call_random_microservie():
    response = requests.get("http://127.0.0.1:8007/ge" , verify=False)
    return response.json().get("random_number")
 
@app.route("/check", methods=['GET'])
def check_even_odd():
    random_number = call_random_microservie()
    result = "even" if random_number % 2 == 0 else "odd"
    return jsonify({"random_number": random_number, "result": result})
 
if __name__ == "__main__":
    app.run(port=8002)
