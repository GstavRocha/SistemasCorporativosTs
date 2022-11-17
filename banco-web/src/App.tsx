import React from 'react';
import './css/App.css';
import LoginPage from "./loginPage/login-page";


function App() {
  return (
    <div className='loginPage'>
      <p className='esfera1'></p>
      <h1> Welcome to Test Bank</h1>
      <p className='aquiestamos'>Aqui estamos criando e inovando</p>P
      <p className='esfera2'></p>
      <p className='esfera3'></p>
      <div className='retangulo'>
        <LoginPage/>
      </div>
  </div>
  );
}

export default App;
