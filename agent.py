# =============== JOGO DA FORCA =============== #

# =============== IMPORTS =============== #

from pyswip import Prolog
import string
import sys

# =============== FUNÇÕES =============== #

def filtrarLetraPosicao(palavrasVetor, letra, posicaoLetra):
	if(posicaoLetra == 0):
		palavras = list(prolog.query("nao_letra(" + str(letra) + ", " + str(palavrasVetor) + ", Palavras)"))
	else:
		palavras = list(prolog.query("letra_em_posicao(" + str(letra) + ", " + str(posicaoLetra) + ", " + str(palavrasVetor) + ", Palavras)"))
	return palavras[0]['Palavras']

def filtrarLetraNaoPosicao(palavrasVetor, letra, posicaoLetra):
	palavras = list(prolog.query("nao_letra_em_posicao(" + str(letra) + ", " + str(posicaoLetra) + ", " + str(palavrasVetor) + ", Palavras)"))
	return palavras[0]['Palavras']

def printBoneco(num):
	boneco = ['  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========',
					  '  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========',
						'  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========',
						'  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========',
						'  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========',
						'  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========',
						'  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========='
					 ]
	print(boneco[num])

# =============== CÓDIGO =============== #

verbose = False
if len(sys.argv) > 1 and (sys.argv[1] == "-v" or sys.argv[1] == "--verbose"):
	verbose = True
	print("Verbose ativo. O agente irá mostrar as palavras disponíveis a cada iteração.")

prolog = Prolog()
prolog.consult("words.pl")
prolog.consult("rules.pl")

# Popular a lista de palavras
palavras = list(prolog.query("todas_palavras(Palavras)"))[0]['Palavras']

print("Bem-vindo ao jogo da forca! Vamos começar!")

if((verbose) and (input("Deseja listar TODAS as palavras disponíveis (AVISO: 200k+ palavras)? (s/n): ").lower() == 's')):
	print(palavras)

erros = 0
maxErros = 6

tamanhoPalavra = int(input("Digite o tamanho da palavra: "))

palavraVisivel = []

for i in range(0, tamanhoPalavra):
	palavraVisivel.append('_')

# Reduzir a lista para somente as palavras de mesmo tamanho
palavras = list(prolog.query("palavras_tamanho(" + str(palavras) + ", " + str(tamanhoPalavra) + ", Palavras)"))[0]['Palavras']

if(verbose): print(palavras)

frequenciaLetras = {}
for letra in string.ascii_lowercase:
	frequenciaLetras[letra] = 0

tentativa = 0
while True:
	tentativa += 1
	print('---------- Tentativa ' + str(tentativa) + ' ----------')
	for letra in frequenciaLetras:
		frequenciaLetras[letra] = list(prolog.query("contar_letra_base(" + str(letra) + ", " + str(palavras) + ", Contagem)"))[0]['Contagem']

	if(verbose): print('Frequencias:\n' + str(frequenciaLetras))

	# Escolher a letra mais frequente
	letraMaisFrequente = max(frequenciaLetras, key=frequenciaLetras.get)

	if(verbose): print("Letra mais frequente: " + letraMaisFrequente)
		
	if (input("A letra '" + letraMaisFrequente + "' está na palavra? (s/n) ").lower() == 's'):
		quantidadeLetra = int(input("Quantas vezes a letra " + letraMaisFrequente + " aparece na palavra? "))
		print("Informe as posições da letra '" + letraMaisFrequente + "' na palavra")
		aparicoes = []
		for i in range(0, quantidadeLetra):
			aparicaoAtual = int(input(str(i + 1) + "a aparição: "))
			aparicoes.append(aparicaoAtual)
		
			# Atualizar a lista de palavras
			palavras = filtrarLetraPosicao(palavras, letraMaisFrequente, aparicoes[i])

			palavraVisivel[aparicaoAtual - 1] = letraMaisFrequente
		
		# Remover as palavras que possuem a letra em outras posições
		for i in range(0, tamanhoPalavra):
			if (i + 1) not in aparicoes:
				palavras = filtrarLetraNaoPosicao(palavras, letraMaisFrequente, (i + 1))
	else:
		quantidadeLetra = 0
		erros += 1
		palavras = filtrarLetraPosicao(palavras, letraMaisFrequente, 0)
	
	printBoneco(erros)
	print()

	for i in range(0, tamanhoPalavra):
		print(palavraVisivel[i], end=" ")
	print('\n')

	if(verbose): print(palavras)

	if erros == maxErros:
		print("Não consegui adivinhar a palavra!")
		break

	# Verificar se a palavra foi descoberta
	if(len(palavras) == 1):
		if input("A palavra é: " + palavras[0] + "? (s/n): ").lower() == 's':
			print("Acertei!")
			break
		else:
			print("Não tenho essa palavra na minha lista de palavras.")
			break
	if(len(palavras) == 0):
		print("Não tenho esta palavra na minha lista de palavras.")
		break

	# Remover a letra da lista de frequência
	del frequenciaLetras[letraMaisFrequente]

print("Fim do jogo!")