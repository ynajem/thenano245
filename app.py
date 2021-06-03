from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def root():
  return "Hello, World!"


@app.route("/index.html")
@app.route("/index.php")
def home():
  return redirect("/")


@app.route("/user/<username>")
def user_template(username):
  return render_template("user.html", name=username)


@app.route("/json")
def data():
  return {
      "name": "NAJEM UNESS",
      "email": "y.najem@gmail.com"
  }


@app.route("/submit", methods=['POST', 'GET'])
def submit():
  if(request.method == "POST"):
    return request.form
  return "No data has benn sent!"
