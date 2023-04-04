import { Link, Outlet } from 'react-router-dom'

import "./../assets/css/Layout.css"

const Layout = () => {
  return (
    <>
      <header>
        <Link to='/'>Home </Link>
        <Link to='/login'>Login </Link>
        <Link to='/posts'>Posts </Link>
        <Link to='/about'>About </Link>
      </header>
      <Outlet />
    </>
  )
}

export default Layout