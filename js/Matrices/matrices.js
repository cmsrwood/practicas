let numeroArreglo=[1,2,3,4,5,6]
let numeroArreglo2=[7,8,9,10,11,12]
let numerosArreglo=[numeroArreglo,numeroArreglo2]

for (let ren=0; ren< numerosArreglo.length; ren++){
    for(let col=0; col<numerosArreglo[ren].length; col++){
        console.log(numerosArreglo[ren][col])
    }
}