from flask import Flask, render_template, request,redirect,jsonify
from research import *
import ast

app = Flask(__name__)


@app.route('/index.html', methods=['POST', 'GET'])
def index():
    userInputSymptomList = ""
    PredictedPersonDisease = ""
    desc, diet, med, prec, work = "", [], [], [], []
    
    if request.method == 'POST':
        userInputSymptomList = request.form.get("text")
        PredictedPersonDisease = get_prediction(userInputSymptomList)
        
        # Assuming these values are returned as string representations of lists
        desc, diet, med, prec, work = otherDetails(PredictedPersonDisease)
        
        # Convert string representations to actual lists using ast.literal_eval
        if isinstance(diet, str):
            diet = ast.literal_eval(diet)
        if isinstance(med, str):
            med = ast.literal_eval(med)
        if isinstance(prec, str):
            prec = ast.literal_eval(prec)
        if isinstance(work, str):
            work = ast.literal_eval(work)
    

        
        print(type(diet))
        print(type(med))
        print(type(prec))
        print(type(work))

        
    return render_template("index.html", 
                           userInputSymptomList=userInputSymptomList, 
                           PredictedPersonDisease=PredictedPersonDisease, 
                           desc=desc, diet=diet, med=med, prec=prec, work=work)






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
    