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






