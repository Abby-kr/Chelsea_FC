from flask import Flask,make_response,jsonify
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
    app.run(port=5555,rdebug=True)