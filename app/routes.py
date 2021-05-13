from app import app
from flask import render_template

@app.route("/")
def login():
    return render_template("welcome-login.html", title="UWA Enrolment and Studies Guide")

@app.route("/registration")
def registration():
    return render_template("welcome-registration.html",  title="Create an Account")

@app.route("/profile")
def profile():
    return render_template("profile.html", title="Your Profile")

@app.route("/content-definitions")
def contentDefinitions():
    return render_template("contentDefinitions.html", title="Additional Information and Definitions")

@app.route("/content-enrolment")
def contentEnrolment():
    return render_template("contentEnrolment.html", title="Enrolling in Your First Undergraduate Degree")

@app.route("/content-postgrad")
def contentPostgrad():
    return render_template("contentPostgrad.html", title="Postgraduate Degrees at UWA")

@app.route("/content-undergrad")
def contentUndergrad():
    return render_template("contentUndergrad.html", title="The Undergraduate Degree at UWA")

@app.route("/home-page")
def homePage():
    user = {"username": "Jack"}
    return render_template("homePage.html", title="Home Page", user=user)

@app.route("/quiz-homepage")
def quizHome():
    return render_template("quizHome.html", title="Quiz Home")

@app.route("/quiz-undergrad")
def quizUndergrad():
    return render_template("quizUndergrad.html", title="Undergraduate Quiz")

@app.route("/quiz-postgrad")
def quizPostgrad():
    return render_template("quizPostgrad.html", title="Postgraduate Quiz")

@app.route("/quiz-definitions")
def quizDefinitions():
    return render_template("quizDefinitions.html", title="Definitions Quiz")

@app.route("/quiz-enrolment")
def quizEnrolment():
    return render_template("quizEnrolment.html", title="Enrolment Quiz")

@app.route("/study-plan")
def studyPlan():
    return render_template("studyPlan.html", title="Study Plan Builder")

@app.route("/study-plan-DS")
def studyPlanDS():
    return render_template("studyPlanDS.html", title="Study Plan - Data Science")

@app.route("/study-plan-FINA")
def studyPlanFINA():
    return render_template("studyPlanFINA.html", title="Study Plan - Finance")

if __name__=="__main__":
    app.run(debug=True)