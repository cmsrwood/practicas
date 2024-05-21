import React from 'react'
import Navigate from '../plantillas/Navigate'

export default function SignIn() {
  return (
    <div className=''>
        <Navigate/>
        <div className='p-5'>
            <h1 className='text-center'>Sign in</h1>
            <form className='justify-content-center align-items-center px-5'>
                <div className='mb-3 form-group'>
                    <label className='form-label'>Email</label>
                    <input className='form-control' type="text" name='email' />
                </div>
                <div className='mb-3 form-group'>
                    <label className='form-label'>Password</label>
                    <input className='form-control' type="text" name='password' />
                </div>
                <div className='mb-3 form-group text-center'>
                    <button className='btn btn-primary'> Sign in</button>
                </div>
            </form>
        </div>
    </div>
  )
}
