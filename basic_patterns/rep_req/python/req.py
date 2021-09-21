import zmq


print(f"Connecting to hello world server")
# The general rule of thumb is to allow one I/O thread per gigabyte of data in or out per second. 
# To raise the number of I/O threads, use the zmq_ctx_set() call before creating any sockets:
context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://127.0.0.1:9999")

for i in range(1, 100):
    socket.send_json({"id": 1, "message": f"{i} hello"})

    message = socket.recv_string()
    print(f"Received response from server: {i} | {message}")

