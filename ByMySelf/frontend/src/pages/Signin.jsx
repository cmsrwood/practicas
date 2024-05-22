import React, { useState } from 'react';
import Navigate from '../plantillas/Navigate';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Swal from 'sweetalert2';
import Validation from './LoginValidation';

export default function Signin() {

    //hooks
    const [user,setUser] = useState({
        email:"",
        password:""
    })
    const [errors,setErrors] = useState({})
    const navigate = useNavigate()

    const handleChange = (e) =>{
        setUser(prev=>({...prev,[e.target.name]:e.target.value}))
      }
      
      const handleClick = async (e) =>{
        e.preventDefault()
        setErrors(Validation(user));
        try{
            if (await axios.post("http://localhost:8800/signin",user))
                Swal.fire("User logged successfully!", "Welcome!", "success");
                navigate("/homeuser")
        }catch(err){
          console.log(err)
        }
      }

  return (
    <div className=''>
        <Navigate/>
        <div className='p-5'>
            <h1 className='text-center'>Signin</h1>
            <form className='justify-content-center align-items-center px-5'>
                <div className='mb-3 form-group'>
                    <label className='form-label'>Email</label>
                    <input className='form-control' onChange={handleChange} type="email" name='email' required/>
                    {errors.email && <span className='text-danger'> {errors.email}</span>}
                </div>
                <div className='mb-3 form-group'>
                    <label className='form-label'>Password</label>
                    <input className='form-control' onChange={handleChange} type="password" name='password' required/>
                    {errors.password && <span className='text-danger'> {errors.password}</span>}
                </div>
                <div className='mb-3 form-group text-center'>
                    <button className='btn btn-primary' onClick={handleClick}>Sign in</button>
                </div>
            </form>
        </div>
    </div>
  )
}


