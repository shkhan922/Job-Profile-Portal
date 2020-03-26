import React from 'react';
import { NavLink } from 'react-router-dom';

import './NavLinks.css';

const NavLinks = props => {
 return <ul className='nav-links'> 
       <li> <NavLink to="/jobprofile/new"> Resume Upload</NavLink>
       </li>
       <li> <NavLink to="/"> Login</NavLink>
       </li>
       <li> <NavLink to="/"> Register </NavLink>
       </li>
       <li> <NavLink to="/"> About Us </NavLink>
       </li>
  </ul> 

};

export default NavLinks;