print(2 + 3) # Adição

print(10 / 2) # Divisão

print(5 * 3) # Multiplicação

print(10 % 3) # Módulo / É o resto da divisão

print(2 ** 3) # Exponênciação


#PRECEDÊNCIA

print(10 - 5 * 2) # Retornará 0

print((10 - 5) * 2) # Retornará 10. O parenteses força a subtração ser realizada primeiro

print(10 ** 2 * 2) # O resultado é 200. Aqui será execultado primeiramente a exponenciação e depois a multiplicação

print(10 ** (2 * 2)) # O resultado é 10000. Aqui será execultado primeiramente a multiplicação e depois a exponenciação

print(10 / 2 * 4) # O resultado é 20. Primeiro será feita a divisão (esquerda > direita), e apos a multiplicação, conforme a regra matematica.

#COMPARAÇÃO

saldo = 200
saque = 450

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)


#ATRIBUIÇÃO 

saldo1 = 500 # Pegou o valor da direita e atribuiu a variável a esquerda
saldo1 += 200 # O += Adiciona 200 ao valor do saldo

print(saldo1)

# LÓGICOS

#saldo1 >= saldo or saldo1 <= saque 

#saldo1 >= saldo and saldo1 <= saque 
    
# ASSOCIAÇÃO

frutas = ["limão", "uva", "laranja"]

print("laranja" in frutas)