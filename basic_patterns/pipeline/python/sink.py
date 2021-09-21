
import sys
import time
import zmq


context = zmq.Context()

sink = context.socket(zmq.PULL)
sink.bind("tcp://*:9999")

# synchronization w/ ventilator
s = sink.recv()

tstart = time.time()

# process 100 confirmations
for task_nbr in range(100):
    s = sink.recv()
    if task_nbr % 10 == 0:
        sys.stdout.write(":")
    else:
        sys.stdout.write(".")
    sys.stdout.flush()

# calculate and report duration of batch
tend = time.time()
print(f"Total elapsed time: {(tend - tstart)*1000} msec")