import React from 'react';

export default function AgregarUsuario() {

    function agregarusuario(){
        
    }

    return (
        <div className='container'>
            <div className='row'>
                <div className=''>
                    <h2 className='mt-4'>Crear un nuevo usuario</h2>
                </div>
            </div>
            <div className='row'>
                <div className='col-sm-6 offset-3'>
                    <div className='mb-3'>
                        <label htmlFor='nombre' className='form-label'>Nombre</label>
                        <input type='text' className='form-control'></input>
                    </div>
                    <div className='mb-3'>
                        <label htmlFor='email' className='form-label'>Email</label>
                        <input type='email' className='form-control'></input>
                    </div>
                    <div className='mb-3'>
                        <label htmlFor='telefono' className='form-label'>Teléfono</label>
                        <input type='text' className='form-control'></input>
                    </div>
                    <button onClick={agregarusuario} className='btn btn-success'>Guardar usuario</button>
                </div>
            </div>
        </div>
    );
}

