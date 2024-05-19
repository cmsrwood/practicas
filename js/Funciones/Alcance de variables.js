let variableglobal=5

variableglobal= 10

function miFuncion(variablelocal){
    console.log(variablelocal)

    variableglobal=20

    var variableglobal=30
}

miFuncion(variableglobal)