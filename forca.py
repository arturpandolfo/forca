import random

palavras = ["televisao", "cachorro", "xicara", "apartamento", "parede"]

palavra = random.choice(palavras)

print (palavra)

tentativas = 0

chances = 6

letras_escolhidas = []

estado_atual = ["_"] * len(palavra)

print ("Bem vindo ao jogo da forca, voce tem", chances,"tentativas")

while tentativas < chances and ''.join(estado_atual) != palavra:

	letra = input("\n\nQual letra você quer tentar? ")

	while letra in letras_escolhidas:
		print ("Você escolheu uma letra que já tinha tentado, escolha outra")
		letra = input("\nQual letra você quer tentar? ")

	letras_escolhidas.append(letra)

	if letra in palavra:
		print ("Parabéns, você acertou a letra!")
		for i in range(len(palavra)):
			if letra == palavra[i]:
				estado_atual[i] = letra
	else:
		print ("Que pena, você errou!")
		tentativas = tentativas + 1

	print ("Você já fez", tentativas, "tentativas erradas e ainda tem", chances-tentativas, "tentativas" )

	print ("Esse é o estado atual:")
	print (estado_atual)

	print ("As letras que você já tentou são:")
	for item in letras_escolhidas:
		print (item, end=" ")

if tentativas == chances:
	print ("\n\nVocê perdeu")
	print ("Acabaram suas tentativas")
else:
	print ("\n\nVocê ganhou, parabéns")

print ("A palavra era", palavra)