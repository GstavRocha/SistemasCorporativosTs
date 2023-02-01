import React from "react";
import Usuario from "./usuario";
import {Link} from "react-router-dom";
import {useState, useEffect} from "react";
import "./banco.css"
import axios from "axios";


const Banco = ()=>{
    const [body, setBody] = useState('')
    useEffect(()=>{
        axios
            .get("http://127.0.0.1:8000/teste")
            .then((res)=>{
                const data = res.data
                // console.log(data.servidor)
                setBody(data.servidor)
            }).catch((err)=>{
                console.error(err)
        })
    },[])
    return(
        <div className='loginPage'>
            <p>Aqui entra os dados</p>
            <table className="bancouser">
                <thead className="bancouser">
                <tr className="bancouser">
                    <th className="bancouser">TESTE</th>
                    <th className="bancouser">Operação</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td className="bancouser">{body}</td>
                    <td>
                        <input  type="button" value="Deposito"/>
                        <input  type="button" value="Pagamento"/>
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
