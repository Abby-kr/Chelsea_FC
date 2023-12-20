import React from "react";


function Navbar() {
    return (
        <nav class="navbar navbar-expand-md bg-primary py-3">
            <div class="container">
                <h1><a href="/" class="navbar-brand">CHELSEA FC</a></h1>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" 
                data-bs-target="#navmenu">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navmenu">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a href="/" class="nav-link">Home</a></li>
                        <li class="nav-item"><a href="/First_Team" class="nav-link">First Team</a></li>
                        <li class="nav-item"><a href="/Womens_Team" class="nav-link">Women's Team</a></li>
                        <li class="nav-item"><a href="/Development_Team" class="nav-link">Development Team</a></li>
                    </ul>
                </div>
             </div>
        </nav>
    );
}

export default Navbar;