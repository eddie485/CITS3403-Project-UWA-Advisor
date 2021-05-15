from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data) 

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '': 
            next_page = url_for('homePage') 
        return redirect(next_page)
    return render_template('welcome-login.html', title='Welcome', form=form)

#    error = None 
#    if request.method == "POST":
#        if request.form["username"] != "admin" or request.form["pass"] != "adminpass":
#            error = "You do not have access or your credentials are wrong"
#        else:
#         return redirect(url_for("homePage"))

#    return render_template("welcome-login.html", title="Sign in", error=error)

@app.route("/logout") 
def logout(): 
    logout_user()
    return redirect(url_for('login'))

@app.route("/registration", methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("homePage"))
    form = RegistrationForm()
    if form.validate_on_submit(): 
        user = User(username=form.username.data, email=form.email.data, name=form.name.data, dateofbirth=form.dateofbirth.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations! You are not registered with UWA Advisor") 
        return redirect(url_for("login"))
    return render_template("welcome-registration.html",  title="Create an Account", form=form)

@app.route("/profile")
@login_required
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
@login_required
def homePage():
    return render_template("homePage.html", title="Home Page")

@app.route("/quiz-homepage")
@login_required
def quizHome():
    return render_template("quizHome.html", title="Quiz Home")

@app.route("/quiz-undergrad")
@login_required
def quizUndergrad():
    return render_template("quizUndergrad.html", title="Undergraduate Quiz")

@app.route("/quiz-postgrad")
@login_required
def quizPostgrad():
    return render_template("quizPostgrad.html", title="Postgraduate Quiz")

@app.route("/quiz-definitions")
@login_required
def quizDefinitions():
    return render_template("quizDefinitions.html", title="Definitions Quiz")

@app.route("/quiz-enrolment")
@login_required
def quizEnrolment():
    return render_template("quizEnrolment.html", title="Enrolment Quiz")

@app.route("/test-results")
def quizResults():
    return render_template("testResults.html", title="Tests Results")

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