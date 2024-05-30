// eslint-disable-next-line no-unused-vars
import React, { useEffect, useState } from 'react'

// eslint-disable-next-line react/prop-types
const Chat = ({ socket, username, room }) => {

    const [currentMessage, setCurrentMessage] = useState("")
    const [messagesList, setMessagesList] = useState([])

    const sendMessage = async () => {
        if (username && currentMessage) {
            const info = {
                message: currentMessage,
                room,
                author: username,
                time: new Date().getHours() + ":" + new Date().getMinutes()
            };
            // eslint-disable-next-line react/prop-types
            await socket.emit("send_message", info);
        }
    }
    
    useEffect (() => {
      const messageHandle = (message) => {
        setMessagesList((list) => [...list, message])
      }
        // eslint-disable-next-line react/prop-types
        socket.on("receive_message", messageHandle)
    }, [ socket ])

  return (
    <div className='my-5'>
        <div className="card shadow">
        <div className="card-header">
            <h3>Live chat | Room: {room}</h3>
        </div>
        <ul className="list-group list-group-flush">
          <li className="list-group-item">
            {messagesList.map((item) => {
                return (
                  <h3>{item.message}</h3>
                )
            })}
          </li>
          <li className="list-group-item">
            <div className="input-group my-2">
                <input className='form-control ' type="text" placeholder='Escribe un mensaje' onChange={(e) => setCurrentMessage(e.target.value)} />
                <button className='btn btn-primary ' onClick={sendMessage}>Enviar <i className="bi bi-send"></i></button>
            </div>
          </li>
        </ul>
      </div>
    </div>
    
  )
}

export default Chat
