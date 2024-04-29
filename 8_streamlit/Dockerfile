# app/Dockerfile

FROM python

#WORKDIR /8_streamlit/counter_app
WORKDIR /8_streamlit/counter_app
RUN git clone https://github.com/Kiana-Jahanshid/PyDeploy.git .

RUN pip3 install -r requirements.txt

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "counter.py", "--server.port=8501", "--server.address=0.0.0.0"]

