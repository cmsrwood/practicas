const express = require ('express')
const app = express()
const archivoDB = require('./conexion')

app.get('/',(req,res)=>{
    res.end('ola')
})

//Configuracion de server
app.listen(5000,function(){
    console.log("El servidor esta corriendose correctamente")
})