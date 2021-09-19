

import zmq

context = zmq.Context()

xsub = context.socket(zmq.SUB)
xsub.bind("tcp://*:9997")

xsub.setsockopt(zmq.SUBSCRIBE, b"")

xpub = context.socket(zmq.PUB)
xpub.bind("tcp://*:9998")

while True:

    msg = xsub.recv_multipart()
    
    print(f"Received: {msg}")

    xpub.send_multipart(msg)