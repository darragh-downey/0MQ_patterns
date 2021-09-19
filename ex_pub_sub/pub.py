
import zmq
from random import randrange
import datetime

context = zmq.Context()

pub = context.socket(zmq.PUB)
pub.connect("tcp://127.0.0.1:9997")

while True:
    # update weather
    zip_code = randrange(1, 10000)
    temperature = randrange(-4, 49)
    relhumidity = randrange(0,100)

    pub.send_string(f"star {zip_code} {temperature} {relhumidity}")
    print(f"Weather @ {datetime.datetime.now()}: {zip_code} {temperature} {relhumidity}")