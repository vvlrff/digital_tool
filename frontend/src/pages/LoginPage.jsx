import { useRef, useState, useEffect, useContext } from 'react';
import { AuthContext } from "../context/AuthProvider";

import axios from 'axios';

const LoginPage = () => {
  const { setAuth } = useContext(AuthContext);
  const userRef = useRef();
  const errRef = useRef();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errMsg, setErrMsg] = useState('');
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, [])

  useEffect(() => {
    setErrMsg('');
  }, [email, password])


  // const handleSubmit = async (e) => {
  //   e.preventDefault();
  //   // if button enabled with JS hack
  //   const v1 = USER_REGEX.test(username);
  //   const v2 = PWD_REGEX.test(password);
  //   if (!v1 || !v2) {
  //     setErrMsg("Invalid Entry");
  //     return;
  //   }
  //   await axios.post("http://127.0.0.1:8000/api/users/",
  //     { email, username, first_name, last_name, password }
  //   )
  //     .then(response => {
  //       console.log(response)
  //       //console.log(JSON.stringify(response))
  //       setSuccess(true);
  //       //clear state and controlled inputs
  //       setUser('');
  //       setPassword('');
  //       setMatchPassword('');
  //     })
  //     .catch(err => {
  //       if (!err?.response) {
  //         setErrMsg('No Server Response');
  //       } else if (err.response?.status === 409) {
  //         setErrMsg('Username Taken');
  //       } else {
  //         setErrMsg('Registration Failed')
  //       }
  //       errRef.current.focus();
  //     })
  // }




  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/auth/token/login/",
        { email, password }
      );
      console.log(JSON.stringify(response?.data));
      //console.log(JSON.stringify(response));
      const accessToken = response?.data?.auth_token;
      setAuth({ email, password, accessToken });
      setEmail('');
      setPassword('');
      setSuccess(true);
    } catch (err) {
      if (!err?.response) {
        setErrMsg('No Server Response');
      } else if (err.response?.status === 400) {
        setErrMsg('Missing Username or Password');
      } else if (err.response?.status === 401) {
        setErrMsg('Unauthorized');
      } else {
        setErrMsg('Login Failed');
      }
      errRef.current.focus();
    }
  }

  return (
    <>
      {success ? (
        <section>
          <h1>You are logged in!</h1>
          <br />
          <p>
            <a href="/">Go to Home</a>
          </p>
        </section>
      ) : (
        <section>
          <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
          <h1>Sign In</h1>
          <form onSubmit={handleSubmit}>
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              ref={userRef}
              autoComplete="off"
              onChange={(e) => setEmail(e.target.value)}
              value={email}
              required
            />

            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              onChange={(e) => setPassword(e.target.value)}
              value={password}
              required
            />
            <button>Sign In</button>
          </form>
          <p>
            Need an Account?<br />
            <span className="line">
              {/*put router link here*/}
              <a href="/register">Sign Up</a>
            </span>
          </p>
        </section>
      )}
    </>
  )
}

export { LoginPage }