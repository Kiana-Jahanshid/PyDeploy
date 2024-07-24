from flask import Flask , send_file
import qrcode
import requests

app = Flask(__name__)

@app.route("/generate" , methods=["GET"])
def text_2_qrcode():
    result = requests.get("http://127.0.0.1:8080/generate")
    print(result)
    qrcode_image = qrcode.make(result)
    qrcode_image.save("img.png")
    return send_file("img.png", mimetype='image/png') 

if __name__ == "__main__" :
    app.run(port=8083)