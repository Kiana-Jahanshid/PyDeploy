# for this first we have to pull python docker :
# docker pull python
FROM python
# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
COPY ./app /code/app


RUN pip install sqlite-database
COPY ./app /code/app

# 
CMD ["sqlite3", "/data/initial-db.sqlite" ,"uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]