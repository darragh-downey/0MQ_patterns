
import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:9999")

while True:
    # wait for message
    message = socket.recv_json()
    print(f"Received: {message}")

    time.sleep(1)

    socket.send_string("World")