import React from "react";
import s from "./Navbar.module.css";
import { NavLink } from "react-router-dom";

const Navbar = (props) => {
  return (
    <nav className={s.Nav}>
      <div>
        <NavLink to="/profile" className={(navData) => (navData.isActive ? s.active : s.item)}>Profile</NavLink>
      </div>
      <div>
        <NavLink to="/dialogs" className={(navData) => (navData.isActive ? s.active : s.item)}>Messages</NavLink>
      </div>
      <div>
        <NavLink to="/photos" className={(navData) => (navData.isActive ? s.active : s.item)}>Photos</NavLink>
      </div>
      <div>
        <NavLink to="/users" className={(navData) => (navData.isActive ? s.active : s.item)}>Users</NavLink>
      </div>
      <div>
        <p>
        <NavLink to="/settings" className={(navData) => (navData.isActive ? s.active : s.item)}>Settings</NavLink>
        </p>
      </div>
    </nav>
  );
};

export default Navbar;
