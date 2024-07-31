from cozinheiro import ConexaoCLP


# Sistema de Salvar a lista de IPs
sinais = [
        ConexaoCLP('172.17.85.114', 'B10:2/6'),
        ]

# Mostrar IPs
print("Dispositívos salvos:")
i = 0
for sinal in sinais:    
    print(f'[{i}] {sinal}')
    i += 1

# Sistema de escolher um IP para se conectar
sinal = input("Sinal: ")
if sinal.isnumeric():
    sinal = sinais[int(sinal)]
else:
    exit('Invalid Input')


# Mostrar Status Inicial
print(f'Status Inicial: {sinal.read()}')

# Decidir a mensagem antes de enviar
print("Olá senhor, o que deseja? [on / off]")
state = input("> ")
if state == 'on':
    state = True
elif state == 'off':
    state = False
else:
    exit('Invalid state')


# Realizar a conexão, escrever valor e mostrar resposta
print(f'Resposta: {sinal.write(state)}')
print(f'Status: {sinal.read()}')

