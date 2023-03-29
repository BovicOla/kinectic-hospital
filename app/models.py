
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    age = db.Column(db.Integer())
    phone_number = db.Column(db.String(16))
    address = db.Column(db.String(256))
    gender = db.Column(db.Enum('male', 'female', name='gender'))
    employment = db.Column(
        db.Enum('student', 'employed', 'self employed', 'unemployed',
                'ful time job', 'part time job')
    )
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.firstname} {self.lastname.upper()})>'
