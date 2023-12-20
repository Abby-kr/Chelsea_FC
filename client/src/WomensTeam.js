import React,{useEffect, useState} from 'react';
import FemalePlayer from './FemalePlayer';

function WomensTeam() {
    const [womensTeam,setWomensTeam] = useState([])

    useEffect(() => {
        fetch('http://localhost:5000/Womens_Team')
        .then((r) => r.json())
        .then((fetchData) => setWomensTeam(fetchData))
        .catch(error => {console.error('Fetch Error:', error)})
    },[])

    return (
        <div className="player-lists">
            <h1 id='womensteam-heading'>Chelsea's Women's Team</h1>
            {womensTeam.map((player, index) => 
            <FemalePlayer 
                key={index} 
                image={player.image}
                name={player.name} 
                playerNumber={player.playerNumber}
                position={player.position}
                nationality={player.nationality}/>
            )}
        </div>
    );
}

export default WomensTeam;