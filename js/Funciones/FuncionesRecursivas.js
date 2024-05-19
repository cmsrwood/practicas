function mi_funcion(valor){
    if (valor==1){
        console.log(valor)
}
    else {
        console.log(valor)
        mi_funcion(valor-1)
    }
}
mi_funcion(10)