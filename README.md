Aqui é possível acompnahar todas as notações que fiz durante a realização do curso FORMAÇÃO EM PYTHON da plataforma DIO, curos com carga hoária de 64 horas.

**CURSO 01: Ambiente de Desenvolvimento e Primeiros Passos com Python**

    1. Introdução ao Python
		a. Origem
			i. Nasceu em 1989 como um hobby, do programador Guido Van Rossum. A ideia inicial era dar continuidade a linguagem ABC, que era desenvolvida no Centro de Pesquisa Holandês (CWI)
			ii. Os Objetivos de Van Rossum para a linguagem Python eram:
				1) Uma linguagem fácil e intuitiva.
				2) Código aberto, para que todos possam contribuir
				3) Código tão inteligível quanto inglês.
				4) Adequada para tarefas diárias, e produtiva
			iii. Em 1994 nasce a versão 1.9 do PYTHON e em 1995 é lançada a versão 1.2.
			iv. Em 2001 nasce a Python Software Foundation (PSF).
			v. Em 2008 é lançada a versão 3.0, que resolveu muitos problemas de design da linguagem e melhorou a performance.
			
	2. Onde Utilizar a Linguagem?
		a. Só não é bom para APP MOBILE
		b. É uma linguagem versátil!
			i. Tipagem dinâmica e forte
			ii. Multiplataforma e multiparadigma
			iii. Comunidade gigante e ativa
			iv. Curva de aprendizagem baixa
			
	3. Configurando o ambiente de desenvolvimento
		a. Instalando o Python
			i. Acesse o python.org e baixe a versão estável mais recente do Python e instale no Windows
			ii. Para máquinas Linux e MacOS o Python já vem instalado
				1) É possível verificar a versão ou se o pyhton está devidamente instalado utilizado os comando: python -v ou python3 -v.
			
		b. IDE'S para utilizar
			i. VSCode
				1) Ao utilizar o VSCode, instale as extensões para utilizar o pyhon:
					a) Python InteliSense
					b) autoDocstring
					c) Python Extesion Pack
					d) Visual Studio IntelliCode
			ii. PyCharm
			iii. Vim
			iv. Eclipse
		

**CURSO 02: Conhecendo a linguagem de programação Python**

	1. Tipo de Dados
		a. Por que usamos tipos?
			i. Os tipos de dados servem para definir as características e comportamentos de um valor (objeto) para o interpretador. Com esses tipos eu sou capaz de realizar operações matemáticas. Esse tipo para ser armazenado em memória irá consumir 24 bytes.
			ii. Alguns do tipos buil-in são:
				1) Texto
					a) Str
				2) Numérico
					a) Int, float, complex
				3) Sequência
					a) List, tuple, range
				4) Mapa
					a) Dict
				5) Coleção
					a) Set, fronzenset
				6) Booleano
					a) Booll
				7) Binário
					a) Bytes, bytearray, memoryview
			iii. Números inteiros são representados pela classe int e possuem precisão ilimitada.
			iv. Os números flutuantes são usados para representar os números racionais e sua implementação é feita pela classe float.
			v. É usado para representar verdadeiro ou falso, e é implementado pela classe bool. Em Python o tipo booleano é uma subclasse de int, uma vez que qualquer número diferente de 0 representa verdadeiro e 0 representa falso.
			vi. STRINS ou cadeia de caracteres são usadas para representar valores alfanuméricos, em Python as strings são definidas utilizando a classe str.
			
	2. Modo Interativo
		a. Usando o Modo interativo
			i. O interpretador Python pode executar em modo que possibilite o desenvolvedor escrever código, e ver o resultado na hora.
			ii. Existem duas formas de iniciar o modo interativo, chamando apenas o interpretador (python) ou executando o script com a flag -i (python -i app.py). Para sair do modo interativo utilize o comando exit()
			iii. Dir(): Retorna a lista de métodos
			iv. Help(): Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável.
			
	3. Variáveis e Constantes
		a. Variáveis
			i. Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.
		b. Constantes
			i. Constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.
			ii. Não existe uma palavra reservada para informar ao interpretador em Python que o valor é constante. Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maiúsculas.
		c. Boas práticas
			i. O padrão de nomes deve ser snake case.
				1) Ex: essa_variavel_declarada
			ii. Escolher nomes sugestivos
				1) Nomear ás variáveis de forma que seja fácil entender para que ela existe.
			iii. Nome de constantes todo em maiúsculo
	4. Conversão de Tipos
		a. Convertendo Tipos
			i. Em alguns momentos é necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo: Variáveis do tipo string, que armazena números e precisamos fazer alguma operação matemática com esse valor 
	5. Funções de entrada e saída
		a. Lendo valores com a função input
			i. A função built input é utilizada quando queremos ler dados de entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.
		b. Lendo valores com a função print
			i. A função built print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário
	
	
			

			

