import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import SignIn from './components/login/SignIn'
import SignUp from './components/login/SignUp'
import Home from './components/tweetPage/home';

function App() {
  

  return (
    <>
      <Router>
        <Routes>
          <Route path="/signin" element={<SignIn/>} />
          <Route path="/signup" element={<SignUp/>} />
          <Route path="/home" element={<Home/>} />
        </Routes>
      </Router>
    </>
  )
}

export default App
