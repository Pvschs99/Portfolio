from flask import *

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")
@app.route("/projects")
def projects():
    return render_template('projects.html')
@app.route("/contactinfo")
def contactinfo():
    return render_template('contactinfo.html')
if __name__=="__main__":
    app.run(debug=True)