#coding:utf-8
from socket import*
import time
import threading
from random import *
from  dico import *  # Les dictionnaires contenant les caractères japonais
import sys

"""
Damien il faudrait enlever de la liste de joueurs les gens qui changent de fenêtre ou qui ferment l'application...
"""

class serveur():
	def __init__(self) :
		self.serveur = socket(AF_INET,SOCK_STREAM)
		self.serveur.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

		#self.host = ""
		#self.port = 8000

		self.list_client = []
		self.list_joueur = []
		self.joueur_score = []  # Tuple joueur,score
		self.list_pseudo = []

	# MINI JEU EN 1 CONTRE 1
	def jeu(self,client) :
		pseudo = client.recv(1024)  # Reçoit le pseudo
		client.send("Vous êtes connecté au mini jeu 1v1 !;")
		
		self.list_joueur.append(client)
		
		self.list_pseudo.append(pseudo)
		
		while len(self.list_joueur) != 2 :
			client.send("En attente d'un adversaire...;")
			# client.recv(1024)  # Reçoit ok / 0

		client.send('Adversaire trouvé !;')
		
		game='!'
		while game != 'fini' :  # Attend que le jeu soit fini coté client
			game = client.recv(1024)
			
		
		score = client.recv(1024)  # Reçoit le score
		self.joueur_score.append((pseudo,int(score)))  # Tuple joueur,score
		
		while True :  # Tant que les deux joueurs n'ont pas fini le jeu...
			if len(self.joueur_score) >= 2 :
				break

		# On détermine le gagnant en comparant les scores
		if self.joueur_score[0][1] > self.joueur_score[1][1] :
			gagnant = self.joueur_score[0][0]
		elif self.joueur_score[0][1] < self.joueur_score[1][1] :
			gagnant = self.joueur_score[1][0]
		else :
			gagnant = "Égalité !"
		
		gagnant = str(gagnant)
		client.send("Le gagnant est %s :)" %gagnant) # Annonce le gagnant
		
		# On réinitialise :
		self.joueur_score = []
		self.list_joueur = []
		#client.close()
		#self.list_client.remove(client)
		self.list_pseudo.remove(pseudo)
		choix(self,client)
		
	# Gère les adversaires du mini-jeu 1V1
	def multi_joueur(self,client) :
		print ('hello')
		pseudo = client.recv(1024)  # Recoit le pseudo du joueur
		pseudo = pseudo.decode()
		print(pseudo)
		try :
			self.list_pseudo.append(pseudo)
		except : 
			print('erreur dans la liste de pseudos')
		print("clients connectés : ", self.list_pseudo)
		if len(self.list_pseudo) == 1 :
			client.send("attendre".encode())  # Attente d'un autre joueur
			print("ordre d'attendre envoyé")
			attendre = True
			while attendre == True  :
				if len(self.list_pseudo) >= 2 :
					attendre = False
					self.list_score = []
			client.send("commencer".encode())
			self.choix(client)
			
		elif len(self.list_pseudo) > 2 :  # Pas plus de deux joueurs
			print("serveur plein")
			client.send("serveur_plein".encode())
			self.list_pseudo.remove('pseudo')
			self.choix(client)
			
		else :  # Si tout est bon, commencer !
			print("ordre de commencer !")
			client.send("commencer".encode())
			self.choix(client)
			
	# Compare les deux score pour donner un gagnant
	def calcul_gagnant(self,client) :
		try :
			print('attente de réception du score')
			score = client.recv(1024)  # Recoit le pseudo du joueur
			score = score.decode()
			print('score recu :', score)
			self.list_score.append(score)
			print('liste des scores : ', self.list_score)
			# Pas de calcul du score tant qu'on n'a pas recu le score des 2 joueurs
			self.attendre_resultats = True
			while self.attendre_resultats == True  :
				print("attente du second score")
				if len(self.list_score) >= 2 :
					print("second score reçu !")
					self.attendre_resultats = False
			score_max = max(self.list_score)
			if score_max == score :
				client.send("Winner".encode())
				print("Winner envoyé")
			else :
				client.send("Loser".encode())
				print("Loser envoyé")
		finally :
			#self.list_score = []
			self.list_pseudo = []
			self.choix(client)
		

	# Menu de choix
	def choix(self,client) :
		while True :
			try :
				rep = client.recv(1024)
				print(rep)
				if rep.decode() == "nouveauHiragana" :
					solution = choice(hiragana_)
					msg = hiragana2[solution]  # Envoi d'un nouveau hiragana
					client.send(msg.encode())
					print("Nouveau hiragana envoyé")
					reponse = client.recv(1024).decode()
					print(reponse)
					if reponse != 'STOP':  # Le client change d'exercice
						if reponse == solution :
							client.send("VRAI".encode())
						else :
							client.send(solution.encode())
				if rep.decode() == "nouveauKatakana" :
					solution = choice(katakana_)
					msg = katakana2[solution]  # Envoi d'un nouveau katakana
					client.send(msg.encode())
					print("Nouveau katakana envoyé")
					reponse = client.recv(1024).decode()
					print(reponse)
					if reponse != 'STOP':  # Le client change d'exercice
						if reponse == solution :
							client.send("VRAI".encode())
						else :
							client.send(solution.encode())
				if rep.decode() == "nouveauSigne" :
					solution = choice(lettre_)
					msg = lettre_to_signe[solution]  # Envoit l'image du signe
					client.send(msg.encode())
					print("Nouveau signe envoyé")
					reponse = client.recv(1024).decode()
					print(reponse)
					if reponse != 'STOP':  # Le client change d'exercice
						if reponse == solution :
							client.send("VRAI".encode())
						else :
							client.send(solution.encode())
				if rep.decode() == "multi_hira" or rep.decode() == "multi_kata" or rep.decode() == "multi_LDS" :  # Mini-jeu multijoueur
					print(rep.decode())
					self.multi_joueur(client)
				if rep.decode() == "score" :  # Lancer le calcul du score
					print(rep.decode())
					print("Score ?")
					self.calcul_gagnant(client)
				# Pour se déconnecter...
				if rep.decode() == "DECONNECTION" or rep.decode() == "" :
					print("Fermeture de l'application")
					print("Déconnexion de ",client)
					self.list_client.remove(client)
					client.shutdown(0)
					client.close()
					break
			except : #socket.error:
				print("Erreur dans le choix")
				break
				
	# Connexion client-serveur
	def run(self):
		host = ""
		try :
			port = int(sys.argv[1])
			print ("Écoute sur le port %s" %port)
		except :
			port = 8000
			print ("Écoute sur le port %s (valeur par défault)" %port)
		self.serveur.bind((host,port))
		self.serveur.listen(5)
		while True :
			client , info_client = self.serveur.accept()
			print ("Connexion de ",info_client[0])
			self.list_client.append(client)
			self.list_client.append((client,info_client))
			threading.Thread(target = self.choix, args = (client, )).start()


serveur = serveur()

serveur.run()



