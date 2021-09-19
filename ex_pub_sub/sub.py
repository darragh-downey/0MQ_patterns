
import zmq

context = zmq.Context()

sub = context.socket(zmq.SUB)
sub.connect("tcp://127.0.0.1:9998")

sub.setsockopt_string(zmq.SUBSCRIBE, "star")

total_temp = 0
for i in range(0, 6):
    message = sub.recv_string()
    _, zip_code, temp, humidity = message.split()
    total_temp += int(temp)

print(f"Average temp for Manly {zip_code} was: {total_temp/5}C")



