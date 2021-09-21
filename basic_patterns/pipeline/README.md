## Parallel Pipeline (Divide and Conquer)

![Parallel Pipeline](https://zguide.zeromq.org/images/fig5.png)


* The workers connect upstream to the ventilator, and downstream to the sink. This means you can add workers arbitrarily. If the workers bound to their endpoints, you would need (a) more endpoints and (b) to modify the ventilator and/or the sink each time you added a worker. We say that the ventilator and sink are stable parts of our architecture and the workers are dynamic parts of it.

* We have to synchronize the start of the batch with all workers being up and running. This is a fairly common gotcha in ZeroMQ and there is no easy solution. The zmq_connect method takes a certain time. So when a set of workers connect to the ventilator, the first one to successfully connect will get a whole load of messages in that short time while the others are also connecting. If you don’t synchronize the start of the batch somehow, the system won’t run in parallel at all. Try removing the wait in the ventilator, and see what happens.

* The ventilator’s PUSH socket distributes tasks to workers (assuming they are all connected before the batch starts going out) evenly. This is called *load balancing* and it’s something we’ll look at again in more detail.

* The sink’s PULL socket collects results from workers evenly. This is called *fair-queuing*.


![Fair Q-ing](https://zguide.zeromq.org/images/fig6.png)

The pipeline pattern also exhibits the “slow joiner” syndrome, leading to accusations that PUSH sockets don’t load balance properly. If you are using PUSH and PULL, and one of your workers gets way more messages than the others, it’s because that PULL socket has joined faster than the others, and grabs a lot of messages before the others manage to connect. If you want proper load balancing, you probably want to look at the load balancing pattern in Chapter 3 - Advanced Request-Reply Patterns.