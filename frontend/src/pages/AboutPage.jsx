import { Outlet, Link } from "react-router-dom"

const AboutPage = () => {
  return (
    <>
      <h1>About Page</h1>
      <p>My company is very big and rich</p>
      <ul>
        <li><Link to='contacts' >Our contacts</Link></li>
        <li><Link to='team' >Our team</Link></li>
      </ul>

      <Outlet />

      {/* <Routes>
        <Route path='contacts' element={<p>Our team</p>} />
        <Route path='team' element={<p>Our contacts</p>} />
      </Routes> */}
    </>
  )
}

export { AboutPage }