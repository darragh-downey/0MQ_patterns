
import datetime
import zmq
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:9999")

while True:
    # update weather
    zip_code = randrange(1, 10000)
    temperature = randrange(-4, 49)
    relhumidity = randrange(0,100)

    socket.send_string(f"{zip_code} {temperature} {relhumidity}")
    print(f"Weather @ {datetime.datetime.now()}: {zip_code} {temperature} {relhumidity}")