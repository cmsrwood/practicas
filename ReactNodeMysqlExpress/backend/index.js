import express from 'express'
import mysql from 'mysql'
import cors from 'cors'

const app = express()

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "test"
})

app.use(express.json())
app.use(cors())

app.get("/",(req,res)=>{
    res.json("Hello World from backend") 
})

app.get("/books",(req,res)=>{
    db.query("SELECT * FROM books",(err,data)=>{
        if(err){
            return res.json(err)
        }else{
            res.send(data)
        }
    })
})

app.post ("/books",(req,res)=>{
    const q = "INSERT INTO books (`title`,`desc`,`cover`) VALUES (?)"
    const values = [
        req.body.title,
        req.body.desc,
        req.body.cover
    ]
    db.query(q,[values],(err,data)=>{
        if(err){
            return res.json(err)
        }
        return res.json("El libro se ha creado correctamente")
    })
})

app.listen(73, ()=>{
    console.log("El servidor backend se corre!")
})   