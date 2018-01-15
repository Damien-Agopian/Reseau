#coding:utf-8
from socket import*
import time
import threading
from random import *
from  dico import *
import sys

def partition(string):
	list_word = []
	word = ''
	for char in string :
		word = word+char
		if char ==';' :
			list_word.append(word)
			word = ''
	return list_word



class serveur():
	def __init__(self) :


		self.serveur = socket(AF_INET,SOCK_STREAM)
		self.serveur.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

		self.host = ""
		self.port = 8000

		self.list_client = []
		self.list_joueur = []
		self.joueur_score = [] #Tuple joueur/Score
		self.list_pseudo = []
		
	def jeu(self,client) :
		pseudo = client.recv(1024) #Recoit le pseudo
		client.send("Vous êtes connecté au mini jeu 1v1 !;")
		
		self.list_joueur.append(client)
		
		self.list_pseudo.append(pseudo)
		
		while len(self.list_joueur) != 2 :
			client.send("En attente d'un adversaire...;")
			#client.recv(1024) #recoit ok / 0

		client.send('Adversaire trouvé !;')
		
		game='!'
		while game != 'fini' :
			#Attend que le jeu soit fini coté client
			game = client.recv(1024)
			
		
		score = client.recv(1024)#Recois le score
		self.joueur_score.append((pseudo,int(score)))#Tuple joueur/Score
		
		while True :
			#Tant que les deux joueurs n'ont pas fini le jeu...
			if len(self.joueur_score) >= 2 :
				break 
		if self.joueur_score[0][1] > self.joueur_score[1][1] :
			gagnant = self.joueur_score[0][0]

		elif self.joueur_score[0][1] < self.joueur_score[1][1] :
			gagnant = self.joueur_score[1][0]
		else :
			gagnant = "Egalité !"
		
		gagnant=str(gagnant)
		client.send("Le gagnant est %s"%gagnant)
		
		
		self.joueur_score = [] #On vide la liste
		self.list_joueur = []
		client.close()
		#self.list_client.remove(client)
		self.list_pseudo.remove(pseudo)



	def choix(self,client) :
		while True :
			try :
				rep = client.recv(1024)
				print(rep)
				if rep.decode() == "nouveauHiragana" :
					solution = choice(hiragana_)
					msg = hiragana2[solution] #Envoie d'un nouveau caractère
					client.send(msg.encode())
					print("Nouveau hiragana envoyé")
					reponse = client.recv(1024).decode()
					print(reponse)
					if reponse != 'STOP':
						if reponse == solution :
							client.send("VRAI".encode())
						else :
							client.send(solution.encode())
				if rep.decode() == "nouveauKatakana" :
					solution = choice(katakana_)
					msg = katakana2[solution] #Envoi d'un nouveau katakana
					client.send(msg.encode())
					print("Nouveau katakana envoyé")
					reponse = client.recv(1024).decode()
					print(reponse)
					if reponse != 'STOP':
						if reponse == solution :
							client.send("VRAI".encode())
						else :
							client.send(solution.encode())
				if rep.decode() == "nouveauSigne" :
					solution = choice(lettre_)
					msg = lettre_to_signe[solution] #Envoi du nom du fichier image qui correspond au signe
					client.send(msg.encode())
					print("Nouveau signe envoyé")
					reponse = client.recv(1024).decode()
					print(reponse)
					if reponse != 'STOP':
						if reponse == solution :
							client.send("VRAI".encode())
						else :
							client.send(solution.encode())
			except : #socket.error:
				print("Erreur dans choix")
				
				
	def run(self):
		self.serveur.bind((self.host,self.port))
		self.serveur.listen(5)
		while True :
			client , info_client = self.serveur.accept()
			print ("Connexion de ",info_client[0])
			self.list_client.append((client,info_client))
			threading.Thread(target = self.choix , args = (client,)).start()


serveur = serveur()

serveur.run()



