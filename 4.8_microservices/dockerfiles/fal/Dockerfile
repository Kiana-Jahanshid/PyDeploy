FROM python

WORKDIR /app1

COPY . /app1

RUN pip install --no-cache-dir Flask hafez

# Make port 8081 available outside container
EXPOSE 8081
ENV FLASK_APP=hafez_micro.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8081"]