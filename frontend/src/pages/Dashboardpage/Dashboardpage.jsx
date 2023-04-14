import { useNavigate, useLoaderData } from 'react-router-dom'
import axios from 'axios'

import { useAuth } from '../../hook/useAuth'

const SinglePage = () => {
  const post = useLoaderData()
  const navigate = useNavigate()

  const { signOut } = useAuth()

  const clickSignOut = () => {
    signOut(() => navigate('/', { replace: true }))
  }

  return (
    <>
      <div>
        {post && (
          <div>
            <h1>{post.title}</h1>
            <p>{post.body}</p>
          </div>
        )}
      </div>
      <button onClick={clickSignOut}>Log Out</button>
    </>
  )
}

export const postLoader = async ({ params }) => {
  const id = params.id
  const res = await axios.get(`https://jsonplaceholder.typicode.com/posts/${id}`)

  return res.data
}

export default SinglePage