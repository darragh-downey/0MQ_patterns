
import zmq
import sys
import time


context = zmq.Context()

# socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://127.0.0.1:9998")

# socket to send messages on
sender = context.socket(zmq.PUSH)
sender.connect("tcp://127.0.0.1:9999")

while True:
    s = receiver.recv_string()

    sys.stdout.write('.')
    sys.stdout.flush()

    time.sleep(int(s)*0.001)

    sender.send(b'')

