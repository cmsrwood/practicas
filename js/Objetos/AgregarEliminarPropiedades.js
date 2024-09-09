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

persona.telefono = '123456789'
persona.telefono = '987654321'

delete persona.telefono

console.log(persona);

//Concatenar cada valor de cada propiedad

console.log(persona.nombre + ' ' + persona.apellido)

//for in

for (nombrePropiedad in persona) {
    console.log(persona[nombrePropiedad])
}

let personaArray = Object.values(persona)