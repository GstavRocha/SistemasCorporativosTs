import React from "react";
import './login.css';
import {Link} from "react-router-dom";



const Login =()=>{
    return(
      <div>
          <h3 className="signIn">Login</h3>
          <input type="text" className="text"/>
          <Link to={"/banco"}>
                <input type="button" value="ENTRAR" className="Botao"/>
          </Link>
      </div>
    );
}
export default Login;
