import React from 'react'
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom'
import Register from './Authentication/Register'
import Login from './Authentication/Login'
import Home from './Components/Home'
import JobBoard from './Components/JobBoard'

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Register />} />
        <Route path='/login/' element={<Login />}/>
        <Route path='/home/' element={<Home />}/>
        <Route path='/jobboard/' element={<JobBoard />}/>
      </Routes>
    </Router>
  )
}

export default App