import { Link } from "react-router-dom"
//import { useContext } from "react"

const Header = () => {
  //  let { user, logoutUser } = useContext(AuthContext)

  return (
    <header>
      <Link to='/' className="home-link black">
        <div className="flex">
          <img src="src/assets/images/sberbank-svgrepo-com.svg" alt="logo" className="header-logo"></img>
          <span>Подбор персонала</span>
        </div>
      </Link>

      <div className="flex-end">
        <Link to='/register' className="white">
          <div className="header-btn">
            Регистрация
          </div>
        </Link>

        <Link to='/login' className="white">
          <div className="header-btn">
            Войти
          </div>
        </Link>
      </div>
      {/* <Link to='/posts'>Posts </Link>
      <Link to='/about'>About </Link> */}
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