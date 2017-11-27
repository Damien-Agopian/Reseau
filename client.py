#coding:utf-8


from socket import*
import time
import threading
import kana


def partition(string):
	#Transforme le string par une liste de mot

	list_word = []
	word = ''
	for char in string :
		word = word+char
		if char == ';' :
			list_word.append(word)
			word = ''
	return list_word

connection = socket(AF_INET,SOCK_STREAM)
connection.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

host = "localhost"
port = 8000

connection.connect((host,port))

print ("Connecté au serveur !")
msg = connection.recv(1024) #Que voulez vous faire
print (msg)
rep = str(raw_input("Votre choix :"))
connection.send(rep)



if rep == "1": #MINI JEU 1V1
	pseudo = raw_input('Entrez votre pseudo:  ')
	connection.send(pseudo)
	msg = connection.recv(1024) #Vous etes co au mini jeu 1v1
	print partition(msg)[0]
	

	
	print "En attente d'Adversaire"

	if "Adversaire trouvé !;" in partition(msg) :
		msg = "Adversaire trouvé !;"

	while msg != "Adversaire trouvé !;":
		#Empeche de lancer le jeu tant qu'il n'y a pas 2 joueur

		msg = connection.recv(1024) #En attente/Adversaire trouvé
		msg = partition(msg)
		if "Adversaire trouvé !;" in msg :
			msg = "Adversaire trouvé !;"
	print "Adversaire trouvé !"
	
	print kana.regles() #Affiche les régles du jeu
	score = kana.exo_hiragana_1v1()#Fait le jeu
		
	connection.send('fini')
	print 'Le jeu est fini. En attente du score adverse...'
	score = str(score)
	
	connection.send(score)  #Envoie le score au serv
		
	gagnant = connection.recv(1024)#Recois le gagnant
	print (gagnant)
		
	

	connection.close()
