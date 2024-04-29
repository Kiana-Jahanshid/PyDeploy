# app/Dockerfile

FROM python

WORKDIR /8_streamlit/counter_app

RUN git clone https://github.com/Kiana-Jahanshid/PyDeploy.git .

RUN pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "counter", "--server.port=8501", "--server.address=0.0.0.0"]

