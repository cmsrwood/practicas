const express = require ("express")
const app = express()
const http = require('http')
const cors = require('cors')

app.use(cors())
const server = http.createServer(app)

const {Server} = require('socket.io')

const io = new Server(server, {
    cors: {
        origin: "http://localhost:5173",
        methods: ["GET", "POST"]
    }
})

io.on('connection', (socket) => {
    console.log(socket.id)
    socket.on('disconnect', () => {
        console.log ("Usuario desconectado: ",socket.id)
    })
})

server.listen (3001, () => {
    console.log("Server listening on port 3001")
})