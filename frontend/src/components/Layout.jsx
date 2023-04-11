import { Outlet } from 'react-router-dom'

import Header from './Header'

import "./../assets/css/Layout/Layout.css"

const Layout = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  )
}

export default Layout