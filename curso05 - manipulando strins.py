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

# INTERPOLAÇÃO DE VÁRIÁVEIS

# Utilizando o método %
nome = "Ícaro"
idade = 28
profissao = "Desenvolvedor de software"
minha_stack = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, minha_stack)) # A %s é para valores do tipo string, %d é para valores do tipo inteiro e %f é para valores de ponto flutuante.

# Utilizando método format

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, minha_stack)) # Esse formato se parece com o anterior.

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(minha_stack, profissao, idade, nome)) # Esse formato se parece com o anterior. Porém os dados entre parentes foram passados em ordem aleatoria, e na numeração entre chaves informa a posição do dado que devera ser retornado.

# Também posso passar o método format informando o nome da propia variavél. A desvantagem é se a variavel se repetir mais de uma vez no código, você tera de ficar escrevendo ela varias vezes. Por isso se dar maior utilização das {} numeradas.

# UTILIZANDO O MÉTODO f-string

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {minha_stack}.") # No f-string já passo a variável diretamente entre as chaves.


# FATIAMENTO DE STRINGS

name = "Ícaro Gabriel Nascimento Silva"

name[0] # Aqui retorna´ra o indice zero da variavel

name[:6] # Os dois pontos no inicio indica que iniciara no zero e só ira parar quando chegar no indice 6

name[10:] # Aqui ele pegara a partir do 10º caracter e só irá parar no fim da string

name[7:15] # Aqui o Python retornara o valores do indice 7 ao 14° (Ele não inclui o 15°).

name[9:12:2] # Aqui o Python pegara a string do intervalo 9 a 12, contando de 2 em 2.

name[:] # Aqui se não passarmos nada ele retornara a string inteira.

name[:: -1] # Aqui vai criar uma cópia da string invertida.

# STRINGS TRIPLAS

mensagem = f'''
    Olá, meu nome {name},
Estou aprendendo Python
    Essa mensagem tem diferentes recuos.
'''
# A strings triplas mantem a formatação do texto, conforme eu passo no código.






