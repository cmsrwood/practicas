// No es posible crear objetos antes de declarar la clase
// let persona2 = new Persona('Diana', 'Romero', 'Diana@romeroz', 17, 'es');

class Persona {
    constructor(nombre, apellido, email, edad, idioma) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre() {
        return this._nombre;
    }

    get apellido() {
        return this._apellido;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre , apellido);
        this._departamento = departamento;
    }

    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
    nombreCompleto() {
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}


let persona = new Persona('Dilan', 'Lopez');
console.log(persona)

let empleado1 = new Empleado('Diana', 'Romero', 'Educacion infantil');
console.log(empleado1)
console.log(empleado1.nombreCompleto())