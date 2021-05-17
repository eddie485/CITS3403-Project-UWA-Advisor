from app import app, db
<<<<<<< HEAD
from app.models import User, Score
from app.forms import LoginForm, RegistrationForm
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
=======
from app.models import User
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

# Main/index route is the login page
# Users are asked to put in their credentials for log in, assuning they already have an account
# If the input passes validation they are redirected to the homepage
#The below code is adapted from Miguel Grinberg's Flask Megatutorial to fit our project's functionality.

@app.route("/", methods=['GET', 'POST'])
def login():
    #Following two lines redirects the user to the UWA Advisor home page once login is authenticated.
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))

>>>>>>> 9f62ff49539933333c8bcee755047354eee4bfaa
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
<<<<<<< HEAD
=======

        login_user(user, remember=form.remember_me.data) 
        
>>>>>>> 9f62ff49539933333c8bcee755047354eee4bfaa
        login_user(user, remember=form.remember_me.data) 

        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '': 
            next_page = url_for('homePage') 
        return redirect(next_page)
<<<<<<< HEAD
    return render_template('welcome-login.html', title='Welcome', form=form)

=======

    return render_template('welcome-login.html', title='Welcome', form=form)

# OLD ADMIN LOGIN
#
>>>>>>> 9f62ff49539933333c8bcee755047354eee4bfaa
#    error = None 
#    if request.method == "POST":
#        if request.form["username"] != "admin" or request.form["pass"] != "adminpass":
#            error = "You do not have access or your credentials are wrong"
#        else:
#         return redirect(url_for("homePage"))
<<<<<<< HEAD

#    return render_template("welcome-login.html", title="Sign in", error=error)
=======
#
#    return render_template("welcome-login.html", title="Sign in", error=error)
#
>>>>>>> 9f62ff49539933333c8bcee755047354eee4bfaa

@app.route("/logout") 
def logout(): 
    logout_user()
    return redirect(url_for('login'))

<<<<<<< HEAD
=======

# Route for welcome-registration.html
# Uses RegistrationForm and asks new users for their details
# Details are then validated to make sure there are no replicates of the unique ones before they are all saved into the database
#The below code is adapted from Miguel Grinberg's Flask Megatutorial to fit our project's functionality.


>>>>>>> 9f62ff49539933333c8bcee755047354eee4bfaa
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("homePage"))
    form = RegistrationForm()
    if form.validate_on_submit(): 
        user = User(username=form.username.data, email=form.email.data, name=form.name.data, 
                                        dateofbirth=form.dateofbirth.data, major=form.major.data, 
                                                studentid=form.studentid.data, year=form.year.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations! You are not registered with UWA Advisor") 
        return redirect(url_for("login"))
    return render_template("welcome-registration.html",  title="Create an Account", form=form)

@app.route("/profile")
@login_required
def profile():
    form = EditProfileForm()
    return render_template("profile.html", title="Your Profile", form=form)


# Route for profileEdit.html
# Shows user's current account info and also lets users edit their information, 
# the form then overwrites it's values in the database

@app.route("/profile-edit", methods=['GET', 'POST'])
@login_required
def profileEdit():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.major = form.major.data
        current_user.year = form.year.data
        current_user.dateofbirth = form.dateofbirth.data
        current_user.studentid = form.studentid.data
        current_user.name = form.name.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.major.data = current_user.major
        form.year.data = current_user.year
        form.dateofbirth.data = current_user.dateofbirth
        form.studentid.data = current_user.studentid
        form.name.data = current_user.name

    return render_template('profileEdit.html', title='Edit Profile', form=form)


# The remaining routes bellow are all links to their respective html pages

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

@app.route("/submit/<int:quiz_id>", methods=["PUT"])
def submit(quiz_id):
    if request.method == "PUT":
        data = request.get_json()
        score = Score.query.filter_by(userid=current_user.id, quiz_id = quiz_id).first()
        print("recieve score put request: score={} in quiz {}".format(data['score'], quiz_id))

        if score is None:
            print("score is none")
            print("score set to {}".format(data['score']))
            new_score = Score(
                score=data['score'],
                quiz_id = quiz_id,
                userid= current_user.id)
            db.session.add(new_score)
            db.session.commit()

        elif score.score < data['score']:
            score.score = data['score']
            print("update score to {}".format(score.score))
            db.session.commit()

    return jsonify({"status": "Ok"})

if __name__=="__main__":
    app.run(debug=True)