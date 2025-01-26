import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/monitor/all">Monitor All</Link></li>
        <li><Link to="/monitor/select">Monitor Select</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
