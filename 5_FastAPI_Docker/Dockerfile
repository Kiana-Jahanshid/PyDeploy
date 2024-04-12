# for this first we have to pull python docker :
# docker pull python
FROM python
# 
# WORKDIR /code  

# # 
# COPY ./requirements.txt /code/requirements.txt

# # 
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# #
# COPY ./app /code/app

WORKDIR /app  

# 
COPY ./requirements.txt ./requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
#
COPY ./app ./app
# 
CMD ["uvicorn", "app.main:app","--proxy-headers", "--host", "0.0.0.0", "--port", "80"]