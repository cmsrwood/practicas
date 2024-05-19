import axios from "axios";
import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import Swal from 'sweetalert2'

const Update = () => {
  const [book, setBook] = useState({
    title: "",
    desc: "",
    price: null,
    cover: "",
  });
  const [error,setError] = useState(false)

  const location = useLocation();
  const navigate = useNavigate();

  const bookId = location.pathname.split("/")[2];

  const handleChange = (e) => {
    setBook((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleClick = async (e) => {
    e.preventDefault();

    try {
      await axios.put(`http://localhost:8800/books/${bookId}`, book);
      navigate("/");
      Swal.fire('Felicidades', 'El link se actualizo con éxito')
    } catch (err) {
      console.log(err);
      setError(true);
    }
  };

  return (
    <div className='form'>
      <h1>Update a Book</h1>
      <form>
        <input type="text" placeholder='title' onChange={handleChange} name='title'/>
        <input type="text" placeholder='desc' onChange={handleChange} name='desc'/>
        <input type="number" placeholder='price' onChange={handleChange} name='price'/>
        <input type="text" placeholder='cover' onChange={handleChange} name='cover'/>
        <button onClick={handleClick}>Update</button>
      </form>
      {error && "Something went wrong!"}
      <Link to="/">See all books</Link>
    </div>
  );
};

export default Update;