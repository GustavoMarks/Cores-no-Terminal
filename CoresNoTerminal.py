print("---BEM-VINDO AO TESTE DE CORES DO TERMINAL---")
print("      (entre 'ajuda' para instruções)")

cinza = "\033[0;30m"
vermelho = "\033[0;31m"
verde = "\033[0;32m"
amarelo = "\033[0;33m"
azul = "\033[0;34m"
violeta = "\033[0;35m"
ciano = "\033[0;36m"
branco = "\033[0;37m"
nulo = "\033[m"

entrada = ' '

while entrada!='sair':
	texto = entrada
	entrada = input("entrada:")
	if entrada!='sair':
		if entrada=='ajuda':
			print("Instruções:")
			print("-Entre 'sair' para encerrar.")
			print("-Entre 'cores' para lista de cores.")
			print("-Entre uma cor da lista apos entrada de texto para colorir.")
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




