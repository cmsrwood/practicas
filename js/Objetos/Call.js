let persona1 = {
    nombre : 'Dilan',
    apellido : 'Lopez',
    email : 'Dilan@lopez',
    edad : 20,
    nombreCompleto: function (titulo, tel) {
        return titulo + ': ' + this.nombre + ' ' + this.apellido + ' ' +  ', ' + tel
    }
}

let persona2 = {
    nombre : 'Diana',
    apellido : 'Romero',
}

console.log(persona1.nombreCompleto('Ingeniero', '1234567890'))

//Uso de call para usar el metodo de persona1 con el objeto persona2

console.log(persona1.nombreCompleto.call(persona2, 'Licenciada', '1234567890'))