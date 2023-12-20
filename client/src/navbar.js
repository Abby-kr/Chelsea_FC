import React from "react";


function Navbar() {
    return (
        <nav className="navbar navbar-expand-md bg-primary py-3">
            <div className="container">
                <h1><a href="/" className="navbar-brand">CHELSEA FC</a></h1>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" 
                data-bs-target="#navmenu">
                <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navmenu">
                    <ul className="navbar-nav ms-auto">
                        <li className="nav-item"><a href="/" className="nav-link">Home</a></li>
                        <li className="nav-item"><a href="/First_Team" className="nav-link">First Team</a></li>
                        <li className="nav-item"><a href="/Womens_Team" className="nav-link">Women's Team</a></li>
                        <li className="nav-item"><a href="/Development_Team" className="nav-link">Development Team</a></li>
                    </ul>
                </div>
             </div>
        </nav>
    );
}

export default Navbar;