const { Client } = require('whatsapp-web.js');

const client = new Client();

client.on('qr', (qr) => {
    // Generate and scan this code with your phone
    console.log('QR RECEIVED', qr);
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('message', msg => {
    if (msg.body == '!ping') {
        msg.reply('pong');
    }
});

client.initialize();


const nodemailer = require('nodemailer');

enviarMail = async () => {
    const config = {
        host: 'smtp.gmail.com',
        port: 465,
        secure: true, 
        auth: {
            user: 'dilanfantas@gmail.com',
            pass: 'jegc hedq jngv tyyg'
        }
    }
    const transporter = nodemailer.createTransport(config);

    const mensaje = {
        from: 'dilanfantas@gmail.com',
        to: 'andres.romerp1473@gmail.com',
        subject: 'Prueba de email nodemailer',
        text: 'Prueba de email compae'
    }
    
    const info = await transporter.sendMail(mensaje)

    console.log(info)
}



