# LISTAS

frutas = ["laranja", "uva", "maca"] # lista com valores

frutas[0]
frutas[2] # Nesses 2 exemplos estou buscando na lista de frutas, aquelas que estão na posição dos índices 0 e 2.

frutas[-1] # Tmabém é possivel retornar os itens da listas do final para o inicio com indices negativos.


carros = [] # Posso também declarar uma lista vazia

letras = list("python") # Aqui será criada uma nova lista com a palavra Python separada letra por letra.

numeros = list(range(10)) # Aqui será criada uma lista de 0 a 10.

# LISTAS ANINHADAS

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0][0]
matriz[0][-1]
matriz[2][1] #Nesses exemplos retorno os índices da linha e coluna, e é possível retornar tanto do inicio > fim quanto o contrario

for matriz in matriz: # A forma mai prática de exibir todos os itens de uma lista é iterando utilizando o comando for.
    print(matriz)
    
# FILTRANDO LISTAS

# Opção 01
numeros = [1, 30, 21, 2, 9, 65, 34] # Lista aleatória com pares e impares.
pares = [] # Lista vazia onde irei retornar os valores que são par da lista anterior

for numeros in numeros:
    if numeros % 2 == 0: # Aqui é feita uma verificação nos numeros que divididos por 2 da 0 (indicando ser par)
        pares.append(numeros)
        
# Opção 2

lista_numeros = [7, 4, 9, 35, 16, 29, 54, 2, 88]
retorna_pares = [lista_numeros for lista_numeros in lista_numeros if lista_numeros % 2 == 0]

# MÉTODOS DA CLASSE LIST

# .append

lista = [] # Definiu uma lista vazia

lista.append(1) # O método append adiciona 1 na lista
lista.append("Python") # append adicionaou uma string a lista.
lista.append([40, 30, 20])

# .clear

lista_compras = ["feijão", "arroz", "macarrão"] 

print(lista_compras) # Vai exibir os dados na tela

lista_compras.clear() # O método append vai limpar a lista

print(lista_compras) # Aqui vai exibir a lista vazia.

# .count

cores = ["Vermelho", "Azul", "Rosa", "Amarelo", "Rosa"]

cores.count("Vermelho")
cores.count("Azul")
# O método count conta quantas vezes determinado valor aparece na lista

# .extend

linguagens = ["python", "js", "c#"]

print(linguagens) # Exibirá na tela os itens da lista

linguagens.extend(["java", "ruby"]) # Aqui adicionará essa linguagens a lista, MAS SEM MUDAR A LISTA ORIGINAL

print(linguagens)

# .index

linguagens.index("java")
linguagens.index("python")
# O .index retorna qual a primeira ocorrência de uma valor na lista, não mostra todas, apenas a primeira.

# .pop

linguagens.pop()
linguagens.pop()
# O .po remove os itens da lista de acordo o indice passado no parenteses.

# .remove
linguagens.remove("java")
# O .remove funciona parecido com o .pop, porém no .remove você passa o propio elemento e não o seu índice.

# .reverse

linguagens.reverse()
print(linguagens)
# O .reverse basicamente irá inverter os elementos da lista (de trás para frente).

# .sort

linguagens.sort() # O .sort colocará a lista em ordem crescente/alfabética.

linguagens.sort(reverse=True) # Aqui a lista ficará invertida (Iniciará no maior (por conta do reverse)) e ficará em ordem decrescente (por conta do sort).

linguagens.sort(key=lambda x: len(x)) # Fará a lista ser ordenada pelo tamanho do elemento (quantidade de caracteres e/ou palavras), que ele possuí.

linguagens.sort(key=lambda x: len(x), reverse=True)

# len

len(linguagens) # O len serve para verificar o tamanho dos itens, nesse caso aqui, quantos elementos a lista possuí.

# sorted() - Funciona parecido com o .sort, porém ele é uma função.





