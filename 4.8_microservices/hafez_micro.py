from flask import Flask , jsonify
import hafez
import random

app = Flask(__name__)

@app.route("/fal" , methods=["GET"])
def random_omen():
    poem_id = random.randint(1, hafez.total_poems())
    fal = hafez.get_poem(poem_id)["interpretation"]
    return fal#jsonify({"fal":fal})


if __name__ == "__main__":
    app.run(port=8081)
