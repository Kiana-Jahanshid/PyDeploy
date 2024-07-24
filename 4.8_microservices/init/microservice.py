
from flask import Flask, jsonify
 
app = Flask(__name__)
 
@app.route("/hello", methods=['GET'])
def hello_microservice():
    message = {"message": "Hello from the microservice! This is GeeksForGeeks"}
    return jsonify(message)
 
if __name__ == "__main__":
    app.run(port=8000)
