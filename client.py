import sys
import zmq
import threading
import time
from multiprocessing import Process

# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

sock1 = context.socket(zmq.SUB)
sock1.connect("tcp://127.0.0.1:5680")



# Send a "message" using the socket
name = " ".join(sys.argv[1:])
sock.send_string(name+'-registerxxxxxxx1')
name = sock.recv()
name = name.decode()
print("User[{}] Connected to the chat server.".format(name))

topicfilter = ''
sock1.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

def SendMessage():
    global sock
    while True:
        messD = input("[{}] >".format(name))
        sock.send_string(name+"-"+messD)
        junk = sock.recv()

def getText():
    while True:    
        messageGet = sock1.recv()
        messageGet = messageGet.decode()
        topic, messagedata = messageGet.split('-')
        if topic != name:
            print("[{}]: {}".format(topic,messagedata))


threading.Thread(target=getText).start()
threading.Thread(target=SendMessage).start()






   