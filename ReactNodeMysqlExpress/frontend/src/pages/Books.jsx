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

  const handleDelete = async (id) => {
    try{
      await axios.delete(`http://localhost:8800/books/${id}`)
      window.location.reload()
    }catch(err){
      console.log(err)
    }
  }

  return (
    <div className='container text-center '>
      <h1 >Books</h1>
      <Link to='/add'><button className='btn btn-success'><i className='bi'></i>Add New Book</button></Link>
      <div className="row row-cols-1 row-cols-md-4 g-4">
          {books.map(book => (
            <div class="card col mb-3" key={book.id} >
            {book.cover && <img className='card-img-top' src={book.cover} alt={book.title} />}
              <div class="card-body">
                <h5 class="card-title">{book.title}</h5>
                <p class="card-text">{book.desc}</p>
                <span>{book.price}</span>
                <div className="row">
                  <Link className='btn btn-warning col' target='blank' to={`/update/${book.id}`}>Update</Link>
                  <Link className='btn btn-danger col' onClick={()=>handleDelete(book.id)}>Delete</Link>
                </div>
              </div>
              </div>
          ))}
      </div>
      
      


      
    </div>
  )
}
