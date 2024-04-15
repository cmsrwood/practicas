import { Route,BrowserRouter,Routes } from 'react-router-dom';
import ListaUsuario from './usuarios/ListarUsuario';
import AgregarUsuario from './usuarios/AgregarUsuario';
import UsuarioIndividual from './usuarios/UsuarioIndividual';
import EditarUsuario from './usuarios/EditarUsuario';


function App() {
  return (
    <div className="container-fluid text-center">
      <h1>Crud MERN</h1>
      <BrowserRouter>
        <Routes>
          <Route exact path='/' element={<ListaUsuario/>}></Route>
          <Route exact path='/agregarusuario' element={<AgregarUsuario/>}></Route>
          <Route exact path='/editarusuario' element={<EditarUsuario/>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
