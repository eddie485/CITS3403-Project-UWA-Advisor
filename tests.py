import unittest
from app import app, db
from app.models import User
from config import Config

class TestConfig(Config):

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserTesting(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_password(self):
        
        user1 = User(username='mike', year = 3, email = 'mike@email.com')
        user1.set_password('passphrase')

        db.session.add(user1)
        db.session.commit()
        self.assertFalse(user1.check_password('password'))
        self.assertTrue(user1.check_password('passphrase'))

    def test_duplicate_email(self):
        user1 = User(username='mike', year = 3, email = 'mike@email.com')
        user2 = User(username='ed', year = 3, email = 'mike@email.com')

        self.assertEqual(user1.email, user2.email)

if __name__ == '__main__':
    unittest.main()