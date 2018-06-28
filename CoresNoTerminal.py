print("---BEM-VINDO AO TESTE DE CORES DO TERMINAL---")
print("      (entre 'ajuda' para instruções)")

entrada = ' '

while entrada!='sair':
	texto = entrada
	entrada = input("entrada:")
	contador = 0
	estilo = '0'
	fundo = ''

	while contador < len(entrada) - 1:
		if entrada[contador] == '*':
			entrada, estilo = entrada.split('*')
		contador = contador + 1
	
	contador = 0
	while contador < len(estilo) - 1:
		if estilo[contador] == '#':
			estilo, fundo = estilo.split('#')
		contador = contador + 1

	if fundo == 'cinza':
		fundo = ';40'

	elif fundo == 'vermelho':
		fundo = ';41'

	elif fundo == 'verde':
		fundo = ';42'

	elif fundo == 'amarelo':
		fundo = ';43'

	elif fundo == 'azul':
		fundo = ';44'

	elif fundo == 'violeta':
		fundo = ';45'

	elif fundo == 'ciano':
		fundo = ';46'

	elif fundo == 'branco':
		fundo = ';47'

	else:
		fundo = ''

	if estilo == 'negrito':
		estilo = '1'
	elif estilo == 'sublinhado':
		estilo = '4'
	elif estilo == 'negativo':
		estilo = '7'
	else:
		estilo = '0'

	cinza = "\033["+estilo+";30"+fundo+"m"
	vermelho = "\033["+estilo+";31"+fundo+"m"
	verde = "\033["+estilo+";32"+fundo+"m"
	amarelo = "\033["+estilo+";33"+fundo+"m"
	azul = "\033["+estilo+";34"+fundo+"m"
	violeta = "\033["+estilo+";35"+fundo+"m"
	ciano = "\033["+estilo+";36"+fundo+"m"
	branco = "\033["+estilo+";37"+fundo+"m"
	nulo = "\033[m"

	if entrada!='sair':
		if entrada=='ajuda':
			print("Instruções:")
			print("-Entre 'sair' para encerrar.")
			print("-Entre 'cores' para lista de cores.")
			print("-Entre uma cor da lista apos entrada de texto para colorir.")
			print("-Entre estilos para lista de estilos.")
			print("-Adicione estilo com cor da lista seguida de '*' e estilo da lista.")
			print("-Adcione cor de fundo com '#' seguido de cor da lsita ao final da entrada de cor.")

		if entrada=='cores':
			print("Lista de cores:"+nulo)
			print("-"+cinza+"cinza"+nulo)
			print("-"+vermelho+"vermelho"+nulo)
			print("-"+verde+"verde"+nulo)
			print("-"+amarelo+"amarelo"+nulo)
			print("-"+azul+"azul"+nulo)
			print("-"+violeta+"violeta"+nulo)
			print("-"+ciano+"ciano"+nulo)
			print("-"+branco+"branco"+nulo)

		if entrada == 'estilos':
			print("-\033[1mnegrito"+nulo)
			print("-\033[4msublinhado"+nulo)
			print("-\033[7mnegativo"+nulo)
			print("-nulo")

		if entrada == 'cinza':
			print(cinza+texto+nulo)

		if entrada == 'vermelho':
			print(vermelho+texto+nulo)

		if entrada == 'verde':
			print(verde+texto+nulo)

		if entrada == 'amarelo':
			print(amarelo+texto+nulo)

		if entrada == 'azul':
			print(azul+texto+nulo)

		if entrada == 'violeta':
			print(violeta+texto+nulo)

		if entrada == 'ciano':
			print(ciano+texto+nulo)

		if entrada == 'branco':
			print(branco+texto+nulo)

		if entrada == 'arco iris':
			print(cinza+"a"+vermelho+"r"+amarelo+"c"+verde+"o "+ciano+"i"+azul+"r"+violeta+"i"+branco+"s"+nulo)

