import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5007
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
        
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    data = factorial(int(data))
    sock.sendto(str(data), addr)
