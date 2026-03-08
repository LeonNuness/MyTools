#!/usr/bin/env python3
import socket
import sys

def portscan(ip, portas):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)

    for porta in portas:
        code = client.connect_ex((ip, porta))
        
        if code == 0:
            print(porta, "Porta Aberta")
        else:
            print(porta, "Porta Fechada")

if __name__ == "__main__":
    ip = sys.argv[1]
    contador = 0
    portas = [21,22,80,443,445,3306,25]

    while True:
        
        if sys.argv[2+contador] == none:
            break
        else:
            portas.append(sys.argv[2 + contador])
            contador+=1
    print("Portas testadas:",portas)
    portscan(ip, porta)

'''
def portscan(ip, porta, mensagem):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect((str(ip), porta))
    client.send(mensagem.encode())

    resposta = client.recv(1024)
    client.close()

    return resposta.decode()


if __name__ == "__main__":
    ip = sys.argv[1]
    porta = int(sys.argv[2])
    mensagem = sys.argv[3]

    print(portscan(ip, porta, mensagem))    
'''