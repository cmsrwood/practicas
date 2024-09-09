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

// Asignar un valor al constructor
Persona.prototype.email = 'Dilan@lopez';