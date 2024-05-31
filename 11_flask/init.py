from flask import Flask , render_template ,render_template_string

app = Flask(import_name="test", template_folder='templates' )


# here our GOAL is to design a website
# so we have to return HTML format ( not json , ....)
@app.route("/")
def root():
    return  render_template("index.html")



# HOW TO RUN 
# flask --app init run 


# we put html files in templates folder