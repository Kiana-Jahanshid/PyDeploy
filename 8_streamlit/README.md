# streamlit :

It can design frontend and backend of website with python so quickly . 


# How to run :

```
streamlit run main.py
```

# How to install :
```
pip install -r requirements.txt
```
Then You can now view your Streamlit app in your browser :
<br>
Local URL: http://localhost:8501


## deployment (counter App):
You can see deploy button at the top of that page .

+ in case of using docker :<br>
1_ create requirements.txt in counter.py folder . containing streamlit  <br>
2_ create Dockerfile in this folder (counter_app) 

```
counter_app/
├── counter.py
├── Dockerfile
└── requirements.txt
```
+ Streamlit apps cannot be run from the root directory of Linux distributions. Your main script should live in a directory other than the root directory. so we push our files to github , then write github repository address in Dockerfile :

```
FROM python

WORKDIR /8_streamlit/counter_app
RUN git clone https://github.com/Kiana-Jahanshid/PyDeploy.git .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
COPY  . .
ENTRYPOINT ["streamlit", "run", "counter.py", "--server.port=8501", "--server.address=0.0.0.0"]

```


3_ build a docker image : <br>
```
docker build -t streamlit .
```

4_ Run Docker container :
```
docker run -p 8501:8501 streamlit
```

5_ Deploy on Liara : <br>
```
npx liara login 
npx liara deploy
```

# -----------------------------------------------------------------------------------------


## deployment (data science App):

### How to run :
+ in localhost :
run this command :
```
streamlit run datascience.py
```
then this url will be open ``` http://localhost:8501 ```

<br>
+ deploy using " Streamlit Community Cloud " :
push code on github . <br>
then press deploy in this link  ``` http://localhost:8501 ```