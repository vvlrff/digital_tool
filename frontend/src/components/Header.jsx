import { Link } from "react-router-dom"
import { useContext } from "react"

const Header = () => {
//  let { user, logoutUser } = useContext(AuthContext)

  return (
    <header>
      <Link to='/'>Home </Link>
      <Link to='/login'>Login </Link>
      <Link to='/register'>Register </Link>
      <Link to='/posts'>Posts </Link>
      <Link to='/about'>About </Link>
      {/* 
        {
          user?(
            <p onClick = { logoutUser } > Logout</p>
          ) : (
            <Link to="/login" >Login</Link>
          )
        }
    */}
    </header >
  )
}

export default Header