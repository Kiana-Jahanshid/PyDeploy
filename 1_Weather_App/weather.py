import http.client
import requests
import json
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import pandas as pd
from datetime import date


def search():
    
    user_text = window.user_input.text()
    response = requests.get(f"https://goweather.herokuapp.com/weather/{user_text}")
    data = json.loads(response.text)
    print(data)

    tomorrow , dayـafterـtomorrow , three_days_hence = day_name()
    window.today_temp.setText(data["temperature"])
    window.today_wind.setText(data["wind"])
    window.Wind.setText("Wind :")
    window.today_desc.setText(data["description"])
    window.farda_temp.setText(data["forecast"][0]["temperature"])
    window.farda_wind.setText(data["forecast"][0]["wind"])
    window.pasfarda_temp.setText(data["forecast"][1]["temperature"])
    window.pasfarda_wind.setText(data["forecast"][1]["wind"])
    window.pasoonfarda_temp.setText(data["forecast"][2]["temperature"])
    window.pasoonfarda_wind.setText(data["forecast"][2]["wind"])
    window.farda.setText(tomorrow)
    window.pasfarda.setText(dayـafterـtomorrow)
    window.pasoonfarda.setText(three_days_hence)

    if data["description"] == "Sunny" :
        window.image.setIcon(QIcon('assets/sun/6.png'))
        window.image.setIconSize(QSize(195, 165))
    elif data["description"] == "Partly cloudy" :
        window.image.setIcon(QIcon('assets/sun/27.png'))
        window.image.setIconSize(QSize(190, 160)) 
    elif data["description"] == "Cloudy" :
        window.image.setIcon(QIcon('assets/cloud/29.png'))
        window.image.setIconSize(QSize(190, 160))
    elif data["description"] == "Rainy" :
        window.image.setIcon(QIcon('assets/cloud/7.png'))
        window.image.setIconSize(QSize(190, 160))
    elif data["description"] == "Clear" :
        window.image.setIcon(QIcon('assets/moon/10.png'))
        window.image.setIconSize(QSize(180, 150))
    elif data["description"] == "Thunderstorm" :
        window.image.setIcon(QIcon('assets/cloud/24.png'))
        window.image.setIconSize(QSize(180, 150))

    # show_icon = [window.image , window.img_farda , window.img_pasfarda , window.img_pasoonfarda ]
    # for i in range(4):
    #     window.img_farda.setIcon(QIcon('assets/cloud/29.png'))
    #     window.img_farda.setIconSize(QSize(90, 80))      
    #     window.img_pasfarda.setIcon(QIcon('assets/cloud/7.png'))
    #     window.img_pasfarda.setIconSize(QSize(90, 80))
    #     window.img_pasoonfarda.setIcon(QIcon('assets/cloud/35.png'))
    #     window.img_pasoonfarda.setIconSize(QSize(90, 80))

def day_name():
    days = ("Saturday" , "Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday", "Friday")
    d = date.today()
    d = pd.Timestamp(d)
    today = d.day_name()
    print(today)
    threedays = []
    for i , item in enumerate(days) :
        if item == today :
            if i == 6 :
                threedays.append([days[i-6] , days[i-5] , days[i-4] ])
            elif i == 5 :
                threedays.append([days[i+1] , days[i-5] , days[i-4] ])
            elif i == 4 :
                threedays.append([days[i+1] , days[i+2] , days[i-4] ])
            else :
                threedays.append([days[i+1] , days[i+2] , days[i+3] ])
    tomorrow , dayـafterـtomorrow , three_days_hence = threedays[0][0] , threedays[0][1] , threedays[0][2]
    return tomorrow , dayـafterـtomorrow , three_days_hence
    

weather_app = QApplication([])
#load ui file 
loader = QUiLoader()
window = loader.load("weather.ui")
window.show()

user_text = window.user_input.text()
window.search.clicked.connect(search)

weather_app.exec()
