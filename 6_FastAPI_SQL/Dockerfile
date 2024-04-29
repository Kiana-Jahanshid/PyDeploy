# FROM python

# WORKDIR /Expert_mode  

# # 
# COPY ./requirements.txt ./requirements.txt

# # 
# RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
# #
# COPY ./Expert_mode ./Expert_mode
# # 
# CMD ["uvicorn", "Expert_mode.main:app","--proxy-headers", "--host", "0.0.0.0", "--port", "80"]



FROM python

WORKDIR /Expert_mode

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./Expert_mode ./Expert_mode


CMD ["uvicorn", "Expert_mode.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]