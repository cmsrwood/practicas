import React, { useState } from 'react'
import Navigate from '../plantillas/Navigate'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import Swal from 'sweetalert2'

export default function Register() {

    //hooks
    const [user,setUser] = useState({
        email:"",
        password:""
    })

    const navigate = useNavigate()

    const handleChange = (e) =>{
        setUser(prev=>({...prev,[e.target.name]:e.target.value}))
      }
      
      const handleClick = async (e) =>{
        e.preventDefault()
        try{
            if (await axios.post("http://localhost:8800/register",user))
              navigate("/")
              Swal.fire("User created successfully!", "Now try to sign in!", "success");
        }catch(err){
          console.log(err)
        }
      }

  return (
    <div className=''>
        <Navigate/>
        <div className='p-5'>
            <h1 className='text-center'>Register</h1>
            <form className='justify-content-center align-items-center px-5'>
                <div className='mb-3 form-group'>
                    <label className='form-label'>Email</label>
                    <input className='form-control' onChange={handleChange} type="email" name='email' required/>
                </div>
                <div className='mb-3 form-group'>
                    <label className='form-label'>Password</label>
                    <input className='form-control' onChange={handleChange} type="password" name='password' required/>
                </div>
                <div className='mb-3 form-group'>
                    <label className='form-label'>Confirm password</label>
                    <input className='form-control' onChange={handleChange} type="password" name='password' />
                </div>
                <div className='mb-3 form-group text-center'>
                    <button className='btn btn-primary' onClick={handleClick}>Register</button>
                </div>
            </form>
        </div>
    </div>
  )
}


