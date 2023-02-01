import React, {useEffect, useState} from "react";
import "./banco.css"
import axios from "axios";
type Correntista = {
    cod_correntista: number;
    nome_correntista: string;
    email_correntista: string;
    saldo_correntista: number;

}
const Usuario =()=>{
    const [usuario, setUsuario] = useState('')
    useEffect(()=>{
        axios
            .get(" http://localhost:8000/usuarios/clube")
            .then((res)=>{
                const user = res.data
                console.log(user)
                setUsuario(user)
            }).catch((err)=>{
                console.log(err)
        })
    },[])

    return(
        <div>
            <h3 className="signIn">Todos os Usuários</h3>
                <table className="tabelausuario">
                    <thead>
                        <tr>
                            <th className="tabelausuario">Nome</th>
                            <th className="tabelausuario">Email</th>
                            <th className="tabelausuario">Saldo</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td></td>
                        </tr>
                    </tbody>
                </table>
        </div>
    );
}
export default Usuario;
// Aqui vou exibir os dados do usuario
//Aqui retorna uma tabela com os dados do usuario
