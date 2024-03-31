import { BrowserRouter, Route, Routes } from "react-router-dom";
import ListadoEmpleados from "./empleados/ListadoEmpleados";
import Navegacion from "./plantilla/Navegacion";
import AgregarEmpleado from "./empleados/AgregarEmpleado";

function App() {
  return (
    <div className="container-fluid">
      <BrowserRouter>
      <Navegacion></Navegacion>
      <Routes>
        <Route exact path="/" element={<ListadoEmpleados></ListadoEmpleados>}></Route>
        <Route exact path="/agregar" element={<AgregarEmpleado></AgregarEmpleado>}></Route>
      </Routes>
      </BrowserRouter>
    </div>
  );
}
export default App;
