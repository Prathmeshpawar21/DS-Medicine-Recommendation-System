from flask import Flask, render_template, request,redirect

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template("index.html")




if  __name__ == "__main__":
    print("Hello this is medicine recommendation system")
    # app.run(debug=True)
    