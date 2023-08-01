from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemon.db'

db = SQLAlchemy(app)


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    base_experience = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)


class PokemonSchema(Schema):
    id = fields.Integer()
    base_experience = fields.Integer()
    height = fields.Integer()
    weight = fields.Integer()
    name = fields.String()
    image_url = fields.String()