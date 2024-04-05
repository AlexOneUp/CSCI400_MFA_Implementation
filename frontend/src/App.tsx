import React from 'react';
import './App.css';
import LoginForm from './routes/LoginForm'; // Make sure the import path matches your file structure
import SignupForm from './routes/SignupForm';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <LoginForm />
        <SignupForm />
      </header>
    </div>
  );
}

export default App;
