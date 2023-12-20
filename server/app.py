
from flask import Flask,make_response,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db,MalePlayer,FemalePlayer

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chelsea.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/subscribers', methods=['GET'])
def get_subscribers():
    subscribers = Subscriber.query.all()
    subscribers_data = [{'name': sub.name, 'email': sub.email} for sub in subscribers]
    return jsonify(subscribers_data)

@app.route('/subscribers', methods=['POST'])
def add_subscriber():
    data = request.get_json()
    new_subscriber = Subscriber(name=data['name'], email=data['email'])
    db.session.add(new_subscriber)
    db.session.commit()
    return jsonify(message='Subscriber added successfully'), 200

@app.route('/First_Team', methods=['GET'])
def get_players():
    players = MalePlayer.query.all()
    players_list = []
    for player in players:
        players_list.append({
            'id': player.id,
            'image':player.image,
            'name':player.name,
            'number': player.playerNumber,
            'position':player.position,
            'nationality': player.nationality
        })

    response = make_response(
        jsonify(players_list),
        200
    )

    return response

@app.route('/Womens_Team', methods=['GET'])
def get_women_players():
    players = FemalePlayer.query.all()
    players_list = []
    for player in players:
        players_list.append({
            'id': player.id,
            'image':player.image,
            'name':player.name,
            'playerNumber': player.playerNumber,
            'position':player.position,
            'nationality': player.nationality
        })

    response = make_response(
        jsonify(players_list),
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555,debug=True)

