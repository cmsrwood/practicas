// Crear un objeto

let persona = {
    nombre: 'Dilan',
    apellido: 'Lopez',
    email: 'Dilan@lopez',
    edad: 20,
    nombrecompleto: function () {
        return this.nombre + ' ' + this.apellido
    }
}

for (nombrePropiedad in persona) {
    console.log(persona[nombrePropiedad])
}

console.log(persona.email)
console.log(persona['nombre'])
console.log(persona.nombrecompleto())

// Crear un objeto a partir de una clase

let persona2 = new Object();
persona2.nombre = 'Dilan Santiago';
persona2.apellido = 'Lopez Romero';
persona2.email = 'Dilan2@lopez';
persona2.edad = 20;
persona2.nombrecompleto = function () {
    return this.nombre + ' ' + this.apellido
}
console.log(persona2.email)
console.log(persona2.nombrecompleto())