FROM python

WORKDIR /app3

COPY . /app3
RUN pip install --no-cache-dir Flask

# Make port 8080 available outside container
EXPOSE 8080
ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]