import { Link, useSearchParams, useLoaderData } from "react-router-dom"
import axios from 'axios'

import { BlogFilter } from "../../components/BlogFilter"

import '../ApplyingPage.css'

const PostsPage = () => {
  const posts = useLoaderData()
  const [searchParams, setSearchParams] = useSearchParams()

  const postQuery = searchParams.get('post') || ''
  const latest = searchParams.has('latest')

  const startsFrom = latest ? 80 : 1

  return (
    <div>
      <h1>Posts</h1>
      <BlogFilter postQuery={postQuery} latest={latest} setSearchParams={setSearchParams} />
      {posts.filter(
        post => post.title.includes(postQuery) && post.id >= startsFrom
      ).map(post => (

        <div className="container">
          <Link key={post.id} to={`/posts/${post.id}`}>
            <div>{post.id} Title: {post.title}</div>
            <div>Body: {post.body}</div>
          </Link>
        </div>
      ))}
    </div>
  )
}

export const postsLoader = async () => {
  const res = await axios.get('https://jsonplaceholder.typicode.com/posts')

  return res.data
}

export { postsLoader }

export default PostsPage