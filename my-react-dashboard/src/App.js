import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import MonitorAll from "./pages/MonitorAll";
import MonitorSelect from "./pages/MonitorSelect";
import "./styles/styles.css";

function App() {
  return (
    <Router>
      <Header />
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/monitor/all" element={<MonitorAll />} />
        <Route path="/monitor/select" element={<MonitorSelect />} />
      </Routes>
    </Router>
  );
}

export default App;
