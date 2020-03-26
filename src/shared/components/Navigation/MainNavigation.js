import React from 'react';
import { Link,NavLink } from 'react-router-dom';

import MainHeader from './MainHeader'
import NavLinks from './NavLinks'
import './MainNavigation.css'
import './NavLinks.css'

const MainNavigation = props => {
    return <MainHeader>
        <button className='main-navigation__menu-btn'>
            <span/> 
            <span/> 
            <span/>
        </button>
        <div className='header__logo'> <a href='/'>The Logo</a></div> 
        <div className='spacer' />
         <div className='main-navigation__title'><Link to="/"><h2 className='navitem'>What to do Next</h2></Link></div>
        <div className='spacer' />
        <nav className='navitem'> <NavLinks/> </nav>
    </MainHeader>

};

export default MainNavigation;