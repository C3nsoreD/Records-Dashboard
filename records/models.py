from records import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

#--- Record Schema
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=False, unique=False)
    lastname = db.Column(db.String(64), index=False, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    factions = db.relationship('Faction', backref='client', lazy=True)
    # dos = db.Column(db.DateTime, index=True, defualt=datetime.utcnow)

    def __repr__(self):
        return '<CLient {} {}'.format(self.firstname, self.lastname)

class Faction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    