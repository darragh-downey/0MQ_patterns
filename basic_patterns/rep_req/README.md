#### Request-reply
Connects a set of clients to a set of services. This is a remote procedure call and task distribution pattern.
![hello_world](https://zguide.zeromq.org/images/fig2.png)

Let us explain briefly what these two programs are actually doing. They create a ZeroMQ context to work with, and a socket. Don’t worry what the words mean. You’ll pick it up. The server binds its REP (reply) socket to port 5555. The server waits for a request in a loop, and responds each time with a reply. The client sends a request and reads the reply back from the server.

If you kill the server (Ctrl-C) and restart it, the client won’t recover properly. Recovering from crashing processes isn’t quite that easy. Making a reliable request-reply flow is complex enough that we won’t cover it until Chapter 4 - Reliable Request-Reply Patterns.