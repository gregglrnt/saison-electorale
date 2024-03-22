import React from "react";
import logo from '../assets/redlogo.png'

const TopBar = () => {
  return (
      <div className="top-bar">
        <img src={logo} className="logo" alt="logo"/>
        <div className="title-container">
          <h1 className="title">Saison électorale</h1>
          <h3 className="subTitle">Qui est le plus fort entre le soleil et le vote ?</h3>
        </div>
      </div>
  );
}

export default TopBar