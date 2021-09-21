#
# https://zguide.zeromq.org/docs/chapter4/#Client-Side-Reliability-Lazy-Pirate-Pattern
# 
# Derived from author: Daniel Lundin <dln(at)eintr(dot)org>
#

import itertools
import os
import sys


from dotenv import load_dotenv
import zmq

load_dotenv()

RETRIES = int(os.environ.get("RETRIES")) if os.environ.get("RETRIES") != None else 3
TIMEOUT = int(os.environ.get("TIMEOUT")) if os.environ.get("TIMEOUT") != None else 2500 # in msecs
ENDPOINT = os.environ.get("ENDPOINT") if os.environ.get("ENDPOINT") != None else "tcp://127.0.0.1:9000"

assert RETRIES >= 0, "No value provided for RETRIES"
assert TIMEOUT > 0, "No value provided for TIMEOUT"
assert len(ENDPOINT) > 0, "No value provided for ENDPOINT"

print(f"Connecting to lazy pirate server")
# The general rule of thumb is to allow one I/O thread per gigabyte of data in or out per second. 
# To raise the number of I/O threads, use the zmq_ctx_set() call before creating any sockets:
context = zmq.Context()
socket = context.socket(zmq.REQ)
# connect to the server endpoint
socket.connect(ENDPOINT)

for sequence in itertools.count():
    request = str(sequence).encode()
    socket.send(request)
    
    retries = RETRIES
    while True:
        if (socket.poll(TIMEOUT) & zmq.POLLIN):
            reply = socket.recv()
            if int(reply) == sequence:
                print(f"I: Server replied OK! {reply}")
                break
            else:
                print(f"E: Malformed reply from server: {reply}")
            
        retries -= 1
        print(f"I: No response from server")
        # socket is confused - close and remove it
        socket.setsockopt(zmq.LINGER, 0)
        socket.close()
        if retries == 0:
            print(f"W: Server appears to be offline, abandoning!!")
            sys.exit()
        
        print(f"I: Reconnecting to server...")
        socket = context.socket(zmq.REQ)
        socket.connect(ENDPOINT)
        print(f"I: Resending request {request}")
        socket.send(request)

