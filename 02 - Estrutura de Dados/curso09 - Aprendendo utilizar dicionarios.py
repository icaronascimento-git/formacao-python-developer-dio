# Dicionário . Exemplos .

pessoa1 = {"nome": "Ícaro", "idade": 28} # Estrutura chave:valor 

pessoa = dict(Nome="Ícaro", Sobrenome="Nascimento", Idade="27", ano_nascimento="1996") # Aqui funciona como o exemplo anterior. Porém foi utilizado o construtor dict.

pessoa["telefone"] = "38 99999-9999" # Nesse exemplo aqui é usado quando eu já possuo um dicionário criado e que ro apenas passar mais um valor para ele.

print(pessoa)

# ACESSANDO OS DADOS DE UM DICIONÁRIO

pessoa["Nome"] # É bem parecido com a lista e o conjunto. Basta passar a variável e o valor que deseja retornar.
pessoa["Sobrenome"]
pessoa["Idade"]

# DICIONÁRIOS ANINHADOS

contatos = { #Aqui foi criado o dicionário "PAI"
    "icaro@gmail.com": {"nome": "Icaro", "telefone": "38 99999-9999"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "38 998888-8888"},
    "nascimento@gmail.com": {"nome": "Nascimento", "telefone": "38 97777-7777"},
    "silva@gmail.com": {"nome": "Silva", "telefone": "38 96666-6666"},
} # Dentro do dicionário "PAI" chamado "contatos" adicionei outros dicionários "FILHOS", que são os contatos cadastrados

print(contatos["gabriel@gmail.com"]["telefone"]) # Para buscar um valor na lista, basta passar a chave principal (que nesse caso é o e-mail) e passar o dado da chave que desejo (nesse caso o telefone).

# ITERAÇÃO DO DICIONÁRIO

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# MÉTODOS DA CLASSE .dict

# .clear
#Utilizado para limpar o dicionário. Ex: contatos.clear() irá limpar todo o dicionário.

# .copy
# Utilizado para alterar os dados do dicionário, mantendo o original intacto.

# .fromkeys
# Ele cria chaves para o dicionário
dict.fromkeys(["sexo", "nacionalidade"]) # Nesse formato cria-se chaves para o dicionário sem adicionar nehum valor

dict.fromkeys(["cidade", "rua"], "vazio") # Nesse formato vai ser criado um conjunto de chaves e será inserido um valor padrão nela.

# .get
# É uma forma de acessar os dados do seu dicionário.

contatos.get("chave") # Retorna None pois esse valor não existe
contatos.get("chave, {}") # Aqui ele vai procurar chave, se não encontrar, retornará vazio
contatos.get("nascimento@gmail.com", {}) # Vai retornar os dados contato, se não existisse retornaria vazio por conta do segundo argumento {}.

# .pop
# Esse método vai apagar a chave do seu dicionário.  

# .popitem
# É parecido com o .pop. A diferença é que a chave não é informada, e ele irá retirando os itens em sequência.
contatos.popitem()

# .setdefault
contatos.setdefault("nome", "Guilherme") # O setsdeafalt verifica se o argumento passado entre as chaves existe no dicionário. Se existir ele vai retornar o valor se não existir e vai passar o valor informado em seu argumento
# No exemplo acima a chave já possuí um valor, se não possuise o método passaria o nome "Guilherme"

# .update
contatos.update({"gabriela@gmail.com": {"nome", "Gabriela", "telefone", "38 55555-5555"}}) # O .update vai atualizar uma chave existente como os novos parâmetros informados. Caso a chave não exista, ele vai criar nova chave.

# in
# o in verifica se existe chaves no dicionário
resultado = "idade" in "icaro@gmail.com"

# del   . é usado para remover chaves do dicionário, e deverá passar qual parametro quer remover.
del contatos["nascimento@gmail.com"]["telefone"]


