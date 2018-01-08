#coding:utf-8

#from romkan import*
from random import *
#from termcolor import colored #Pour ecrire du texte en couleur
							  # colored("hello","red")
import time


hiragana2 ={
	'a' : u'\u3042',
	'i' : u'\u3044',
	'u' : u'\u3046',
	'e' : u'\u3048',
	'o' : u'\u304A',
	'ka' : u'\u304B',
	'ki' : u'\u304D',
	'ku' : u'\u304F',
	'ke' : u'\u3051',
	'ko' : u'\u3053',
	'sa' : u'\u3055',
	'shi' : u'\u3057',
	'su' : u'\u3059',
	'se' : u'\u305B',
	'so' : u'\u305D',
	'ta' : u'\u305F',
	'chi' : u'\u3061',
	'tsu' : u'\u3064',
	'te' : u'\u3066',
	'to' : u'\u3068',
	'ma' : u'\u307E',
	'mi' : u'\u307F',
	'mu' : u'\u3080',
	'me' : u'\u3081',
	'mo' : u'\u3082',
	'ha' : u'\u306F',
	'hi' : u'\u3072',
	'fu' : u'\u3075',
	'he' : u'\u3078',
	'ho' : u'\u307B',
	'na' : u'\u306A',
	'ni' : u'\u306B',
	'nu' : u'\u306C',
	'ne' : u'\u306D',
	'no' : u'\u306E',
	'ra' : u'\u3089',
	'ri' : u'\u308A',
	'ru' : u'\u308B',
	're' : u'\u308C',
	'ro' : u'\u308D',
	'ya' : u'\u3084',
	'yu' : u'\u3086',
	'yo' : u'\u3088',
	'wa' : u'\u308F',
	'n' : u'\u3093',
	'wo' : u'\u3092',
	'ga' : u'\u304C',
	'gi' : u'\u304E',
	'gu' : u'\u3050',
	'ge' : u'\u3052',
	'go' : u'\u3054',
	'za' : u'\u3056',
	'ji' : u'\u3058',
	'zu' : u'\u305A',
	'ze' : u'\u305C',
	'zo' : u'\u305E',
	'da' : u'\u3060',
	#'ji' : to_hiragana('ji'),
	#'du' : to_hiragana('du'),
	'de' : u'\u3067',
	'do' : u'\u3069',
	'ba' : u'\u3070',
	'bi' : u'\u3073',
	'bu' : u'\u3076',
	'be' : u'\u3079',
	'bo' : u'\u307C',
	'pa' : u'\u3071',
	'pi' : u'\u3074',
	'pu' : u'\u3077',
	'pe' : u'\u307A',
	'po' : u'\u307D',
	
} 

hiragana_ = ('a','i','u','e','o'
	,'ka','ki','ku','ke','ko'
	,'sa','shi','su','se','so'
	,'ta','chi','tsu','te','to'
	,'ma','mi','mu','me','mo'
	,'ha','hi','fu','he','ho'
	,'na','ni','nu','ne','no'
	,'ra','ri','ru','re','ro'
	,'ya','yu','yo'
	,'wa','n','wo'
	,'ga','gi','gu','ge','go'
	,'za','ji','zu','ze','zo'
	,'da','de','do'
	,'ba','bi','bu','be','bo'
	,'pa','pi','pu','pe','po'
	) 


katakana2 ={
	'a' : u'\u30A2',
	'i' : u'\u30A4',
	'u' : u'\u30A6',
	'e' : u'\u30A8',
	'o' : u'\u30AA',
	'ka' : u'\u30AB',
	'ki' : u'\u30AD',
	'ku' : u'\u30AF',
	'ke' : u'\u30B1',
	'ko' : u'\u30B3',
	'sa' : u'\u30B5',
	'shi' : u'\u30B7',
	'su' : u'\u30B9',
	'se' : u'\u30BB',
	'so' : u'\u30BD',
	'ta' : u'\u30BF',
	'chi' : u'\u30C1',
	'tsu' : u'\u30C4',
	'te' : u'\u30C6',
	'to' : u'\u30C8',
	'ma' : u'\u30DE',
	'mi' : u'\u30DF',
	'mu' : u'\u30E0',
	'me' : u'\u30E1',
	'mo' : u'\u30E2',
	'ha' : u'\u30CF',
	'hi' : u'\u30D2',
	'fu' : u'\u30D5',
	'he' : u'\u30D8',
	'ho' : u'\u30DB',
	'na' : u'\u30CA',
	'ni' : u'\u30CB',
	'nu' : u'\u30CC',
	'ne' : u'\u30CD',
	'no' : u'\u30CE',
	'ra' : u'\u30E9',
	'ri' : u'\u30EA',
	'ru' : u'\u30EB',
	're' : u'\u30EC',
	'ro' : u'\u30ED',
	'ya' : u'\u30E4',
	'yu' : u'\u30E6',
	'yo' : u'\u30E8',
	'wa' : u'\u30EF',
	'n' : u'\u30F3',
	'wo' : u'\u30F2',
	'ga' : u'\u30AC',
	'gi' : u'\u30AE',
	'gu' : u'\u30B0',
	'ge' : u'\u30B2',
	'go' : u'\u30B4',
	'za' : u'\u30B6',
	'ji' : u'\u30B8',
	'zu' : u'\u30BA',
	'ze' : u'\u30BC',
	'zo' : u'\u30BE',
	'da' : u'\u30C0',
	#'ji' : to_hiragana('ji'),
	#'du' : to_hiragana('du'),
	'de' : u'\u30C7',
	'do' : u'\u30C9',
	'ba' : u'\u30D0',
	'bi' : u'\u30D3',
	'bu' : u'\u30D6',
	'be' : u'\u30D9',
	'bo' : u'\u30DC',
	'pa' : u'\u30D1',
	'pi' : u'\u30D4',
	'pu' : u'\u30D7',
	'pe' : u'\u30DA',
	'po' : u'\u30DD',
	
} 

katakana_ = ('a','i','u','e','o'
	,'ka','ki','ku','ke','ko'
	,'sa','shi','su','se','so'
	,'ta','chi','tsu','te','to'
	,'ma','mi','mu','me','mo'
	,'ha','hi','fu','he','ho'
	,'na','ni','nu','ne','no'
	,'ra','ri','ru','re','ro'
	,'ya','yu','yo'
	,'wa','n','wo'
	,'ga','gi','gu','ge','go'
	,'za','ji','zu','ze','zo'
	,'da','de','do'
	,'ba','bi','bu','be','bo'
	,'pa','pi','pu','pe','po'
	) 


def printj(mot) :#Print japanese characters.
					# Prend en parametre to_hirgana()
					#On encode le kana en utf8 et on le print
	print (mot.encode('utf-8'))


def exo_hiragana2():
	print ("Convertissez en romaji : (taper > fin < pour arreter)")
	reponse = "pas fin"
	while True :
		kana = choice(hiragana_)
		kana_encode = hiragana2[kana]
		print(kana_encode)
		reponse = str(input(": "))
		if kana == reponse :
			print ("Correct")
		elif reponse == 'fin':
			print("A bientot !")
			break

		else :
			print ("Faux, la reponse etait: ",kana)
			#print ("FAUX : ",kana)
			

def exo_katakana2():
	print ("Convertissez en romaji : (taper > fin < pour arreter)")
	reponse = "pas fin"
	while True :
		kana = choice(katakana_)
		kana_encode = katakana2[kana]
		print(kana_encode)
		reponse = str(input(": "))
		if kana == reponse :
			print ("Correct")
		elif reponse == 'fin':
			print("A bientot !")
			break

		else :
			print ("Faux, la reponse etait: ",kana)
			#print ("FAUX : ",kana)



### COMPTE A REBOUR

def countdown(t):
    
    print('Le jeu commencera dans ...')
    while t >= 0:
        print (t)
        time.sleep(1)
        t -= 1
    print('GOOOOO !\n')

###


def exo_hiragana_1v1():
	score = 0

	reponse = "pas fin"
	#print "Le jeu commence dans 10 secondes\n"
	
	countdown(10)
	
	debut = time.time()
	fin = debut
	temps= 0 

	while temps < 15 :
		kana = choice(hiragana_)
		kana_encode = hiragana2[kana]
		print(kana_encode)
		reponse = str(input(": "))
		
		fin = time.time()
		
		if kana == reponse :
			print ("Correct")
			score+=1

		else :
			print ("Faux, la reponse etait: ",kana)
		
		temps = fin - debut
	print ("Votre score est de : ",score)
	return (score)


def regles():
	print ("Convertissez en romaji.")
	print ("Donnez le plus de réponses justes possible en 15 secondes.")
	print ("Le joueur ayant donné le plus de réponses justes gagne !\n")




def choix_exo():
	print ("Quel exercice voulez vous faire : \n")
	print ("1-Hiragana --> Romaji. Traduisez les hiragana en romaji \n")
	print ("2-Katakana --> Romaji. Traduisez les katakana en romaji \n")
	choix = str(input("Tapez 1, 2 ou 3 :  "))
	if choix == "1" :
		exo_hiragana2()
	elif choix == "2" :
		exo_katakana2()
	elif choix == "3" :
		exo_hiragana_1v1()
	else :
		print ("Erreur vous n'avez pas tapé 1, 2 ou 3")


#exo_hiragana2()
