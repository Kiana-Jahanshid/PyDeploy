FROM python

WORKDIR /9_streamlit_SQLModel
RUN git clone https://github.com/Kiana-Jahanshid/PyDeploy.git .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
COPY  . .
ENTRYPOINT ["streamlit", "run", "authenticator.py", "--server.port=8501", "--server.address=0.0.0.0"]