print("---BEM-VINDO AO TESTE DE CORES DO TERMINAL---")
print("      (entre 'ajuda' para instruções)")

orig = 'Criado por Gustavo (GitHub: GustavoM7) ;)' #variável para 'memória externa' dentro do loop

cores = {'cinza':'30', 'vermelho':'31', 'verde':'32', 'amarelo':'33', 'azul':'34', 'violeta':'35', 'ciano':'36', 'branco':'37'} #dicionário para valores das cores
fundos = {'cinza':';40m', 'vermelho':';41m', 'verde':';42m', 'amarelo':';43m', 'azul':';44m', 'violeta':';45m', 'ciano':';46m', 'branco':';47m','nulo':'m'} #dicionário para valores das cores de fundo
estilos = {'nulo':'\033[0;','negrito':'\033[1;','sublinhado':'\033[4;', 'negativo':'\033[7;'} #dicionário para valores dos estilos
nulo = "\033[m" #variável para limpar configurações do terminal

while True: #cria loop que será quebrado com entrada 'sair'.
	texto = orig  #guarda a última entrada do loop na memória.
	entrada = input("entrada:")
	orig = entrada #salva entrada com formatação original
	entrada = entrada.lower() #formata string para reconhecer variações de maiúsculo e minúsculo

	if entrada == 'sair': #verifica se entrada pede saída e encerra o programa
		break

	if entrada == 'ajuda': #caso de entrada para instruções
		print("Instruções:")
		print("-Entre 'sair' para encerrar.")
		print("-Entre 'cores' para lista de cores.")
		print("-Entre uma cor da lista apos entrada de texto para colorir.")
		print("-Entre estilos para lista de estilos.")
		print("-Adicione estilo com cor da lista seguida de '*' e estilo da lista.")
		print("-Adcione cor de fundo com '#' seguido de cor da lsita ao final da entrada de cor.")

	elif entrada == 'cores': #caso de entrada para lista de cores
		print("Lista de cores:"+nulo)
		print("-\033[0;30mcinza"+nulo)
		print("-\033[0;31mvermelho"+nulo)
		print("-\033[0;32mverde"+nulo)
		print("-\033[0;33mamarelo"+nulo)
		print("-\033[0;34mazul"+nulo)
		print("-\033[0;35mvioleta"+nulo)
		print("-\033[0;36mciano"+nulo)
		print("-\033[0;37mbranco"+nulo)

	elif entrada == 'estilos': #caso de entrada para lista de estilos
		print("-\033[1mnegrito"+nulo)
		print("-\033[4msublinhado"+nulo)
		print("-\033[7mnegativo"+nulo)
		print("-nulo")

	else:
		cor = entrada #salva valor da entrada para manipulação
		estilo = 'nulo' #valor padrão para estilo
		if '*' in cor: #verifica se há e salva comando para adicionar estilo (*)
			try: #testa se é possível separa em somente daus variáveis
				cor, estilo = cor.split('*')
			except:
				estilo = 'erro'

		fundo = 'nulo' #valor padrão para fundo
		if '#' in estilo: #verifica se há e salva comando para adicionar fundo (#)
			try:#testa se é possível separar em somente duas variáveis
				estilo, fundo = estilo.split('#')

			except:
				fundo = 'erro'
		if '#' in cor: #verifica se há e salva comando para adicionar fundo (#)
			try:#testa se é possível separar em somente duas variáveis
				cor, fundo = cor.split('#')
			except:
				fundo = 'erro'

		if (estilo in estilos) and (cor in cores) and (fundo in fundos): #verifica validade das entradas e mostra teste com comando
			print(estilos[estilo]+cores[cor]+fundos[fundo]+texto+nulo)
		
		else: #assume entrada de texto
			print("-Entrada de texto registrada.")

