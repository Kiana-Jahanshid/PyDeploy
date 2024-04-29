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


## deployment :
You can see deploy button at the top of that page .

+ in case of using docker :
1_ create requirements.txt in file.py folder . containing streamlit , numpy , opencv-python <br>
2_ create Dockerfile in this folder  ,use previous Dockerfile , but instead of uvicorn , write streamlit command :
["streamlit" , "run" , "" , ""]  <br> 
3_ build docker <br>
4_ send to liara <br>


+ in case of selecting cloud :
```
1_ push code on github <br>
your-repository/
├── your_app.py
└── requirements.txt



for changing color theme  and other visualizations  , and change these parameter in config file : 
your-repository/
├── .streamlit/
│   └── config.toml
├── your_app.py
└── requirements.txt



2_  in this address : share.streamlit.io
press new app
paste github link 

branch = main
main file path = file_name.py
subdomain : name of site

```