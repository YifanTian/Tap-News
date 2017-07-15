import React, { PropTypes } from 'react';
import Auth from '../Auth/Auth';
import './Base.css';

const Base = ({ children }) => (
  <div>
     <nav className="nav-bar indigo lighten-1">
       <div className="nav-wrapper">
         <a href="/" className="brand-logo">  Tap News</a>
         <ul id="nav-mobile" className="right">
           {Auth.isUserAuthenticated() ?
             (<div>
                <li>{Auth.getEmail()}</li>
                <li><a href="/logout">Log out</a></li>
              </div>)
              :
             (<div>
                <li><a href="/login">Log in</a></li>
                <li><a href="/signup">Sign up</a></li>
              </div>)
           }
         </ul>
       </div>
     </nav>
     <br/>
     {children}
   </div>
);

Base.propTypes = {
  children: PropTypes.object.isRequired
};

export default Base;
