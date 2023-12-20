import React from 'react';
import './cards.css'

function Player({image,name, position, playerNumber, nationality}) {
    return (
        <div className='card-container'>
            <div className='card'>
            <img src={image} alt={name} />
            <div className='card-content'>   
                <h3 className='card-name'>Name: {name}</h3>
                <p className='card-name'>Jersey Number: {playerNumber}</p>
                <p className='card-body'>Position: {position}</p>
                <p className='card-body'>Nationality: {nationality}</p>
            </div>
            </div>
        </div>
    );
}

export default Player;