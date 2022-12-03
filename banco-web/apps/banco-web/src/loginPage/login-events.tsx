import React from 'react';
import './login-events.css';
import * as events from "events";

let LoginButton: events =()=>{
  return(
    <h1>teste</h1>
  )
}
let LoginEvents =()=>{
    return(
        <h1>
          <span>
            <input className="login" type="text" placeholder="Email Address"/>
            <br/>
            <input className="login" type="text" placeholder="Password"/>
          </span>
        </h1>
    );

}
export default {LoginEvents, LoginButton};
