import tkinter as tk
from tkinter import font
from PIL import Image
from PIL import ImageTk
from dico import *
import time
from random import *
from socket import*
import threading
import sys


"""
AMELIORATIONS : 
- regrouper les fonction jeuHira et jeuKata
- mettre des exceptions
- faire des commentaires propres
- faire les mini jeux
- entrainement : si on clique sur commencer pendant le jeu on affiche la réponse...
"""

#CLIENT
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
	
	

"""
class ThreadReception(threading.Thread):
	#objet thread gérant la réception des messages
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connexion = conn		   # réf. du socket de connexion
 
	def run(self):
			message_recu = self.connexion.recv(1024)
			print ("*" + message_recu + "*")
			if message_recu =='' or message_recu.upper() == "FIN":
				#Le thread <réception> se termine ici.
				# On force la fermeture du thread <émission> :
				print (u"Client arrêté. Connexion interrompue.")
				self.connexion.close()

class ThreadSend(threading.Thread):
	def __init__(self, connexion,msg):
		threading.Thread.__init__(self)
		self.connexion = connexion
		self.msg = msg
 
	def run(self):
		self.connexion.send(self.msg.encode())
	
"""



class interface:


	def fenetre(self,name):
		self.nettoyer_fenetre()
		print("fenêtre à ouvrir : ", name)
		if name == 'accueil':
			self.can = tk.Canvas(self.root, width =580, height =200, bg ='blue')
			image = Image.open("accueil.jpg") 
			photo = ImageTk.PhotoImage(image) 
			lab = tk.Label(image=photo)
			lab.image = photo
			lab.pack()
			self.txt = tk.Label(self.root, text='Bienvenue dans notre application d\'apprentissage de langues !')
			self.txt.pack()
			print('Fenêtre par défaut = accueil')
		elif name == 'aide':
			self.can = tk.Canvas(self.root, width =580, height =400, bg ='blue')
			image = Image.open("chien_tient_sa_laisse.jpg") 
			photo = ImageTk.PhotoImage(image) 
			lab = tk.Label(image=photo)
			lab.image = photo
			lab.pack()
			self.txt = tk.Label(self.root, text='On n\'est jamais mieux servi que par soi même.')
			self.txt.pack()
			print('Vous pensiez avoir de l\'aide? Perdu.')
		elif name=='LDS_alphabet_cours':
			self.can = tk.Canvas(self.root, width =360, height =440, bg ='yellow')
			image = Image.open("LDS_cours.jpg") 
			photo = ImageTk.PhotoImage(image) 
			lab = tk.Label(image=photo)
			lab.image = photo
			lab.pack()
			print('Alphabet language des signes')
		elif name=='exerciceLDS':
			self.txt1 = tk.Label(self.root, text ='Trouver la lettre correspondant au signe suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Si vous n\'y arrivez pas, référez-vous au cours. Bisous')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.exerciceLDS)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 6, column=2, columnspan=4)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			self.txt22 = tk.Label(self.root, text='Veuillez répondre en lettres minuscules.')
			self.txt22.grid(row = 5, column=2, columnspan=4, pady=40)
			print('Exercice de langue des signes')
			self.nouveauSigne()
		elif name == 'entrainementLDS':
			self.txt1 = tk.Label(self.root, text ='Trouver la lettre correspondant au signe suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt22 = tk.Label(self.root, text='Veuillez répondre en lettres minuscules.')
			self.txt3 = tk.Label(self.root, text ='Tapez sur \'Entrée\' pour valider votre réponse.')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.entrainementLDS)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt22.grid(row = 5, column=2, columnspan=4, pady=40)
			self.txt2.grid(row=2, column=1)
			self.txt3.grid(row = 5, column=2, columnspan=4)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3, padx =20)
			print('Jeu en solo de langue des signes')
		elif name=='japonais_entrainement_hira':
			self.txt1 = tk.Label(self.root, text ='Convertir le hiragana suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.entrainementHira)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			print('Entrainement hiragana : traduire le plus de caractères en un temps donné')
		elif name=='japonais_jeu_hiragana':
			self.txt1 = tk.Label(self.root, text ='Votre pseudo :')
			self.pseudo = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.pseudo)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.miniJeuHira)
			self.txt1.grid(row =1, column=1, pady=50)
			self.entr1.grid(row=1, column=2)
			self.bout1.grid(row=1, column=3)
			print('Mini jeu en ligne hiragana : Soyez meilleur que les autres joueurs !')
		elif name=='japonais_entrainement_kata':
			self.txt1 = tk.Label(self.root, text ='Convertir le katakana suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.entrainementKata)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			print('Entrainement katagana : traduire le plus de caractères en un temps donné')
		elif name=='japonais_hiragana':
			self.txt1 = tk.Label(self.root, text ='Convertir le hiragana suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.exerciceHiragana)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			print('Exercice 1 : convertir les hiragana.')
			self.nouveauHiragana()
		elif name=='japonais_katakana':
			self.txt1 = tk.Label(self.root, text ='Convertir le katakana suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.exerciceKatakana)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			print('Exercice 2 : convertir les katakana.')	
			self.nouveauKatakana()
		else :
			print('Cette page n\'existe pas encore. Merci de votre compréhension. Vous allez être redirigé vers la page d\'acceuil')
			self.change('accueil')
			
	
	def Send(self,connexion,msg):
		connexion.send(msg.encode())
	

	def Recv(self,connexion):
		self.REPONSE = connexion.recv(1024).decode()	
	
	#=============================================================#
	#                     LDS                                     #
	#=============================================================#
	
	def entrainementLDS(self):
		#supprimer les réponses précédentes
		self.bout1.destroy()
		try : 
			self.txt3.delete(0.0, tk.END)
			self.txt33.delete(0.0, tk.END)
		except :
			print("Premier jeu : pas de réponses à effacer.")
		#printer l'interface
		self.vrai = 0 #nombre de réponses justes/fausses
		self.faux = 0
		self.nouveauSigne()
		self.endTime = time.time() + 10 #le jeu dure 10 secondes
		self.entr1.event_add('<<Return>>', '<KeyPress - Return>')
		self.entr1.bind('<<Return>>', self.nouveauSigneJeu)

			 
		
	def nouveauSigneJeu(self, event):
		reponse = self.entr1.get()
		#Demande de correction au serveur
		if len(reponse) != 0 and time.time()<self.endTime : #self.repondre==True:
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			correction = self.REPONSE #Stock la le nom du fichier envoyé par le serveur
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'):
				self.vrai += 1
			else :
				self.faux += 1
			print ("vrai : ", self.vrai, "      faux : ", self.faux)
			self.nouveauSigne() 
			#self.entr1.config('')
		else :
			print('Fin du temps')
			self.txt33 = tk.Label(self.root, text ="Fin du temps !", fg='red')
			self.txt33.grid(row =4, column=2, pady=10)
			info_serveur = threading.Thread( target = self.Send, args = (connection,"STOP")) #permet de débloquer le serveur en attente de la réponse du joueur
			info_serveur.start()
			info_serveur.join()
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.entrainementLDS)
			self.bout1.grid(row=2, column=3)
		txt = "Score : " + str(self.vrai) + "/" + str(self.vrai+self.faux)
		self.txt3 = tk.Label(self.root, text =txt)
		self.txt3.grid(row =3, column=2, pady=10)
		
				
	def nouveauSigne(self):
		demande_serveur = threading.Thread( target = self.Send, args = (connection,"nouveauSigne"))
		demande_serveur.start()
		demande_serveur.join()
		print("Nouveau Signe")
		thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception du nom du ficher qui contient l'image du signe
		thread_recv.start()
		thread_recv.join()
		print("Nouveau signe recu")
		try :
			self.lab.image = None
		except :
			print ("Unexpected error in nouveauSigne():", sys.exc_info()[0])
		nomImage = self.REPONSE
		image = Image.open(nomImage) 
		photo = ImageTk.PhotoImage(image) 
		self.lab = tk.Label(image=photo)
		self.lab.image = photo
		self.lab.grid(row=1, column=2)

		
	def exerciceLDS(self):
		reponse=self.entr1.get()
		if len(reponse) != 0: #si on a entré une réponse
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			correction = self.REPONSE #Stock la dernière valeur de REPONSE
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'):
				try :
					self.txt5.config(text='Vrai !', fg='green')
				except :
					self.txt5 = tk.Label(self.root, text='Vrai !', fg='green')
					self.txt5.grid(row=4, column =2)
			else :
				rep = 'Faux, la réponse était : ' + self.REPONSE
				try :
					self.txt5.config(text=rep, fg='red')
				except :
					self.txt5 = tk.Label(self.root, text=rep, fg='red')
					self.txt5.grid(row=4, column =2)
			self.nouveauSigne()
		
	#=============================================================#
	#                    Hiragana                                 #
	#=============================================================#
	
	def miniJeuHira(self):
		demande_serveur = threading.Thread(target = self.Send, args = (connection,'multi_hira'))
		demande_serveur.start()
		demande_serveur.join()
		#envoi du pseudo
		self.pseudo = self.entr1.get()
		if len(self.pseudo)!=0 :
			demande_serveur = threading.Thread(target = self.Send, args = (connection,self.pseudo))
			demande_serveur.start()
			demande_serveur.join()
			print("Pseudo envoyé")
			thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'ordre (attendre ou commencer)
			thread_recv.start()
			thread_recv.join()
			if self.REPONSE == 'commencer':
				print('Commencer le jeu')
				self.jeuHira()
			elif self.REPONSE == 'attendre':
				print('Attente de joueur')
				for c in self.root.winfo_children(): #nettoie la fenetre
					c.destroy()
				self.txt1 = tk.Label(self.root, text ='En attente d\'un adversaire...')
				self.txt1.grid(row =1, column=1, pady=50)
				self.menu()
				thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'ordre (attendre ou commencer)
				thread_recv.start()
				thread_recv.join()
				if self.REPONSE == 'commencer':
					print('Commencer le jeu')
					self.jeuHira()
			elif self.REPONSE =='serveur_plein':
				for c in self.root.winfo_children(): #nettoie la fenetre
					c.destroy()
				self.menu()
				self.txt1 = tk.Label(self.root, text ='Le serveur est occupé, veuillez réessayer plus tard.')
				self.txt1.grid(row =1, column=1, pady=50)
				
	def jeuHira(self):
		for c in self.root.winfo_children(): #nettoie la fenetre
			c.destroy()
		self.menu()
		self.txt1 = tk.Label(self.root, text ='Convertir le hiragana suivant :')
		self.txt2 = tk.Label(self.root, text='Votre réponse :')
		self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
		self.caractere = tk.StringVar()
		self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
		self.bout1 = tk.Button(self.root, text="Commencer", command=self.entrainementHira)
		self.txt1.grid(row =1, column=1, pady=50)
		self.txt2.grid(row =2, column=1)
		self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
		self.entr1.grid(row=2, column=2)
		self.bout1.grid(row=2, column=3)
		self.entrainementHira()
		if time.time() > self.endTime :
			print("temps écoulé")
			score = self.vrai
			demande_serveur = threading.Thread(target = self.Send, args = (connection,'score')) #envoi du score
			demande_serveur.start()
			demande_serveur.join()
			print("score send")
			demande_serveur = threading.Thread(target = self.Send, args = (connection,str(score)))
			demande_serveur.start()
			demande_serveur.join()
			thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #réception du résultat
			thread_recv.start()
			thread_recv.join()
			if self.REPONSE == 'Winner':
				self.txt33.config(text ="Gagné !", fg='green')
			else :
				self.txt33.config(text ="Perdu...", fg='red')

	
	def nouveauHiragana(self):
		demande_serveur = threading.Thread( target = self.Send, args = (connection,"nouveauHiragana"))
		demande_serveur.start()
		demande_serveur.join()
		print("Hello")
		thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'hiragana
		thread_recv.start()
		thread_recv.join()
		print("done")
		self.txt4 = tk.Label(self.root, text = self.REPONSE,  font=self.bigFont)
		self.txt4.grid(row = 1, column=2)
		
	def exerciceHiragana(self):
		reponse=self.entr1.get()
		if len(reponse) != 0: #si on a entré une réponse
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			correction = self.REPONSE #Stock la dernière valeur de REPONSE
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'):
				try :
					self.txt5.config(text='Vrai !', fg='green')
				except :
					self.txt5 = tk.Label(self.root, text='Vrai !', fg='green')
					self.txt5.grid(row=4, column =2)
			else :
				rep = 'Faux, la réponse était : ' + correction + ' = ' + self.REPONSE
				try :
					self.txt5.config(text=rep, fg='red')
				except :
					self.txt5 = tk.Label(self.root, text=rep, fg='red')
					self.txt5.grid(row=4, column =2)
			self.nouveauHiragana()
	
	def entrainementHira(self):
		self.bout1.destroy()
		#supprimer les réponses précédentes
		try : 
			self.txt3.delete(0.0, tk.END)
			self.txt33.delete(0.0, tk.END)
		except :
			print("Premier jeu : pas de réponses à effacer.")
		#printer l'interface
		self.vrai = 0 #nombre de réponses justes/fausses
		self.faux = 0
		self.nouveauHiragana()
		self.endTime = time.time() + 10 #le jeu dure 10 secondes
		self.entr1.event_add('<<Return>>', '<KeyPress - Return>')
		self.entr1.bind('<<Return>>', self.nouveauHiraJeu)

	def nouveauHiraJeu(self, event):
		reponse = self.entr1.get()
		#Demande de correction au serveur
		if len(reponse) != 0 and time.time()<self.endTime : #self.repondre==True:
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			correction = self.REPONSE #Stock la le nom du fichier envoyé par le serveur
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'):
				self.vrai += 1
			else :
				self.faux += 1
			print ("vrai : ", self.vrai, "      faux : ", self.faux)
			self.nouveauHiragana() 
			#self.entr1.config('')
		else :
			print('Fin du temps')
			self.txt33 = tk.Label(self.root, text ="Fin du temps !", fg='red')
			self.txt33.grid(row =4, column=2, pady=10)
			info_serveur = threading.Thread( target = self.Send, args = (connection,"TEMPS_ECOULE")) #permet de débloquer le serveur en attente de la réponse du joueur
			info_serveur.start()
			info_serveur.join()
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.entrainementHira)
			self.bout1.grid(row=2, column=3)
		txt = "Score : " + str(self.vrai) + "/" + str(self.vrai+self.faux)
		self.txt3 = tk.Label(self.root, text =txt)
		self.txt3.grid(row =3, column=2, pady=10)

	
	#=============================================================#
	#                     Katakana                                #
	#=============================================================#
	
	
	def entrainementKata(self):
		self.bout1.destroy()
		#supprimer les réponses précédentes
		try : 
			self.txt3.delete(0.0, tk.END)
			self.txt33.delete(0.0, tk.END)
		except :
			print("Premier jeu : pas de réponses à effacer.")
		#printer l'interface
		self.vrai = 0 #nombre de réponses justes/fausses
		self.faux = 0
		self.nouveauKatakana()
		self.endTime = time.time() + 10 #le jeu dure 10 secondes
		self.entr1.event_add('<<Return>>', '<KeyPress - Return>')
		self.entr1.bind('<<Return>>', self.nouveauKataJeu)
	
	def nouveauKataJeu(self, event):
		reponse = self.entr1.get()
		#Demande de correction au serveur
		if len(reponse) != 0 and time.time()<self.endTime : #self.repondre==True:
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			correction = self.REPONSE #Stock la le nom du fichier envoyé par le serveur
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'):
				self.vrai += 1
			else :
				self.faux += 1
			print ("vrai : ", self.vrai, "      faux : ", self.faux)
			self.nouveauKatakana() 
			#self.entr1.config('')
		else :
			print('Fin du temps')
			self.txt33 = tk.Label(self.root, text ="Fin du temps !", fg='red')
			self.txt33.grid(row =4, column=2, pady=10)
			info_serveur = threading.Thread( target = self.Send, args = (connection,"STOP")) #permet de débloquer le serveur en attente de la réponse du joueur
			info_serveur.start()
			info_serveur.join()
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.entrainementKata)
			self.bout1.grid(row=2, column=3)
		txt = "Score : " + str(self.vrai) + "/" + str(self.vrai+self.faux)
		self.txt3 = tk.Label(self.root, text =txt)
		self.txt3.grid(row =3, column=2, pady=10)
		
	def nouveauKatakana(self):
		demande_serveur = threading.Thread( target = self.Send, args = (connection,"nouveauKatakana"))
		demande_serveur.start()
		demande_serveur.join()
		print("Fonction nvx kata")
		thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'hiragana
		thread_recv.start()
		thread_recv.join()
		print("Nvx Kata recu")
		self.txt4 = tk.Label(self.root, text = self.REPONSE,  font=self.bigFont)
		self.txt4.grid(row = 1, column=2)
		
		
	def exerciceKatakana(self):
		reponse=self.entr1.get()
		if len(reponse) != 0: #si on a entré une réponse
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			correction = self.REPONSE #Stock la dernière valeur de REPONSE
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'):
				try :
					self.txt5.config(text='Vrai !', fg='green')
				except :
					self.txt5 = tk.Label(self.root, text='Vrai !', fg='green')
					self.txt5.grid(row=4, column =2)
			else :
				rep = 'Faux, la réponse était : ' + correction + ' = ' + self.REPONSE
				try :
					self.txt5.config(text=rep, fg='red')
				except :
					self.txt5 = tk.Label(self.root, text=rep, fg='red')
					self.txt5.grid(row=4, column =2)
			self.nouveauKatakana()
			
		
	def change(self,text):
		try:
			self.fenetre(text)
			self.menu()
		except:
			print ("Unexpected error in change:", sys.exc_info())#[0])
			self.fenetre('accueil')
			self.menu()	
	
			
	def nettoyer_fenetre(self):	
		for c in self.root.winfo_children():
			c.destroy()
		info_serveur = threading.Thread( target = self.Send, args = (connection,"STOP")) #permet de débloquer le serveur en attente de la réponse du joueur
		info_serveur.start()
		info_serveur.join()
		
		
	def menu(self):
		#Creation du menu
		menubar = tk.Menu(self.root)

		menu0 = tk.Menu(menubar, tearoff=0)
		menu0.add_command(label="Page d'accueil", command=lambda text='accueil': self.change(text))
		menubar.add_cascade(label="Accueil", menu=menu0)

		menu1 = tk.Menu(menubar, tearoff=0)
		menu1.add_command(label="Exercice Hiragana", command=lambda text='japonais_hiragana': self.change(text))
		menu1.add_command(label="Entrainement Hiragana", command=lambda text='japonais_entrainement_hira': self.change(text))
		menu1.add_command(label="Jeu Hiragana", command=lambda text='japonais_jeu_hiragana': self.change(text))
		
		menu1.add_separator()
		menu1.add_command(label="Exercice Katakana", command=lambda text='japonais_katakana': self.change(text))
		menu1.add_command(label="Entrainement Katakana", command=lambda text='japonais_entrainement_kata': self.change(text))
		menu1.add_command(label="Jeu Katakana", command=lambda text='japonais_jeu_katakana': self.change(text))
		menubar.add_cascade(label="Japonais", menu=menu1)

		menu2 = tk.Menu(menubar, tearoff=0)
		menu2.add_command(label="Alphabet", command=lambda text='LDS_alphabet_cours': self.change(text))
		menu2.add_command(label="Signes", command=lambda text='exerciceLDS': self.change(text))
		menu2.add_separator()
		menu2.add_command(label="Entrainement", command=lambda text='entrainementLDS': self.change(text))
		menu2.add_command(label="Mini jeu", command=lambda text='LDS_jeu': self.change(text))
		menubar.add_cascade(label="Langue des signes", menu=menu2)

		menu3 = tk.Menu(menubar, tearoff=0)
		menu3.add_command(label="Aide", command=lambda text='aide': self.change(text))
		menubar.add_cascade(label="Aide", menu=menu3)
		
		self.root.config(menu=menubar)
		
		
	def __init__(self):
		#initialisation de l'interface graphique
		self.root=tk.Tk()
		self.root.title('Apprentissage de langues')
		self.root.geometry("800x500") #taille fixe
		
		#taille du texte pour les caractères
		self.bigFont = font.Font(family='Helvetica', size=20, weight='bold')
		
		#Variable recue par les recv
		self.REPONSE =  ""
		
		#initialisation de la fenêtre
		self.fenetre('accueil') #fenetre d'accueil
		self.menu()
		
		#création fenêtre
		self.root.mainloop()
		
		#destruction de la fenêtre
		self.root.destroy()
 

 
 
if __name__ == "__main__":
	connection = socket(AF_INET,SOCK_STREAM)
	connection.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

	host="localhost"
	port=8000
	connection.connect((host,port))
	print ("Connecte au serveur !")
	
	try :
		app=interface()
	except :
		print ("Unexpected error in main :", sys.exc_info()[0])
	finally :
		print("Fermeture de l'application, à bientôt !")	
		connection.send("DECONNECTION".encode()) 
