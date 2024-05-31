from flask import Flask , render_template , request

app = Flask(import_name="__init__" , template_folder="" , static_folder=".venv/static")


# here our GOAL is to design a website
# so we have to return HTML format ( not json , ....)
@app.route("/" , methods=['GET'])
def root():
    name = "kiki"
    x="8"
    return  render_template(".venv/templates/index.html" , name=name , x=x)


@app.route("/download")
def download():
    media = ["image" , "music" , "movie"]
    return render_template(".venv/templates/download.html" , media=media)



@app.route("/me")
def me():
    myinfo = {"fname":"kiki" , 
              "lname":"jhn"}
    return myinfo

@app.route("/blog" , methods=["GET" , "POST"])
def blog():
    if request.method == "GET" :
        return "this is get method"
    elif request.method == "POST" :
        return "this is post method"



# HOW TO RUN 
#flask --app init run --debug


# we put html files in templates folder


# create virtual environmets :
'''
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
> .venv/Scripts/activate
$ pip install Flask

'''


# because LIARA supports flask , SO we dont need to write Dockerfile
# https://docs.liara.ir/cicd/github/