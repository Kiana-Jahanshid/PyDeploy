FROM python

WORKDIR /app4

COPY . /app4
RUN pip install --no-cache-dir Flask qrcode

# Make port 8083 available outside container
EXPOSE 8083
ENV FLASK_APP=qrcode_micro.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8083"]