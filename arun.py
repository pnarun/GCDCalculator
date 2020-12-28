from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("gcd.html")

if __name__ == '__main__' :
    app.run(port=8000,debug=True)