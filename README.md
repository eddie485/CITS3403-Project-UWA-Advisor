# CITS3403-Project

Main project for Agile Web Development.

## About
UWA ADVISOR

Our project website is designed to help UWA students with learning about the undergraduate and postgraduate course structure at the University of Western Australia, simultaneously creating a "How To" guide on how to enrol on studentconnect. 
The content of our project elaborates and explains the rules and terms that they must follow when enrolling at UWA. It explains concepts such as undergraduate enrolment, postgraduate enrolment, what to do if a unit changes its course outline, how to switch majors/courses, as well as other definitions that new students should be familiar with when starting off at University.
This content is presented in the form of Bootstrap carousel slides (adapted to the aesthetic and functional needs of our webpage) and is presented in four sections: Undergraduate, Enrolment, Postgraduate, and Additional Information and Definitions
Alongside the contents page there are also multiple choice quizzes to help ensure that the student/user has a good understanding of everything they learn throughout the content slides.
A mock study plan is also available which lets users begin creating a study plan, dragging and dropping their core and complementarity units throughout their undergraduate degree. This was designed in order to help students choose their essential course units so that picking broadening units and electives can be much simpler when it comes to making their real study plans.
The example majors that we selected and that are available in the study plan are Finance and Data Science.

UWA Advisor contains the following pages:
- Login and Registration
- Home
- Contents
> Undergraduate, Enrolment, Postgraduate, Definitions
- Study Plan
> Finance or Data Science (Selecting major redirects you to study plan page for selected major) 
- Quizzes Home Page
> Undergraduate Quiz
> Enrolment Quiz
> Postgraduate Quiz
> Definitions Quiz
> Quiz Results
- Profile and Edit Profile

## Running the Project

Our application uses Python 3.8.5 to run. Please install Python on your computer by typing the following into your command line if you are on linux or using a windows WSL: 
Additionally on windows you must install python off the website available at https://www.python.org/downloads/. 
```
sudo apt-install python3.8
```
Migrations and app.db were deleted in the final commit in order for the selenium testing to be able to be conducted. 
To initialise and start the database:
```
flask db init
flask db migrate -m Usertable
flask db upgrade
flask run
```

Next, you must set up the virtual environment in which the project is run. This can be done through python using the following commands.
In the command line, go to the project's directory and type: 
```
python3 -m venv venv
source venv/bin/activate
```

## Testing

In order to run the unit tests that we have made for the project, open the directory for the project on the command line and enter:
```
python -m unittest discover
```
To run the selenium tests, make sure the database is deleted and then load the selenium_testing.py into a new project in selenium IDE, or use the .side file also included. Deleting the database ensures that proper testing of user registration is possible, by providing a clean slate.


## Running the Website

In order to run the web server locally, with each of the previous steps followed, packages installed and with the .env file in the directory submitted with the project:
Go to the directory for the project on command line and type the following:
```
flask run
```

## Acknowledgements and References
All photos used are photos of the university and is owned by UWA
CSS and Javscript libraries were used from Bootstrap, AJAX and jQuery.


## Creators
This project was made by **Sohail Kharrazi 22707644**, **Michael Tan 22710212**, **Jack Chen 22768692** and **Ervin Basilio 22836721**.
