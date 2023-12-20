import React,{useEffect, useState} from 'react';
import Player from './Player';

function FirstTeam() {
    const [firstTeam,setFirstTeam] = useState([])

    useEffect(() => {
        fetch('http://localhost:5000/First_Team')
        .then((r) => r.json())
        .then((fetchData) => setFirstTeam(fetchData))
        .catch(error => {console.error('Fetch Error:', error)})
    },[])

    return (
        <div className="player-lists">
            <h1 id='firstteam-heading'>First Team players</h1>
            {firstTeam.map((player, index) => 
            <Player 
                key={index} 
                image={player.image}
                name={player.name} 
                position={player.position}
                playerNumber={player.playerNumber}
                nationality={player.nationality}/>
            )}  
        </div>
    );
}

export default FirstTeam;