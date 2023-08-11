# UTILIZANDO sets
numeros = set([1, 2, 3, 1, 3, 4]) # O set é utilizado para eliminar registros repetidos em uma lista.
print(numeros)

fruta = set("Carambola") # o Set elimina as palavras repetidas na string.
print(fruta)

# Utilizando função ENUMERATE
carros = {"palio", "celta", "gol", "polo"}

for indice, carros in enumerate(carros):
    print(f"{indice}: {carros}") # A função ENUMERATE criou um indice para a lista de carros

# MÉTODOS DA CLASSE SET

# .union

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.union(conjunto_b)) # O método .unio juntou ambos os conjuntos.

# .intersection

print(conjunto_a.intersection(conjunto_b)) # O método .intersection faz a interseção (exibe os valores em comun em ambos os conjuntos).

# .difference 

print(conjunto_a.difference(conjunto_b)) # Aqui vai ser exibido o valor que tem no conjunto A e não tem no B.
print(conjunto_b.difference(conjunto_a)) # Aqui será exibido os valores que tem no conjunto B e não tem no conjunto A.

# .symmetric_difference

print(conjunto_a.symmetric_difference(conjunto_b)) # Aqui será exibido todos os itens que não estão na interseção do conjnunto A e B. No caso o 1 eo 4.
 # Esse método funciona parecido com o .difference . Porém ele irá exibir os valores que não são comuns a ambos os conjunto de uma só vez.
 
 # .issubset
 # Esse método verifica se um conjunto é subconjunto de outro ( Se todos os itens de um está dentro do outro.)
 
 # .isdisjoint
 
 # .discard
 # Esse método descarta algum valor de uma lista ou conjunto.
 
 # .pop 
 # Esse método vai descarta um valor do conjunto, de acordo o indice passado. Se não passar o indice ele vai descartar o primeiro item do conjunto.
 
lista_valores = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(lista_valores.pop()) #Aqui foi removido o primeiro item do conjunto.
print(lista_valores.pop()) #

print(lista_valores)

# .remove
# Esse método é bem parecido com o .discard, a diferença é que no .remove se eu passar algum parametro que não existe para ser removido do conjunto, ele retorna´ra um erro. Já no .discard ele apenas ignora.

# len
# Esse método verifica o tamanho do conjunto.

# Posso utilizar o in para verificar se determinado item está no meu conjunto de valores.
10 in lista_valores
5 in lista_valores
 
 
