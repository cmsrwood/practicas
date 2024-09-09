// Crear un objeto

let persona = {
    nombre: 'Dilan',
    apellido: 'Lopez',
    email: 'Dilan@lopez',
    edad: 20,
    idioma : 'es',
    get lang () {
        return this.idioma.toUpperCase();
    },
    set lang (idioma) {
        this.idioma = idioma.toUpperCase();
    },
    get nombrecompleto () {
        return this.nombre + ' ' + this.apellido;
    }
    
}

console.log(persona.nombrecompleto)
console.log(persona.lang)

persona.lang = 'en'

console.log(persona.lang)