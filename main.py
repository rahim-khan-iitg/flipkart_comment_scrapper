from functions import *
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def hello():
    if request.method=="POST":
        link=request.form.get('link')
        data=[]
        get_data(link,data)
        return render_template("index.html",data=data)
    return render_template("index.html",data=[[]])

app.run(debug=True,host="0.0.0.0")