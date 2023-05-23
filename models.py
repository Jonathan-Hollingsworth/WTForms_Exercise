from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    "Initiates the connection to the database"
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """The basic model for all pets"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(20), nullable=False)

    species = db.Column(db.String(25), nullable=False)

    photo_url = db.Column(db.String(70))

    age = db.Column(db.Integer)

    notes = db.Column(db.String)

    available = db.Column(db.Boolean, nullable=False, default=True)