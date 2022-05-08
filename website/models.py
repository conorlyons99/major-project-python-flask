from . import db
from flask_login import UserMixin


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(128))
    artist_name = db.Column(db.String(128))
    track_name = db.Column(db.String(128), unique=True)
    popularity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    firstName = db.Column(db.String(128))
    songs = db.relationship("Song")

