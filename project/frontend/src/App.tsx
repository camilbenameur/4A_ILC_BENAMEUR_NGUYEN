import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SignIn from './components/login/SignIn'
import SignUp from './components/login/SignUp'
import { Home } from './pages/Home';
import { Layout } from './components/Layout';
import { User } from './pages/User';

function App() {


  return (
    <>
      <Router>
        <Routes>
          <Route element={<Layout />} >
            <Route path="/user/:userId" element={<User />} />
            <Route path="/" element={<Home />} />
          </Route>
          <Route path="/signin" element={<SignIn />} />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
      </Router >
    </>
  )
}

export default App
