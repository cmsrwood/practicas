import React from 'react'
import { Link} from 'react-router-dom'

export default function Navigate() {


  function changeTheme(){
    var index = document.getElementById('html');
    var icon = document.getElementById('botont');
        if (index.getAttribute("data-bs-theme") === "light") {
          index.setAttribute("data-bs-theme", "dark");
          icon.setAttribute("class","bi bi-moon-fill")
        }
        else {
          index.setAttribute("data-bs-theme", "light");
          icon.setAttribute("class","bi bi-sun-fill")
        }
      }

  return (
    <div>
      <nav class="navbar navbar-expand-lg bg-body-tertiary shadow">
        <div class="container-fluid">
          <Link className='navbar-brand' to='/'>ByMySelf</Link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-between" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <Link className='nav-link' to='/'>Home</Link>
              </li>
              <li class="nav-item">
                <Link className='nav-link' to='/signin'>Sign in</Link>
              </li>
              <li class="nav-item">
                <Link className='nav-link' to='/register'>Register</Link>
              </li>
            </ul>
          <button className='btn justify-content-end' onClick={changeTheme}><i id="botont" className='bi bi-moon-fill'></i></button>
          </div>
        </div>
      </nav>
    </div>
  )
}
