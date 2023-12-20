import './App.css';
import Navbar from './navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Router>
        <Routes>
          <Route path={"/"} element={<Home/>} />
          <Route path={"/First_Team"} element={<First_Team/>} />
          <Route path={"/Womens_Team"} element={<Womens_Team />} />
          <Route path={"/Development_Team"} element={<Development_Team />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
