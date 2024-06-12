// eslint-disable-next-line no-unused-vars
import React from 'react'
import { BrowserRouter , Routes, Route } from 'react-router-dom'
import HomeDefault from './pages/HomeDefault'
import SignUp from './pages/SignUp'
import Login from './pages/Login'


function App() {

  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<HomeDefault/>}></Route>
      <Route path="/login" element={<Login/>}></Route>
      <Route path="/signup" element={<SignUp/>}></Route>
    </Routes>
    </BrowserRouter>
  )
}

export default App
