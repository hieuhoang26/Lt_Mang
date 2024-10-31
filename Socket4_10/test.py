import  socket
host = "127.0.0.1"
ip_add = socket.gethostbyname(host)
# scan
while 1:
    port_n = int(input("enter port:"))
    try:
        s = socket.socket()
        r = s.connect((ip_add,port_n))
        print("port {}: open ".format(port_n))
    except:
        print("Port {}: close".format(port_n))
