from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'  
db = SQLAlchemy(app)

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
