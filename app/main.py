  
from flask import Flask
app = Flask(__name__)

import socket
server = socket.socket() 
server.bind(("172.18.85.134", 5000)) 
server.listen(4) 

@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(host='172.18.85.134')
