# Funções exemplo
def exibir_mnesagem(): # Nome identificador da função. o def é para mostrar ao interpretador que ali se trata de uma função.
    print("Olá Mundo!") # Bloco de códigos.
    
def exibir_mensagem_2(nome): # Aqui passei a função com argumento nome
    print(f"Seja bem vindo: {nome}!") # O f indica que vou passa variável na string e a váriavel é o parâmetro nome, que passei na função exibir_mensagem_2
    
def exibir_mensagem_3(nome="Ícaro"):
    print(f"Seja bem vindo {nome}") # Aqui passei a mensgaem e a variável nome que foi definida no parametro da função como "Ícaro"
    

# Após declarar a função e passar todos seus parâmetros eu preciso executar (chamar função).
exibir_mnesagem() 
exibir_mensagem_2(nome="Gabriel") # Aqui será executado a função passando um argumento.
# Ao declarar a função, se eu não passar o valor em defalt no momentoda sua declaração, obrigatoriamente vou precisar passar o parâmetro no momento da sua execução.
exibir_mensagem_3()
exibir_mensagem_3(nome="Nascimento")
    
# Usando o return

def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

print(calcular_total([10, 20, 30]))
print(retornar_antecessor_e_sucessor(10))


#PARÂMETROS

#Parametros por posição
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # Os parâmetros após a barra posso passa0los por posição e nome ou só por posição mesmo.
    print(modelo, ano, placa, marca, motor, combustivel) # Os parâmtros antes da barra serão obrigat´roios serem passados por posição.
   
# Parâmetros por posição e nome
def criar_carro(modelo="Palio", ano="1999", placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina"):
    print(modelo, ano, placa)