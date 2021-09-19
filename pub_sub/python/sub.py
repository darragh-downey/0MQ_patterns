
import zmq


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:9999")

# You MUST set a socket option for SUB sockets
# an empty string will accept all otherwise it will filter based on first
# element of message
socket.setsockopt_string(zmq.SUBSCRIBE, "2095")

total_temp = 0
for i in range(0, 6):
    message = socket.recv_string()
    zip_code, temp, humidity = message.split()
    total_temp += int(temp)

print(f"Average temp for Manly {zip_code} was: {total_temp/5}C")
