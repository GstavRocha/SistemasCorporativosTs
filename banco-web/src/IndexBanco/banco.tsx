import React from "react";
import Usuario from "./usuario";
import {Link} from "react-router-dom";
import "./banco.css"


const Banco = ()=>{
    return(
        <div className='loginPage'>
            <p>Aqui entra os dados</p>
            <table className="bancouser">
                <thead>
                <tr>
                    <th>Nome do Usuario</th>
                    <th>Operação</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>Fulano</td>
                    <td>
                        <input type="button" value="Deposito"/>
                        <input type="button" value="Pagamento"/>
                        <input type="button" value="Transferência"/>
                    </td>
                </tr>

                </tbody>

            </table>
            <div className='retangulo'>
                <div className="teste"><Usuario/></div>
                <Link to={"/"}>
                    <input type="button" value='voltar'/>
                </Link>
            </div>
        </div>

    );
}
export default Banco;
// Aqui será as operações do usuario
