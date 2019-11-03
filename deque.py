#   Samuel Veloso - Instituto Federal de Alagoas
#   Estrutura de dados - Prof. Ricardo 
#   Simulação de um atendimento de uma fila.
#   A cada um segundo um cliente novo chega.
#   A cada dois clientes chegarem (dois segundos), um cliente é atendido.

import collections
import time
from random import *
import string
from cliente import Cliente

atender = True
quant_atendidos = 0
fila = collections.deque()

def gerar_nome():
    import random
    letras = string.ascii_uppercase
    nome = ''.join(random.choice(letras) for _ in range(5))
    return nome

def gerar_idade():
    return randint(18, 100)

def eh_vip():
    return randint(0,1)
    
def atender_cliente(): 
    if quant_atendidos < 10:
        quant_atendidos += 1
        fila.popleft()
    else:
        quant_atendidos = 0
        fila.pop()

def mostar_dados():
    primeiro = fila.popleft()
    fila.appendleft(primeiro)
    if len(fila) > 1:
        ultimo = fila.pop()
    else:
        ultimo = primeiro
    fila.append(ultimo)
    tam = str(len(fila))
    print("\nCliente no inicio: " + primeiro.nome)
    print("Tamanho da fila: " + tam)
    print("Cliente no final: " + ultimo.nome)

while atender:
    if eh_vip():
        fila.appendleft(Cliente(gerar_nome(), gerar_idade()))
    else:
        fila.append(Cliente(gerar_nome(), gerar_idade()))
    print('\nNovo cliente')
    mostar_dados()
    time.sleep(1)

    if eh_vip():
        fila.appendleft(Cliente(gerar_nome(), gerar_idade()))
    else:
        fila.append(Cliente(gerar_nome(), gerar_idade()))
    print('\nNovo cliente - 1')    
    mostar_dados()
    time.sleep(1)
    
    if quant_atendidos < 10:
        quant_atendidos += 1
        fila.popleft()
    else:
        quant_atendidos = 0
        fila.pop()
    if len(fila) == 0:
        atender = False
    print('\nUm cliente atendido')
    mostar_dados()