import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target_ip = '127.0.0.1'
port_no = 2525
target_address = (target_ip,port_no)
quiet = True
while True:
    message = input('please enter your messege')
    message_encryp = message.encode('ascii')
    s.sendto(message_encryp, target_address)
    print('your messsege has been sent')
    user_input= input('do you want to quit it press Y/N :')
    if user_input =="y" or user_input == "n":
        quiet= False
 
 