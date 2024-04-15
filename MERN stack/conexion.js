const mongoose = require ('mongoose')
mongoose.connect('mongodb://localhost:27017/crudmernstack')

const objetobd = mongoose.connection

objetobd.on('connected',()=>{console.log("Conexion exitosa a MongoDB")})
objetobd.on('error',()=>{console.log("Error al conectar a MongoDB")})

module.exports = mongoose;