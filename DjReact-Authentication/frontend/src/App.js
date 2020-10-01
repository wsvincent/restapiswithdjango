import React from 'react';
import './bootstrap.min.css';
import './index.css';
import {BrowserRouter,Route} from 'react-router-dom'
import Home from './components/Home.js';
import Login from './components/Login.js';
import Logout from './components/Logout.js';
import Register from './components/Register.js';
  
function App() {
    return (
        <React.Fragment>
        <br/>
        <div className="container jumbotron">
            <BrowserRouter>
                <Route exact path="/" component={Home} />
                <Route exact path="/login" component={Login} />
                <Route exact path="/logout" component={Logout} />
                <Route exact path="/register" component={Register} />
            </BrowserRouter>
        </div>
        </React.Fragment>
    );
}

export default App;
