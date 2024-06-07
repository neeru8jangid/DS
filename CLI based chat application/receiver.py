import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # medium  , protocol
# ip_address = "192.168.115.125" #my ip
ip_address = "127.0.0.1" #local host
port_no = 2525 

my_address = (ip_address, port_no)
s.bind(my_address)

while True:
    data = s.recvfrom(100)
    messege = data[0]
    sender_address = data[1] # (ip,port)
    sender_ip = sender_address[0]
    messege = messege.decode('ascii')

    with open(str(sender_ip)+".txt", "a") as file:
        file.write(messege+"\n")
        print(messege)

    #ipadress.txt --> 
    #try foor txt file , image ,pdf  < -- tcp
# hello.txt <-- read all content "filename+|content"

