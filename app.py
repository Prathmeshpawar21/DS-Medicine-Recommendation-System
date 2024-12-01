from flask import Flask, render_template, request,redirect,jsonify
from research import *

app = Flask(__name__)


@app.route('/index.html', methods=['POST','GET'])
def index():
    userInputSymptomList=""
    PredictedPersonDisease = ""
    desc, diet, med, prec,  work = "","","","",""
    if request.method == 'POST':
        userInputSymptomList = request.form.get("text")
        
        PredictedPersonDisease = get_prediction(userInputSymptomList)
        desc, diet, med, prec,  work = otherDetails(PredictedPersonDisease)
        
        
        
        
        
        
        
        
        
        
    
        
    return render_template("index.html",userInputSymptomList=userInputSymptomList,PredictedPersonDisease=PredictedPersonDisease,desc=desc, diet=diet, med=med, prec=prec,  work=work)



# @app.route("/index.html")
# def index():
#     return render_template("index.html")
    
@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/departments.html")
def departments():
    return render_template("departments.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

    
if __name__ == "__main__":
    app.run(debug=True)
    