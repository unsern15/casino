 #-*-coding:utf-8 -*
import random
import math

# from random import randrange
def verifier_chiffre_correct(question):
	while True:
		try:
			le_biff = int(raw_input(question))
			print("TOTO")
		except:
			print("La valeur n'est pas correcte")
		print(le_biff)
		if le_biff <= 0:
			print("La valeur n'est pas correcte")
		else:
			print("TA MAMAN")
			return le_biff
	
def verifier_chiffre_correct(question):
	while True:
		try:
			choix = int(raw_input(question))
		except:
			print("La valeur n'est pas correcte")
			#pass
		else:
			if choix <= 0 and choix >=50:
				print("La valeur n'est pas correcte")
				continue
			return choix

le_biff=verifier_chiffre_correct("Combien d'argent voulez-vous apporter à la table    :")
print("Votre cagnotte est actuellement de     ", le_biff)

choix=verifier_chiffre_correct("Veuillez faire votre choix entre les chiffres 0 et 49       :")
if choix % 2 == 0:
	print("vous avez choisis le chiffre     RED ", choix)
else:
	print("vous avez choisis le chiffre     BLACK ", choix)

exit()

choix = input("Veuillez faire votre choix entre les chiffres 0 et 49     :")

while choix<0 or choix>49:
	print("T es con ou tu fais expres ? Je sais pas comment on code autrement, alors fais pas le malin !")
	choix = input("Veuillez faire votre choix entre les chiffres 0 et 49     :")
	

mise = input("Combien désirez vous miser : ")
if mise < 20:
	print("Et baaaah alors ?? On aurait peur de la banque ? ")
elif mise < 20:
	print("Et baaaah voila !! on a enfin compris ! ")
raw_input("Appuyez sur entree ma petite poule")

while le_biff > 0:
	print("Les jeux sont faits !")
	raw_input("C est le moment ou tu commences a avoir peur ? ALLEZ fais pas le fier !")
	raw_input("RIEN NE VA PLUUUUUUUS")
	s = random.randrange(50)
	if s % 2 == 0:
		print("ET LE NUMERO GAGNANT EST LE rouge :", s)
		raw_input("Je parie que tu te dis que ta femme avait raison.... Me tromp-je ?")
	else:
		print("ET LE NUMERO GAGNANT EST LE noir :", s)
		raw_input("Je parie que tu te dis que ta femme avait raison.... Me tromp-je ?")
	if (s == choix):
		print("VOUS AVEZ GAGNEZ ! FELICITATIONS ! vous remportez $ ", mise*3)
		gain = (mise*3)
		le_biff += gain #paul's rustine ?
		print("Il vous reste $",le_biff)
		raw_input("C EST A CE MOMENT LA QUE TU TE DIS QUE SI TU AVAIS MISER PLUS TU AURAIS PU QUITTER TA FEMME")
	elif (s != choix and     # Dans le cas ou ce n'est pas le meme nombre qui sort
		s % 2 == 0 and 
		choix % 2 == 0): 
		print("Pairs ! Rouges ! Vous recuperez la somme de $", mise*0.5)
		gain = (mise-(mise*0.5))
		le_biff += gain
		print("Il vous reste $", le_biff)
		raw_input("Recuperez...recuperez...je vous croyais ici pour gagner")
	elif(s != choix and 
		s % 2 != 0 and 
		choix % 2 != 0): 
		print("Impairs ! Noirs ! Vous recuperez la somme de $", mise*0.5)
		gain = (mise-(mise*0.5))
		le_biff += gain
		print("Il vous reste $", le_biff)
		raw_input("Recuperez...recuperez...je vous croyais ici pour gagner")
	else : 
		print("Perdu ! la banque recupere la somme de $", mise)
		raw_input("Si on additione cela fait quand même.... Roulements de tambours....")
		gain = (-mise)
		le_biff += gain
		print("Il vous reste $", le_biff)
		raw_input("AVEC UN PROGRAMME AUSSI NUL T ES CAPABLE DE PERDRE ? AHAHAHAHHAAHAHAHAHHAAHAHAHAHHAHAAH")
	print(gain)
	mise = input("Combien desirer vous miser : ")
	choix = input("Veuillez faire votre choix entre les chiffres 0 et 49     :")
	while choix<0 or choix>49:
		print("Ceci n'est pas possible")
		choix = input("Veuillez faire votre choix entre les chiffres 0 et 49     :")
		mise = input("Combien desirez vous miser : ")
		if mise < 20:
			print("Et baaaah alors ?? On aurait peur de la banque ? ")
		elif mise < 0:
			print("Nan MAIS SERIEUX ????? tu me prends pour un con la ?")
		elif mise > 20:
			print("Et baaaah voila !! on a enfin compris ! ")
	input("Appuyez sur entree ma petite poule")

	# def resultat(choix):
	# 	if (s == choix):
	# 		print("VOUS AVEZ GAGNEZ ! FELICITATIONS ! vous remportez $ ", mise*3)
	# 		cagnotte += (mise*3)
	# 		print("Il vous reste $",cagnotte)
	# 	elif (s != choix and     # Dans le cas ou ce n'est pas le meme nombre qui sort
	# 		s % 2 == 0 and 
	# 		choix % 2 == 0): 
	# 		print("Pairs ! Rouges ! Vous reécupérez la somme de $", mise*0.5)
	# 		cagnotte += (mise*0.5)
	# 		print("Il vous reste $",cagnotte)
	# 	elif(s != choix and 
	# 		s % 2 != 0 and 
	# 		choix % 2 != 0): 
	# 		print("Impairs ! Noirs ! Vous récupérez la somme de $", mise*0.5)
	# 		cagnotte += mise*0.5
	# 		print("Il vous reste $", cagnotte)
	# 	else : 
	# 		print("Perdu ! la banque recupère la somme de $", mise)
	# 		cagnotte += (-mise)
	# 		print("Il vous reste $", cagnotte)

	# resultat(choix)



# Avant




