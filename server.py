import time
import zmq
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("Socket Awaiting Messages *:5555")
while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(1)

    os.system("./script.sh")

    #  Send reply back to client
    socket.send(b"Script executed")
