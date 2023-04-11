import { useRef, useState, useEffect } from "react";
import { faCheck, faTimes, faInfoCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import axios from '../api/axios';

const USER_REGEX = /^[A-z][A-z0-9-_]{3,23}$/;
const EMAIL_REGEX = /^[A-z][A-z0-9-_]@{3,23}$/;
const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,24}$/;
const REGISTER_URL = '/api/users/';

const RegisterPage = () => {
  const userRef = useRef();
  const errRef = useRef();

  const [email, setEmail] = useState('');
  const [role, setRole] = useState('');
  const [first_name, setFirst_name] = useState('');
  const [last_name, setLast_name] = useState('');

  const [username, setUser] = useState('');
  const [validName, setValidName] = useState(false);
  const [userFocus, setUserFocus] = useState(false);

  const [password, setPassword] = useState('');
  const [validPassword, setValidPassword] = useState(false);
  const [passwordFocus, setPasswordFocus] = useState(false);

  const [matchPassword, setMatchPassword] = useState('');
  const [validMatch, setValidMatch] = useState(false);
  const [matchFocus, setMatchFocus] = useState(false);

  const [errMsg, setErrMsg] = useState('');
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, [])

  useEffect(() => {
    setValidName(USER_REGEX.test(username));
  }, [username])

  useEffect(() => {
    setValidPassword(PWD_REGEX.test(password));
    setValidMatch(password === matchPassword);
  }, [password, matchPassword])

  useEffect(() => {
    setErrMsg('');
  }, [username, password, matchPassword])

  const handleSubmit = async (e) => {
    e.preventDefault();
    // if button enabled with JS hack
    const v1 = USER_REGEX.test(username);
    const v2 = PWD_REGEX.test(password);
    if (!v1 || !v2) {
      setErrMsg("Invalid Entry");
      return;
    }
    await axios.post(REGISTER_URL,
      { email, username, first_name, last_name, password, role }
    )
      .then(response => {
        console.log(response)
        //console.log(JSON.stringify(response))
        setSuccess(true);
        //clear state and controlled inputs
        setUser('');
        setPassword('');
        setMatchPassword('');
      })
      .catch(err => {
        if (!err?.response) {
          setErrMsg('No Server Response');
        } else if (err.response?.status === 409) {
          setErrMsg('Username Taken');
        } else {
          setErrMsg('Registration Failed')
        }
        errRef.current.focus();
      })
  }

  return (
    <>
      {success ? (
        <div className="flex">
          <section>
            <h1>Успешно!</h1>
            <p>
              <a href="/login">Войти</a>
            </p>
          </section>
        </div>
      ) : (
        <div className="flex">
          <section>
            <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
            <h1>Регистрация</h1>
            <form onSubmit={handleSubmit}>

              <label htmlFor="email">
                Email:
              </label>
              <input
                type="email"
                id="email"
                autoComplete="off"
                onChange={(e) => setEmail(e.target.value)}
                value={email}
                required
              />

              <label htmlFor="username">
                Имя пользователя:
                {/* <FontAwesomeIcon icon={faCheck} className={validName ? "valid" : "hide"} />
                <FontAwesomeIcon icon={faTimes} className={validName || !username ? "hide" : "invalid"} /> */}
              </label>
              <input
                type="text"
                id="username"
                ref={userRef}
                autoComplete="off"
                onChange={(e) => setUser(e.target.value)}
                value={username}
                required
              // aria-invalid={validName ? "false" : "true"}
              // aria-describedby="uidnote"
              // onFocus={() => setUserFocus(true)}
              // onBlur={() => setUserFocus(false)}
              />
              {/* <p id="uidnote" className={userFocus && username && !validName ? "instructions" : "offscreen"}>
                <FontAwesomeIcon icon={faInfoCircle} />
                4 до 24 символов.<br />
                Must begin with a letter.<br />
                Letters, numbers, underscores, hyphens allowed.
              </p> */}

              <label htmlFor="first_name">
                Имя:
              </label>
              <input
                type="text"
                id="first_name"
                autoComplete="off"
                onChange={(e) => setFirst_name(e.target.value)}
                value={first_name}
                required
              />

              <label htmlFor="last_name">
                Фамилия:
              </label>
              <input
                type="text"
                id="last_name"
                autoComplete="off"
                onChange={(e) => setLast_name(e.target.value)}
                value={last_name}
                required
              />

              <label htmlFor="role">
                Роль:
              </label>
              <select
                id="role"
                onChange={e => setRole(e.target.value)}
                value={role}
              >
                <option value="employer">Я работодатель</option>
                <option value="applicant">Я ищу работу</option>
              </select>


              <label htmlFor="password">
                Пароль:
                {/* <FontAwesomeIcon icon={faCheck} className={validPassword ? "valid" : "hide"} />
              <FontAwesomeIcon icon={faTimes} className={validPassword || !password ? "hide" : "invalid"} /> */}
              </label>
              <input
                type="password"
                id="password"
                autoComplete="on"
                onChange={(e) => setPassword(e.target.value)}
                value={password}
                required
              // aria-invalid={validPassword ? "false" : "true"}
              // aria-describedby="pwdnote"
              // onFocus={() => setPasswordFocus(true)}
              // onBlur={() => setPasswordFocus(false)}
              />
              {/* <p id="pwdnote" className={passwordFocus && !validPassword ? "instructions" : "offscreen"}>
              <FontAwesomeIcon icon={faInfoCircle} />
              8 to 24 characters.<br />
              Must include uppercase and lowercase letters, a number and a special character.<br />
            </p> */}

              <label htmlFor="confirm_pwd">
                Повторите пароль:
                {/* <FontAwesomeIcon icon={faCheck} className={validMatch && matchPassword ? "valid" : "hide"} />
              <FontAwesomeIcon icon={faTimes} className={validMatch || !matchPassword ? "hide" : "invalid"} /> */}
              </label>
              <input
                type="password"
                id="confirm_pwd"
                autoComplete="on"
                onChange={(e) => setMatchPassword(e.target.value)}
                value={matchPassword}
                required
              // aria-invalid={validMatch ? "false" : "true"}
              // aria-describedby="confirmnote"
              // onFocus={() => setMatchFocus(true)}
              // onBlur={() => setMatchFocus(false)}
              />
              {/* <p id="confirmnote" className={matchFocus && !validMatch ? "instructions" : "offscreen"}>
              <FontAwesomeIcon icon={faInfoCircle} />
              Must match the first password input field.
            </p> */}

              {/* <button>Зарегистрироваться</button> */}
              <button disabled={!validName || !validPassword || !validMatch ? true : false}>Зарегистрироваться</button>
            </form>
            <p>
              Уже зарегистрированы?<br />
              <span className="line">
                {/*put router link here*/}
                <a href="/login">Войти</a>
              </span>
            </p>
          </section>
        </div>
      )}
    </>
  )
}

export { RegisterPage }