# blco em python
def sacar(self, valor: float):
    if self.slado >= valor:
        self.saldo -= valor
        
        
# ESTRUTURA CONDICIONAL

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque")
    
else:
    print("Saldo insulficiente")
    
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para saque"))
    
elif opcao == 2:
    print("Exibindo o extrato...")
    
#else: sys.exit("Opção Inválida")

# If ternário

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

# UTILIZANDO FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        
print()

# FUNÇÃO RANGE

list(range(10)) # Gera uma sequência de números até 10.

# Utilizando range com for
for numero in range(0,11):
    print(numero, end=" ")
    
# EXIBINDO TABUADA DO 5 
for numero in range(0, 51, 5):
    print(numero, end=" ")
    
# UTILIZANDO O COMANDO WHILE
    
opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] Extrato \n[0] Sair \n: "))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")     
else:
    print("Obrigado por utilizar nosso sistema bancário, até logo!")