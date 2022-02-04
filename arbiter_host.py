import socket
import random

def compute_numbers():
    sum = 8 if random.random() < 0.5 else 10

    num1 = random.randint(0, sum)
    num2 = sum - num1

    return (num1, num2)

UDP_IP = input('Client IP: ')
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

print(f'Will send data to {UDP_IP}:{UDP_PORT}')

while True:
    input('Prees enter to give numbers')
    num1, num2 = compute_numbers()
    sock.sendto(bytes([num1]), (UDP_IP, UDP_PORT))

    print('Your number:')
    print(num2)