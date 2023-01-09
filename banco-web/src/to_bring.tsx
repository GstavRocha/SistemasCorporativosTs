import React from "react";
import LoginIndex from "./login/index_login";
import Login from "./login/login";

const ToBring =()=>{
    return(
        <div className="coluna">
            <div className="linha1">
                <LoginIndex/>
            </div>
            <div className="linha2">
                <Login/>
            </div>
        </div>
    );
}

export default ToBring;
