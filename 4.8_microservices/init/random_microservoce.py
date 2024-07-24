
from flask import Flask, jsonify
import random
 
app = Flask(__name__)
 
@app.route("/ge", methods=['GET'])
def generate_random_number():
    random_number = random.randint(1, 1000)
    return jsonify({"random_number": random_number})
 
if __name__ == "__main__":
    app.run(port=8007)
