import React from "react";
import './login.css';

const Login =()=>{
    return(
      <div>
          <h3 className="signIn">Login</h3>
          <input type="text" className="text"/>
          <input type="button" value="ENTRAR" className="Botao"/>
      </div>
    );
}
export default Login;
