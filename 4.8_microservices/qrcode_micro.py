from flask import Flask , send_file
import qrcode
import requests
import json
from io import BytesIO


app = Flask(__name__)

@app.route("/qr" , methods=["GET", "POST"])
def text_2_qrcode():
    response = requests.get("http://127.0.0.1:8080/merge")
    text = response.text
    qrcode_image = qrcode.make(text)
    img = BytesIO()    
    qrcode_image.save(img, 'PNG')

    img.seek(0)
    return send_file(img , mimetype='image/png') 

if __name__ == "__main__" :
    app.run(port=8083)