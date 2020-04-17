from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager 
# User admin 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128)) 

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    # implementing password hashing for super users
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

#--- Record Schema
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=False, unique=False)
    lastname = db.Column(db.String(64), index=False, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    factions = db.relationship('Faction', backref='client', lazy=True)
    # dos = db.Column(db.DateTime, index=True, defualt=datetime.utcnow)

    def __repr__(self):
        return '<Client {} {}'.format(self.firstname, self.lastname)

class Faction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    