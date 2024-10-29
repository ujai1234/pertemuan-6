import socket
from termcolor import colored

def scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        service_version = sock.recv(1024)
        service_version = service_version.decode('utf-8').strip('\n')
        port_state = f'Port {port} is open'
        print(colored(port_state, 'yellow'), end='   ')
        print(service_version)
    except ConnectionRefusedError:
        print(colored(f'Port {port} is closed', 'red'))
    except UnicodeDecodeError:
        print(colored(f'Port {port} is open', 'yellow'))

target = input("Target: ")
ports = input("Port: ")

if ',' in ports:
    port_list = ports.split(',')
    for port in port_list:
        scan(target, int(port))
elif '-' in ports:
    port_range = ports.split('-')
    start = int(port_range[0])
    end = int(port_range[1])
    for port in range(start, end+1):
        scan(target, port)
else:
    scan(target, int(ports))
