import { Outlet } from 'react-router-dom'

import Header from './Header'

import "./../assets/css/Layout.css"

const Layout = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  )
}

export default Layout