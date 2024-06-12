const express = require('express')
const mysql = require('mysql')
const session = require('express-session')
const MySQLStore = require('express-mysql-session')(session)
const multer = require('multer')
const uniqid = require('uniquid')
const path = require('path')
const cors = require('cors')
const bcrypt = require('bcrypt');



// app
const app = express()

// config
const { BACKEND_PORT, DB_HOST, DB_USER, DB_PASS, DB_DATABASE, FRONTEND_URL } = require("./config.js");

// database
const options = {
    host: DB_HOST,
    user: DB_USER,
    password: DB_PASS,
    database: DB_DATABASE
}

// conexion 

const conn = mysql.createConnection(options)

// session
const sessionStore = new MySQLStore(options)
app.use(session({
    key: 'session_cookie_name',
    secret: 'secret',
    resave: false,
    saveUninitialized: false,
    store: sessionStore
}))


// middlewares
app.use(cors())
app.use(express.json())
app.use(express.urlencoded({ extended: true }))


// multer
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads')
    },
    filename: (req, file, cb) => {
        cb(null, file.fieldname + '-' + Date.now())
    }
})


const password = 'mi_contraseña';

// Generar una contraseña encriptada



// routes
app.get('/', (req, res) => {
    req.session.username = 'dilan'
    req.session.password = '1234'
    req.session.email = 'Zk6uT@example.com'
    req.session.visitas = req.session.visitas ? req.session.visitas + 1 : 1
    res.json(`El usuario ${req.session.username} ha visitado esta página ${req.session.visitas} veces`)
})

app.post("/signup", (req, res) => {

    conn.query("SELECT * FROM users WHERE email = ?", [req.body.email], (err, result) => {

        const id = uniqid()


        if (err) {
            res.send(err)
        }
        if (result.length > 0) {
            res.send("User already exists")
        } else {
            const password = req.body.password
            const hashpassword = bcrypt.hashSync(password, 10)
            const q = "INSERT INTO users (id_user, username, email, pass) VALUES (?,?,?,?)"
            const values = [
                id,
                req.body.username,
                req.body.email,
                hashpassword
            ]
            conn.query(q, values, (err) => {
                if (err) {
                    res.send(err)
                }
                res.send("User created successfully")
            })
        }
    })
})

app.post("/login", (req, res) => {

    const username = req.body.username
    const password = req.body.password

    conn.query("SELECT * FROM users WHERE username = ?", [username], (err, result) => {

        if (err) {
            res.send(err)
        }

        if (result.length > 0) {
            const hashedPassword = result[0].pass
            const passwordMatch = bcrypt.compareSync(password, hashedPassword)
            if (passwordMatch) {
                res.send("Success")
            } else {
                res.send("Wrong password or username") 
            }
        }
    })
})

const upload = multer({ storage: storage })

app.listen(BACKEND_PORT, () => {
    console.log(`App is running on http://localhost:${BACKEND_PORT}`)
})
