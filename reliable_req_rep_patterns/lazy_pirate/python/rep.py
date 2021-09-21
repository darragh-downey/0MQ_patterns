#
# https://zguide.zeromq.org/docs/chapter4/#Client-Side-Reliability-Lazy-Pirate-Pattern
# 
# Derived from author: Daniel Lundin <dln(at)eintr(dot)org>
#
#

import os
import time

from dotenv import load_dotenv
import zmq

load_dotenv()

RETRIES = int(os.environ.get("RETRIES")) if os.environ.get("RETRIES") != None else 3
TIMEOUT = int(os.environ.get("TIMEOUT")) if os.environ.get("TIMEOUT") != None else 2500
ENDPOINT = os.environ.get("ENDPOINT") if os.environ.get("ENDPOINT") != None else "tcp://*:9000"

assert RETRIES >= 0, "No value provided for RETRIES"
assert TIMEOUT > 0, "No value provided for TIMEOUT"
assert len(ENDPOINT) > 0, "No value provided for ENDPOINT"

# create the context
context = zmq.Context()
# create the reply socket
socket = context.socket(zmq.REP)
assert socket
# bind the server to the endpoint
socket.bind(ENDPOINT)

cycles = 0

while True:
    request = socket.recv()
    cycles += 1

    if cycles > 3 and cycles % 15 == 0:
        print(f"I: Simulating crash!")
        break
    elif cycles > 3 and cycles % 5 == 0:
        print(f"I: Simulating CPU overload!!")
        time.sleep(2)
    
    print(f"I: Normal request {request}")
    # simulate some computation
    time.sleep(1)

    socket.send(request)

