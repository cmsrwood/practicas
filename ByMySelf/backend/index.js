import express from 'express'
import cors from 'cors'
import mysql from 'mysql'

const app = express()
app.use(express.json())
app.use(cors())

// base de datos
const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "bymyself"
})


app.listen (8800, () => {
    console.log("Server running on port 8800")}
)

app.get("/",(req,res)=>{
    res.json("Hello World from backend :D") 
})
