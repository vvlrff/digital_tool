import { useContext } from "react"
import { AuthContext } from "../hoc/AuthProvider"

const LoginPage = () => {

  const handleSubmit = useContext(AuthContext)

  return (
    <div>
      <h1>Login Page</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Name: <input name='username' />
        </label>
        <button type='submit'>Login</button>
      </form>
      {fromPage}
    </div>
  )
}

export default LoginPage