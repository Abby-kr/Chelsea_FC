import './App.css';
import Navbar from './navbar';
import FirstTeam from './FirstTeam';
import WomensTeam from './WomensTeam';
import DevelopmentTeam from './DevelopmentTeam';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Router>
        <Routes>
          {/* <Route path={"/"} element={<Home/>} /> */}
          <Route path={"/First_Team"} element={<FirstTeam/>} />
          <Route path={"/Womens_Team"} element={<WomensTeam />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
