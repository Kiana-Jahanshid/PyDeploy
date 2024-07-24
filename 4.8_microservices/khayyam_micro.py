from flask import Flask , jsonify
import khayyam 


app = Flask(__name__)

@app.route("/today" , methods=["GET" , "POST"])
def jalali():
    today = str(khayyam.JalaliDatetime.now().strftime('%C'))
    return today#jsonify({"today":today})

if __name__ == "__main__":
    app.run(port=8082)