from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True) #nullable = False)
    password_hash = db.Column(db.String(128)) #nullable = True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


#Adding progress class for later when we want to implement individual user progress in a database and connect it via relationships to the primary key user ID
#class Progress(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    progresspercent = db.Column(db.Integer) - depends how we're going to display the user progress (% or as string (e.g. 100% or "completed: Undergraduate")
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#    def __repr__(self):
#        return 'Progress {}>'.format(self.progresspercent);
