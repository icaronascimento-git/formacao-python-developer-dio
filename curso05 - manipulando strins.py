# String: Maíuscula, minuscula e título
curso = "pYtHon"

print(curso.upper()) #O método upper retorna a string em maiuscula

print(curso.lower()) #O método lower retorna a strign em minuscula

print(curso.title()) #O método title retorna a string com a letra inicial em maiuscula e o restante minuscula

#eliminado espaços em branco
formacao ="      Python Developer"

print(formacao.strip()) #O método strip remove os espaços em brancos da esquerda e da direita

print(formacao.lstrip()) #O método lstrip remove o espaço da esquerda

print(formacao.rstrip()) #O método rstrip remove o espaço em branco da direita

# JUNÇÕES E CENTRALIZAÇÕES

minha_stack = "Python"

print(minha_stack.center(10, "#")) #O método center tem 2 argumensto (o 10 indica o número de caracteres 
#que a string passara a possuir Ex: a palavra python tem 6 caracteres, se infdiquei 10 no argumento do meétodo,
#o python ira inserir mais 4 caracteres na string) e o segundo agumento é para indicar qual caractere você quer inserir nesse espaços em brancos criados.

print(".".join(curso)) # A junção é feita utilizando o join







