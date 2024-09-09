function Persona(nombre, apellido, email, edad, idioma) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.edad = edad;
    this.idioma = idioma;
    this.lang = function () {
        return this.idioma.toUpperCase();
    }
    this.nombreCompleto = function () {
        return this.nombre + ' ' + this.apellido;
    }
}

let padre = new Persona('Dilan', 'Lopez', 'Dilan@lopez', 20, 'es');
let madre = new Persona('Diana', 'Romero', 'Diana@romeroz', 20, 'es');

console.log(padre)

padre.nombre = 'Carlos';

console.log(padre)
console.log(madre)