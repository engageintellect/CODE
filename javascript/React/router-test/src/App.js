import "./App.css";

import Nav from "./Components/Nav";
import Footer from "./Components/Footer";
import Home from "./Pages/Hello";
import About from "./Pages/About";
import Hello from "./Pages/Hello";

// ----------------------------------------------
// IMPORT ROUTER

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// ----------------------------------------------

function App() {
  return (
    <Router>
      <Nav />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/hello" element={<Hello />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
