#!/usr/bin/env python3

import socket
import sys

def portscan(ip, portas):

    for porta in portas:

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)

        code = client.connect_ex((ip, porta))
        
        if code == 0:
            print(porta, "OPEN")
    
        client.close()
    print()

if __name__ == "__main__":
    portas = [21,22,80,443,445,3306,25]

    ip = sys.argv[1]
    for arg in sys.argv[2:]:
            portas.append(int(args))

    print("Portas testadas:",portas,"\n")
    portscan(ip, portas)