from turtle import position
from models import db,MalePlayer,FemalePlayer
from flask_sqlalchemy import SQLAlchemy
from app import app

with app.app_context():
    player1 = MalePlayer(image='https://i2-prod.football.london/incoming/article27286314.ece/ALTERNATES/s1200c/0_GettyImages-1258244500.jpg',name='Raheem Sterling',playerNumber='7',position='Forward',nationality='English')
    player2 = MalePlayer(image='https://static.wikia.nocookie.net/the-football-database/images/b/b8/Robert_S%C3%A1nchez.png/revision/latest?cb=20210110010241',name='Robert Sanchez',playerNumber='1',position='Goalkeeper',nationality='English')
    player3 = MalePlayer(image='https://cdn1.unitedinfocus.com/uploads/14/2023/01/GettyImages-1245365487-scaled.jpg',name='Axel Disasi',playerNumber='2',position='Defender',nationality='French')
    player4 = MalePlayer(image='https://cdn1.unitedinfocus.com/uploads/14/2023/01/GettyImages-1245365487-scaled.jpg',name='Marc Cucurella',playerNumber='3',position='Defender',nationality='Spanish')
    player5 = MalePlayer(image='https://phantom-marca.unidadeditorial.es/4e8adc45c4be46f17ea15d85a7b57bf2/resize/828/f/jpg/assets/multimedia/imagenes/2023/01/05/16729275440848.jpg',name='Benoit Badiashile',playerNumber='5',position='Defender',nationality='French')
    player6 = MalePlayer(image='https://i2-prod.football.london/incoming/article28069737.ece/ALTERNATES/s615/0_GettyImages-1779855118.jpg',name='Thiago Silva',playerNumber='6',position='Defender',nationality='Brazilian')
    player7 = MalePlayer(image='https://cdn1.thechelseachronicle.com/uploads/17/2023/10/GettyImages-1644452290.jpg',name='Enzo Fernández',playerNumber='8',position='Midfielder',nationality='Argentinian')
    player8 = MalePlayer(image='https://e0.365dm.com/22/12/2048x1152/skysports-mudryk-mykhaylo_6007407.jpg?20221228122132',name='Mykhaylo Mudryk',playerNumber='10',position='Forward',nationality='Ukrainian')
    player9 = MalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNxc1pKFNLTKiJ2xFvN1Qo1ZTnlyD7cFTdmYAiK15Um1GuXrSuEn9PtqlfHeMFEAWN9BA&usqp=CAU',name='Nicolas Jackson',playerNumber='15',position='Forward',nationality='Senegalese')
    player10 = MalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfiEiN47PyXQRkuwXpOtmoD4gtEhDd65G-dnhqZCTTtK1tf-oQPIBS4ZtSO7Ige92sV8k&usqp=CAU',name='Marcus Bettinelli',playerNumber='13',position='Goalkeeper',nationality='British')
    player11 = MalePlayer(image='https://i2-prod.football.london/incoming/article27144977.ece/ALTERNATES/s615/0_GettyImages-1243930749.jpg',name='Trevoh Chalobah',playerNumber='14',position='Defender',nationality='English')

    db.session.add_all([player1, player2, player3, player4, player5, player6 ,player7, player8, player9, player10, player11])
    db.session.commit()


    player1 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCZl8vFwUWLYnitN_-OJcG3B3BJN-ZreoFNw&usqp=CAU',name='Zecira Musovic',playerNumber='1',position='Goalkeeper',nationality='Swedish')
    player2 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsYVer0-QCYOQGsG83RHCNC9FbB3B7Am8uXQ&usqp=CAU',name='Aniek Nouwen',playerNumber='3',position='Centre-Back',nationality='Dutch')
    player3 = FemalePlayer(image='https://www.fifplay.com/img/fc/24/players/238257.png',name='Millie Bright',playerNumber='4',position='Centre-back',nationality='British')
    player4 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTirWVkknfOYWDbxpMj0AKPXr2z2E-yGr4ycw&usqp=CAU',name='Jess Carter',playerNumber='7',position='Full-back',nationality='British')
    player5 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPExpgJVIQvH383Qu0-bwSzGWUnL_ERVbhAQ&usqp=CAU',name='Sjoeke Nusken',playerNumber='6',position=' Midfielder',nationality='German')
    player6 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0qJPampU62BfzrDNP3AMn-x5xKwzPH7Vqig&usqp=CAU',name='Jessie Fleming',playerNumber='17',position='Midfielder',nationality='Canadian')
    player7 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhXTQylOCFsKtfeORPkA_Ine38hKdJMFtu3Q&usqp=CAU',name='Melanie Leupolz',playerNumber='8',position='Midfielder',nationality='German')
    player8 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTL8HB0hdWFzJff8hBNzkVZVAJX0gttdlUgxA&usqp=CAU',name='Catarina Macario',playerNumber='9',position='Striker',nationality='Brazilian')
    player9 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLcWmYqprHYnHcgwt0i7UhEm30B-BHZcXj5w&usqp=CAU',name='Lauren James',playerNumber='10',position='Forward',nationality='British')
    player10 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQvgMJ4KIZRsJ3tK8ABfcDCjyqMYjDIZa00w&usqp=CAU',name='Guro Reiten',playerNumber='11',position='Winger',nationality='Norweigiean')
    player11 = FemalePlayer(image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlqHNrnIF1U4ey0-Qd1YHfhr-Ul9dyLYyhXQ&usqp=CAU',name='Sam Kerr',playerNumber='20',position='Striker',nationality='Australian')

    db.session.add_all([player1, player2, player3, player4, player5, player6 ,player7, player8, player9, player10, player11])
    db.session.commit()