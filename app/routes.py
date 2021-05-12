from app import app
from flask import render_template

@app.route("/")
def login():
    return render_template("welcome-login.html")

@app.route("/registration")
def registration():
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
    return render_template("quizHome.html")

@app.route("/quiz-undergrad")
def quizUndergrad():
    return render_template("quizUndergrad.html")

@app.route("/quiz-postgrad")
def quizPostgrad():
    return render_template("quizPostgrad.html")

@app.route("/quiz-definitions")
def quizDefinitions():
    return render_template("quizDefinitions.html")

@app.route("/quiz-enrolment")
def quizEnrolment():
    return render_template("quizEnrolment.html")

if __name__=="__main__":
    app.run(debug=True)