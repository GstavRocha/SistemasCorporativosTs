import React from 'react';
import './css/App.css';
import './css/login.css';
import LoginEvents from "./loginPage/login-events";


function App() {
  return (
    <div className='loginPage'>
      <p className='esfera1 esferaAnimation1'></p>
      <h1> Welcome to Test Bank</h1>
      <p className='aquiestamos'>Aqui estamos criando e inovando</p>P
      <p className='esfera2 esferaAnimation1'></p>
      <p className='esfera3 esferaAnimation1'></p>
      <div className='retangulo'>
        <LoginEvents/>
      </div>
  </div>
  );
}

export default App;
