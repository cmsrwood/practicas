import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

export default function Books() {

  const [books,setBooks] = useState([])

  useEffect(() => {
    const fetchAllBooks = async () => {
      try{
        const res= await axios.get('http://localhost:8800/books')
        setBooks(res.data)
      }catch(err){
        
      }
    }
    fetchAllBooks()
  }, [])

  return (
    <div>
      <h1>Books</h1>
        <div className='books'>
          {books.map(book => (
            <div className='book' key={book.id}>
              {book.cover && <img src={book.cover} alt={book.title} />}
              <h2>{book.title}</h2>
              <p>{book.desc}</p>
              <span>{book.price}</span>
            </div>
          ))}
        </div>
        <button>
          <Link to="/add">Add new book</Link>
        </button>
    </div>
  )
}
