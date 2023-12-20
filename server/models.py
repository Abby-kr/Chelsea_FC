from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MalePlayer(db.Model):
    __tablename__ = 'male_players'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    playerNumber = db.Column(db.String, unique=True, nullable=False)
    position = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Player: {self.name}>'

class FemalePlayer(db.Model):
    __tablename__ = 'female_players'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    playerNumber = db.Column(db.String, unique=True, nullable=False)
    position = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Player: {self.name}>'
    
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)