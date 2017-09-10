import React from 'react';
import ReactDOM from 'react-dom';
import App from './App/App';
import './index.css';

// import LoginPage from './Login/LoginPage';
// import SignUpPage from './SignUp/SignUpPage';

import { browserHistory, Router } from 'react-router';
import routes from './routes';

ReactDOM.render(
  // <SignUpPage />,
  <Router history = {browserHistory} routes={routes}/>,
  document.getElementById('root')
)
