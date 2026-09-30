from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/home",methods=["POST","GET"])
def home():
    if(request.method == "POST"):
        name = request.form.get("name")
        bussiness = request.form.get("business")
        state = request.form.get("state")
        city = request.form.get("city")
        exp = request.form.get("exp")
        print("name: ",name)
        print("bussiness: ",bussiness)
        print("location: ",state,",",city)
        print("exp: ",exp)


    return render_template("home.html")


app.run(debug = True)
