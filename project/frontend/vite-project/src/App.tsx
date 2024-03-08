import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import SignIn from './SignIn'
import SignUp from './SignUp'

function App() {
  

  return (
    <>
      <Router>
        <Routes>
          <Route path="/signin" element={<SignIn/>} />
          <Route path="/signup" element={<SignUp/>} />
        </Routes>
      </Router>
    </>
  )
}

export default App
