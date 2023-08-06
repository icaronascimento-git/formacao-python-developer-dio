print(10 + 8 + 36)
print(5 * 6)
print("Python")

age, name = (26, 'Ícaro Nascimento')
print(f'Meu nome é {name} e tenho {age} anos(s).')

age, name = (27, 'Ícaro Gabriel')
print(f'Meu nome é {name} e tenho {age} anos') # O f no ínicio da string indica que vou usar variáveis nessa string

limite_saque_diario = 1000 # Padrão snake_case

STATES_BRAZILIAN = ('SP', 'MG', 'AC', 'MT') # Variável toda em maiúscula para indicar que se trata de constante

print(int(1.9)) # O int coverte o valor quebrado 1.9 em valor inteiro
print(int("10"))
print(float("10.10"))
print(float(100))

print(51 / 3) # Aqui será realizada a divisão e o resultado mostrará os quebrados
print(51 // 3) # Aqui será realizada a divisão e as barras "//" duplas indicam que será retornado o valor inteiro da divisão

#nome1 = input("Informe o seu nome: ") # o input faz com que o texto seja exibido na tela para o usuário inserir um dado, esse dado inserido será atribuido a variável nome

nome = "Gabriel"
sobrenome = "Silva"

print(nome, sobrenome) # Aqui será exibido na tela o nome e o sobrenome, conforme declarado na variável.
print(nome, sobrenome, end="...\n") # Nesse exemplo estou pedindo para ser adicionado três pontos ao final e o \n fara uma quebra de linha.
print(nome, sobrenome, sep="#") # Nesse exemplo será adicionado o nome e o sobrenome e o sep irá adicionar um separador.

