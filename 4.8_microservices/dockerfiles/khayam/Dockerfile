FROM python

WORKDIR /app2

COPY . /app2

RUN pip install --no-cache-dir Flask khayyam

# Make port 8082 available outside container
EXPOSE 8082
ENV FLASK_APP=khayyam_micro.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8082"]