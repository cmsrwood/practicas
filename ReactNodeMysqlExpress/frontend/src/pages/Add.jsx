import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import React, { useState } from 'react'
import Swal from 'sweetalert2'


export default function Add() {

const [book,setBook] = useState({
  title:"",
  desc:"",
  cover:"",
  price:""
})

const navigate = useNavigate()

const handleChange = (e) =>{
  setBook(prev=>({...prev,[e.target.name]:e.target.value}))
}

const handleClick = async (e) =>{
  e.preventDefault()
  try{
    await axios.post("http://localhost:8800/books",book)
    navigate("/")
    Swal.fire("Saved!", "", "success");

  }catch(err){
    console.log(err)
  }
}
  return (
    <div className='form'>
      <h1>Add New Book</h1>
      <form>
        <input type="text" placeholder='title' onChange={handleChange} name='title'/>
        <input type="text" placeholder='desc' onChange={handleChange} name='desc'/>
        <input type="number" placeholder='price' onChange={handleChange} name='price'/>
        <input type="text" placeholder='cover' onChange={handleChange} name='cover'/>
        <button onClick={handleClick}>Add</button>
      </form>
    </div>
  )
}
