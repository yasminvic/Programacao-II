# importações
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# configurações
app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'animais.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.Text)
    raca = db.Column(db.Text)
    cor = db.Column(db.Text)
    genero = db.Column(db.Text)
    type = db.Column(db.Text)

    __mapper_args__ = {
        'polymorphic_identity':'animal', 
        'polymorphic_on':type,
    }


class Gato(Animal):
    id = db.Column(db.Integer, db.ForeignKey('animal.id'), primary_key = True)
    fugas = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity':'gato',
    }

class Cachorro(Animal):
    id = db.Column(db.Integer, db.ForeignKey('animal.id'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity':'cachorro',
    }

with app.app_context():
    db.create_all()

    gato1 = Gato(nome = 'Merlin', raca = 'negro', cor = 'branco', genero = 'gay', fugas = 10)
    cachorro1 = Cachorro(nome = 'Bilu', raca = 'negra', cor = 'amarelo', genero = 'homossexual')

    db.session.add(gato1)
    db.session.add(cachorro1)
    db.session.commit()

