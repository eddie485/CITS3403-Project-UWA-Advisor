from flask import render_template
from app import app

@app.route("/")
def login():
    return render_template("welcome-login.html")

@app.route("/register")
def register():
    return render_template("welcome-registration.html")

@app.route("/profile")
def profile():
    return render_template("profile.html", title="Profile")

@app.route("/content-changing-degrees")
def contentChangeDegree():
    return render_template("")

@app.route("/content-definitions")
def contentDefinitions():
    return render_template("contentDefinitions.html")

@app.route("/content-enrolment")
def contentEnrolment():
    return render_template("contentEnrolment.html")

@app.route("/content-postgrad")
def contentPostgrad():
    return render_template("contentPostgrad.html")

@app.route("/content-undergrad")
def contentUndergrad():
    return render_template("contentUndergrad.html")

@app.route("/home-page")
def homePage():
    return render_template("homePage.html")

@app.route("/quiz-homepage")
def quizHome():
    return render_template("quizHomepage.html")

@app.route("/quiz-undergrad")
def quizUndergrad():
    return render_template("quizUndergrad.html")

@app.route("/quiz-handbook")
def quizHandbook():
    return render_template("quizHandbook.html")

if __name__=="__main__":
    app.run(debug=True)