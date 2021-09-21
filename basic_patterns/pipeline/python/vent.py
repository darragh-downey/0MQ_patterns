
import zmq
import random
import time


context = zmq.Context()

# socket to send messages on
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:9998")

# socket w/ direct access to the sink: used to synchronize start of batch
sink = context.socket(zmq.PUSH)
sink.connect("tcp://127.0.0.1:9999")

print("Press enter when workers are ready...")
_ = input()
print("Sending tasks to workers")

# The first message to send is '0' and signals start of batch
sink.send(b'0')

random.seed()

total_msec = 0
for task_nbr in range(100):
    # Random workload between 1-100msecs
    workload = random.randint(1, 100)
    total_msec += workload

    sender.send_string(f"{workload}")

print(f"Total expected cost: {total_msec} msec")
# Give 0MQ time to deliver
time.sleep(3)