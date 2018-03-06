import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

sock1 = context.socket(zmq.PUB)
sock1.bind("tcp://127.0.0.1:5680")

# Run a simple "Echo" server
while True:
    message = sock.recv()
    message = message.decode()
    topic, messagedata = message.split('-')
   
    if messagedata == 'registerxxxxxxx1':
        sock.send_string(topic)
    else:
        sock.send_string(messagedata)
        sock1.send_string("%s-%s" % (topic, messagedata))

    
    

    