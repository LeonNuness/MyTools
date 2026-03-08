#!/usr/bin/env python3
# Exemplo: ./dnsbrute.py xxxx.com /home/usr/wordlist

import dns.resolver
import sys

res = dns.resolver.Resolver()
arquivo = open(sys.argv[2], "r")
subdominios = arquivo.read().splitlines()

alvo = sys.argv[1]

for subdominio in subdominios
    try: 
        sub_alvo = subdominio + "." + alvo
        resultado = res.resolve(sub_alvo, "A")
        for ip in resultado:
            print(sub_alvo, "->", ip)
        sub_alvo = 
        
    except:
        pass

#Agradecimentos especiais a Solyd por disponibilizar o modelo de código