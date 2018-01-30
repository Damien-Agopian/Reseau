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
- faire les entrainements : affichage de la correction précédente et du nvx caractère : les deux sont reçus en même temps? 

"""

class interface:
	
	#=============================================================#
	#         Initialisation de l'interface graphique             #
	#=============================================================#
	
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
	
	
	#=============================================================#
	#              Gestion de la fenetre graphique                #
	#=============================================================#
		
	def change(self,text):
		try: #changement de fenetre quand on appuie sur un bouton du menu
			self.fenetre(text)
			self.menu()
		except: #redirige vers la page d'accueil en cas d'erreur
			print ("Unexpected error in change:", sys.exc_info())
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
		#Page d'accueil
		menu0 = tk.Menu(menubar, tearoff=0)
		menu0.add_command(label="Page d'accueil", command=lambda text='accueil': self.change(text))
		menubar.add_cascade(label="Accueil", menu=menu0)
		#Japonais : entrainement, jeu en solo et jeu en multi joueur pour les alphabets hiragana et katakana
		menu1 = tk.Menu(menubar, tearoff=0)
		menu1.add_command(label="Exercice Hiragana", command=lambda text='japonais_hiragana': self.change(text))
		menu1.add_command(label="Entrainement Hiragana", command=lambda text='japonais_entrainement_hira': self.change(text))
		menu1.add_command(label="Jeu Hiragana", command=lambda text='japonais_jeu_hiragana': self.change(text))
		menu1.add_separator()
		menu1.add_command(label="Exercice Katakana", command=lambda text='japonais_katakana': self.change(text))
		menu1.add_command(label="Entrainement Katakana", command=lambda text='japonais_entrainement_kata': self.change(text))
		menu1.add_command(label="Jeu Katakana", command=lambda text='japonais_jeu_katakana': self.change(text))
		menubar.add_cascade(label="Japonais", menu=menu1)
		#Langue Signes : alphabet, entrainement, jeu en solo et jeu en multi joueur 
		menu2 = tk.Menu(menubar, tearoff=0)
		menu2.add_command(label="Alphabet", command=lambda text='LDS_alphabet_cours': self.change(text))
		menu2.add_command(label="Signes", command=lambda text='exercice_LDS': self.change(text))
		menu2.add_separator()
		menu2.add_command(label="Entrainement", command=lambda text='jeu_solo_LDS': self.change(text))
		menu2.add_command(label="Mini jeu", command=lambda text='LDS_jeu': self.change(text))
		menubar.add_cascade(label="Langue des signes", menu=menu2)
		#Aide
		menu3 = tk.Menu(menubar, tearoff=0)
		menu3.add_command(label="Aide", command=lambda text='aide': self.change(text))
		menubar.add_cascade(label="Aide", menu=menu3)
		#Ajoute le menu à notre fenêtre
		self.root.config(menu=menubar)

	def fenetre(self,name):
		"""
		Cette fonction permet de créer les objets tk qui seront nécessaire pour les différentes fenêtres.
		Pour l'accueil, l'aide et le cours LDS on n'affiche qu'une image et du texte.
		Pour les exercice et les jeu, il faut des boutons de validation, des entrée texte,...
		Les boutons sont reliés à des fonctions de validation (test si la réponse entrée est correcte)
		ou des fonctions de jeu
		"""
		self.nettoyer_fenetre() #enlève tous les objets tk
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
		elif name=='exercice_LDS':
			self.txt1 = tk.Label(self.root, text ='Trouver la lettre correspondant au signe suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Si vous n\'y arrivez pas, référez-vous au cours. Bisous')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.exercice_LDS)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 6, column=2, columnspan=4)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			self.txt22 = tk.Label(self.root, text='Veuillez répondre en lettres minuscules.')
			self.txt22.grid(row = 5, column=2, columnspan=4, pady=40)
			print('Exercice de langue des signes')
			self.nouveau_signe()
		elif name == 'jeu_solo_LDS':
			self.txt1 = tk.Label(self.root, text ='Trouver la lettre correspondant au signe suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt22 = tk.Label(self.root, text='Veuillez répondre en lettres minuscules.')
			self.txt3 = tk.Label(self.root, text ='Tapez sur \'Entrée\' pour valider votre réponse.')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeu_solo_LDS)
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
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeu_solo_hira)
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
			self.bout1 = tk.Button(self.root, text="Valider", command=self.jeu_multi_hira)
			self.txt1.grid(row =1, column=1, pady=50)
			self.entr1.grid(row=1, column=2)
			self.bout1.grid(row=1, column=3)
			print('Mini jeu en ligne hiragana : Soyez meilleur que les autres joueurs !')
		elif name=='japonais_jeu_katakana':
			self.txt1 = tk.Label(self.root, text ='Votre pseudo :')
			self.pseudo = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.pseudo)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.jeu_multi_kata)
			self.txt1.grid(row =1, column=1, pady=50)
			self.entr1.grid(row=1, column=2)
			self.bout1.grid(row=1, column=3)
			print('Mini jeu en ligne katakana : Soyez meilleur que les autres joueurs !')
		elif name=='LDS_jeu':
			self.txt1 = tk.Label(self.root, text ='Votre pseudo :')
			self.pseudo = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.pseudo)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.jeu_multi_LDS)
			self.txt1.grid(row =1, column=1, pady=50)
			self.entr1.grid(row=1, column=2)
			self.bout1.grid(row=1, column=3)
			print('Mini jeu en ligne LDS : Soyez meilleur que les autres joueurs !')
		elif name=='japonais_entrainement_kata':
			self.txt1 = tk.Label(self.root, text ='Convertir le katakana suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeu_solo_kata)
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
			self.bout1 = tk.Button(self.root, text="Valider", command=self.exercice_hira)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			print('Exercice 1 : convertir les hiragana.')
			self.nouveau_hira()
		elif name=='japonais_katakana':
			self.txt1 = tk.Label(self.root, text ='Convertir le katakana suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.exercice_kata)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			print('Exercice 2 : convertir les katakana.')	
			self.nouveau_kata()
		else :
			print('Cette page n\'existe pas encore. Merci de votre compréhension. Vous allez être redirigé vers la page d\'acceuil')
			self.change('accueil')
			
	#=============================================================#
	#          Communication avec le serveur                      #
	#=============================================================#
	
	def Send(self,connexion,msg):
		connexion.send(msg.encode())
	

	def Recv(self,connexion):
		self.REPONSE = connexion.recv(1024).decode()	
	
	#=============================================================#
	#                     LDS                                     #
	#=============================================================#
	
	def nouveau_signe(self):
		#Prévient le serveur qu'il faut envoyer un nouveau signe
		demande_serveur = threading.Thread( target = self.Send, args = (connection,"nouveauSigne"))
		demande_serveur.start()
		demande_serveur.join()
		print("Nouveau Signe")
		#Réception du nouveau signe (reçoit le nom du ficher stocké en local qui correspond à l'image du signe)
		thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception du nom du ficher qui contient l'image du signe
		thread_recv.start()
		thread_recv.join()
		print("Nouveau signe recu")
		try :
			self.lab.image = None #supprime l'ancienne image
		except :
			print ("Unexpected error in nouveau_signe():", sys.exc_info()[0])
		nomImage = self.REPONSE
		image = Image.open(nomImage) 
		photo = ImageTk.PhotoImage(image) 
		self.lab = tk.Label(image=photo)
		self.lab.image = photo
		self.lab.grid(row=1, column=2)
		
	def exercice_LDS(self):
		reponse=self.entr1.get() #réponse entrée par l'utilisateur
		if len(reponse) != 0: #si on a vraiment entré une réponse
			#envoi au serveur de la réponse de l'utilisateur
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			#réception de la correction
			correction = self.REPONSE #Stock la dernière valeur de REPONSE
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			#traitement de la correction
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
			self.nouveau_signe() #demande au serveur et affichage du nouvau signe
	
	def nouveau_signe_jeu(self, event):
		reponse = self.entr1.get() #réponse de l'utilisateur
		if len(reponse) != 0 and time.time()<self.endTime : #si le client a répondu et que le temps n'est pas écoulé
			#Demande de correction au serveur
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			#Réception de la correction
			correction = self.REPONSE #Stock la le nom du fichier envoyé par le serveur
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			#Incrémentation des réponses 
			if (self.REPONSE=='VRAI'):
				self.vrai += 1
			else :
				self.faux += 1
			print ("vrai : ", self.vrai, "      faux : ", self.faux) #affichage du score au fur et à mesure
			self.nouveau_signe() #demande au serveur et affichage du nouvau signe
		elif time.time() >= self.endTime : #Si le temps est écoulé
			print('Fin du temps')
			self.txt33 = tk.Label(self.root, text ="Fin du temps !", fg='red')
			self.txt33.grid(row =4, column=2, pady=10)
			info_serveur = threading.Thread( target = self.Send, args = (connection,"STOP")) #permet de débloquer le serveur en attente de la réponse du joueur
			info_serveur.start()
			info_serveur.join()
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeu_solo_LDS) #On remet le bouton qui permet de débuter le jeu
			self.bout1.grid(row=2, column=3)
			"""thread_correction = threading.Thread(target = self.Recv, args = (connection,)) #stockage inutile de la correction que le serveur envoie même si on a fini le jeu
			thread_correction.start() 
			thread_correction.join()"""
			if self.jeu == 'multi' :
				print ('fin du temps jeu multi')
				try :
					score = self.vrai #envoie du score
					demande_serveur = threading.Thread(target = self.Send, args = (connection,'score')) 
					demande_serveur.start()
					demande_serveur.join()
					demande_serveur = threading.Thread(target = self.Send, args = (connection,str(score)))
					demande_serveur.start()
					demande_serveur.join()
					print('score envoyé')
				except :
					print ("Erreur dans l'envoi du score:", sys.exc_info())
				try :
					thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #réception du résultat
					thread_recv.start()
					thread_recv.join()
					print('réception du classement')
					print('résultat : ', self.REPONSE)
				except :
					print ("Erreur dans la réception du classement:", sys.exc_info())
				for c in self.root.winfo_children(): #nettoie la fenetre
					c.destroy()
				self.menu()
				if self.REPONSE == 'Winner': #traiement du résultat
					self.txt3 = tk.Label(self.root, text ="Gagné !", fg='green')
					self.txt3.grid(row=1, column=1)
				else :
					self.txt3 = tk.Label(text ="Perdu...", fg='red', )
					self.txt3.grid(row=1, column=1)
				self.jeu = 'solo'
		"""txt = "Score : " + str(self.vrai) + "/" + str(self.vrai+self.faux) #Affichage du score final
		self.txt3 = tk.Label(self.root, text =txt)
		self.txt3.grid(row =3, column=2, pady=10)"""

		
	def jeu_solo_LDS(self):
		#supprimer les réponses précédentes
		self.bout1.destroy()
		try : 
			self.txt3.delete(0.0, tk.END)
			self.txt33.delete(0.0, tk.END)
		except :
			print("Premier jeu : pas de réponses à effacer.")
		self.vrai = 0 #nombre de réponses justes/fausses
		self.faux = 0
		self.nouveau_signe() #demande au serveur et affichage du nouvau signe
		self.endTime = time.time() + 10 #le jeu dure 10 secondes
		self.entr1.event_add('<<Return>>', '<KeyPress - Return>') #corrige la réponse quand on appuie sur 'entrée'
		self.entr1.bind('<<Return>>', self.nouveau_signe_jeu)
		
	def jeu_multi_LDS(self):
		"""
		Mini jeu à deux joueurs
		Le serveur attend d'avoir deux clients qui se connectent pour leur donner le top départ.
		Les deux joueurs ont 10 sec pour traduire un maximum de signes
		A la fin du temps chaque joueur envoie son score (nombre de bonnes réponses)
		Le serveur envoie le résultat ('gagant' ou 'perdant')
		"""
		self.jeu = 'multi'
		#Prévient le serveur qu'on va jouer en ligne au jeu hiragana
		demande_serveur = threading.Thread(target = self.Send, args = (connection,'multi_LDS'))
		demande_serveur.start()
		demande_serveur.join()
		#envoi du pseudo
		self.pseudo = self.entr1.get()
		if len(self.pseudo)!=0 : #Si le pseudo a été renseigné
			demande_serveur = threading.Thread(target = self.Send, args = (connection,self.pseudo))
			demande_serveur.start()
			demande_serveur.join()
			print("Pseudo envoyé")
			thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'ordre (attendre ou commencer)
			thread_recv.start()
			thread_recv.join()
			if self.REPONSE == 'commencer': #si il y avait déjà un advairsaire 
				print('Commencer le jeu')
				self.jeu_multi_LDS_interface()
			elif self.REPONSE == 'attendre': #on doit attendre l'arrivée d'un adversaire
				print('Attente de joueur')
				for c in self.root.winfo_children(): #nettoie la fenetre
					c.destroy()
				self.txt1 = tk.Label(self.root, text ='En attente d\'un adversaire...')
				self.txt1.grid(row =1, column=1, pady=50)
				self.menu()
				thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'ordre (attendre ou commencer)
				thread_recv.start()
				thread_recv.join()
				if self.REPONSE == 'commencer': #si un nouvel adversaire se connecte
					print('Commencer le jeu')
					self.jeu_multi_LDS_interface()
			elif self.REPONSE =='serveur_plein': #si il y a déjà deux adversaire qui attendent dans la liste du serveur (et jouent)
				for c in self.root.winfo_children(): #nettoie la fenetre
					c.destroy()
				self.menu()
				self.txt1 = tk.Label(self.root, text ='Le serveur est occupé, veuillez réessayer plus tard.')
				self.txt1.grid(row =1, column=1, pady=50)
			else :
				print('Erreur lors de la réception de l\'ordre')
				
	def jeu_multi_LDS_interface(self):
		for c in self.root.winfo_children(): #nettoie la fenetre
			c.destroy()
		self.menu()
		self.txt1 = tk.Label(self.root, text ='Convertir le signe suivant :') #inerface initiale
		self.txt2 = tk.Label(self.root, text='Votre réponse :')
		self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
		self.caractere = tk.StringVar()
		self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
		self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeu_solo_LDS)
		self.txt1.grid(row =1, column=1, pady=50)
		self.txt2.grid(row =2, column=1)
		self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
		self.entr1.grid(row=2, column=2)
		self.bout1.grid(row=2, column=3)
		self.jeu_solo_LDS() #utilisation de la même fonction que le jeux en solitaire
		print('time.time() = ', time.time())
		print('timeEnd = ', self.endTime)


		
	#=============================================================#
	#                    Hiragana                                 #
	#=============================================================#
	
	def nouveau_hira(self):
		#Demande d'un nouveau hiragana au serveur
		demande_serveur = threading.Thread( target = self.Send, args = (connection,"nouveauHiragana"))
		demande_serveur.start()
		demande_serveur.join()
		#Réception du hiragana (encodé)
		thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'hiragana
		thread_recv.start()
		thread_recv.join()
		#Affichage du caractère
		self.txt4 = tk.Label(self.root, text = self.REPONSE,  font=self.bigFont)
		self.txt4.grid(row = 1, column=2)
		
	def exercice_hira(self):
		reponse=self.entr1.get() #réponse de l'utilisateur
		if len(reponse) != 0: #si on a entré une réponse
			#Envoi de la réponse de l'utilisateur au serveur
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			#Réception de la correction
			correction = self.REPONSE #Stock la dernière valeur de REPONSE
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'): #traitement de la correction
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
			self.nouveau_hira() #demande au serveur et affichage du nouvau hiragana
	
	def jeu_solo_hira(self):
		self.bout1.destroy() #enlève le bouton 'Commencer'
		#supprimer les réponses précédentes
		try : 
			self.txt3.delete(0.0, tk.END)
			self.txt33.delete(0.0, tk.END)
			self.txt4.delete(0.0, tk.END)
		except :
			print("Premier jeu : pas de réponses à effacer.")
			print ("Unexpected error in jeu_solo_hira():", sys.exc_info()) 
		self.vrai = 0 #nombre de réponses justes/fausses
		self.faux = 0
		self.nouveau_hira() #demande au serveur et affichage du nouvau hiragana
		self.endTime = time.time() + 10 #le jeu dure 10 secondes
		self.entr1.event_add('<<Return>>', '<KeyPress - Return>') #Correction qaund on appuie sur 'entrée'
		self.entr1.bind('<<Return>>', self.nouveau_hira_jeu)

	def nouveau_hira_jeu(self, event):
		reponse = self.entr1.get() #Réponse de l'utilisateur
		#Demande de correction au serveur
		if len(reponse) != 0 and time.time()<self.endTime : #si l'utilisateur a vraiment entré une réponse
			#Envoie de la réponse de l'utilisateur
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			correction = self.REPONSE #Correction
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'):  #Traitement de la correction
				self.vrai += 1
			else :
				self.faux += 1
			print ("vrai : ", self.vrai, "      faux : ", self.faux)
			self.nouveau_hira() #demande au serveur et affichage du nouvau hiragana			
		elif time.time() >= self.endTime : #Si le temps est fini
			print('Fin du temps')
			self.txt33 = tk.Label(self.root, text ="Fin du temps !", fg='red')
			self.txt33.grid(row =4, column=2, pady=10)
			info_serveur = threading.Thread( target = self.Send, args = (connection,"TEMPS_ECOULE")) #permet de débloquer le serveur en attente de la réponse du joueur
			info_serveur.start()
			info_serveur.join()
			self.REPONSE = None
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeu_solo_hira) #On remet le bouton 'Commencer'
			self.bout1.grid(row=2, column=3)
			thread_correction = threading.Thread(target = self.Recv, args = (connection,)) #stockage inutile de la correction que le serveur envoie même si on a fini le jeu
			thread_correction.start()
			thread_correction.join()			
		txt = "Score : " + str(self.vrai) + "/" + str(self.vrai+self.faux) #affichage du score
		self.txt3 = tk.Label(self.root, text =txt)
		self.txt3.grid(row =3, column=2, pady=10)

	def jeu_multi_hira(self):
		"""
		Mini jeu à deux joueurs
		Le serveur attend d'avoir deux clients qui se connectent pour leur donner le top départ.
		Les deux joueurs ont 10 sec pour traduire un maximum de hiragana
		A la fin du temps chaque joueur envoie son score (nombre de bonnes réponses)
		Le serveur envoie le résultat ('gagant' ou 'perdant')
		"""
		#Prévient le serveur qu'on va jouer en ligne au jeu hiragana
		demande_serveur = threading.Thread(target = self.Send, args = (connection,'multi_hira'))
		demande_serveur.start()
		demande_serveur.join()
		#envoi du pseudo
		self.pseudo = self.entr1.get()
		if len(self.pseudo)!=0 : #Si le pseudo a été renseigné
			demande_serveur = threading.Thread(target = self.Send, args = (connection,self.pseudo))
			demande_serveur.start()
			demande_serveur.join()
			print("Pseudo envoyé")
			thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'ordre (attendre ou commencer)
			thread_recv.start()
			thread_recv.join()
			if self.REPONSE == 'commencer': #si il y avait déjà un advairsaire 
				print('Commencer le jeu')
				self.jeu_multi_hira_interface()
			elif self.REPONSE == 'attendre': #on doit attendre l'arrivée d'un adversaire
				print('Attente de joueur')
				for c in self.root.winfo_children(): #nettoie la fenetre
					c.destroy()
				print('fenêtre nettoyée')
				self.txt1 = tk.Label(self.root, text ='En attente d\'un adversaire...')
				self.txt1.grid(row =1, column=1, pady=50)
				self.menu()
				print('texte affiché')
				time.sleep(10)
				print('attente pour permettre l\'affichage du message')
				"""IL N'AFFICHE PAS AVANT D'ATTENDRE LA REPONSE DU SERVEUR..."""
				thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'ordre (attendre ou commencer)
				thread_recv.start()
				thread_recv.join()
				if self.REPONSE == 'commencer': #si un nouvel adversaire se connecte
					print('Commencer le jeu')
					self.jeu_multi_hira_interface()
			elif self.REPONSE =='serveur_plein': #si il y a déjà deux adversaire qui attendent dans la liste du serveur (et jouent)
				for c in self.root.winfo_children(): #nettoie la fenetre
					c.destroy()
				self.menu()
				self.txt1 = tk.Label(self.root, text ='Le serveur est occupé, veuillez réessayer plus tard.')
				self.txt1.grid(row =1, column=1, pady=50)
				
	def jeu_multi_hira_interface(self):
		for c in self.root.winfo_children(): #nettoie la fenetre
			c.destroy()
		self.menu()
		self.txt1 = tk.Label(self.root, text ='Convertir le hiragana suivant :') #inerface initiale
		self.txt2 = tk.Label(self.root, text='Votre réponse :')
		self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
		self.caractere = tk.StringVar()
		self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
		self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeu_solo_hira)
		self.txt1.grid(row =1, column=1, pady=50)
		self.txt2.grid(row =2, column=1)
		self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
		self.entr1.grid(row=2, column=2)
		self.bout1.grid(row=2, column=3)
		self.jeu_solo_hira() #utilisation de la même fonction que le jeux en solitaire
		if time.time() > self.endTime : #à la fin du temps
			score = self.vrai #envoie du score
			demande_serveur = threading.Thread(target = self.Send, args = (connection,'score')) 
			demande_serveur.start()
			demande_serveur.join()
			demande_serveur = threading.Thread(target = self.Send, args = (connection,str(score)))
			demande_serveur.start()
			demande_serveur.join()
			thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #réception du résultat
			thread_recv.start()
			thread_recv.join()
			if self.REPONSE == 'Winner': #traiement du résultat
				self.txt3.config(text ="Gagné !", fg='green')
			else :
				self.txt3.config(text ="Perdu...", fg='red')
				
				
	#=============================================================#
	#                     Katakana                                #
	#=============================================================#
	
	
	def nouveau_kata(self):
		demande_serveur = threading.Thread( target = self.Send, args = (connection,"nouveauKatakana")) #demande au serveur d'un nouveau katakana
		demande_serveur.start()
		demande_serveur.join()
		thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception du katakana
		thread_recv.start()
		thread_recv.join()
		self.txt4 = tk.Label(self.root, text = self.REPONSE,  font=self.bigFont) #affichage du katakana à traduire
		self.txt4.grid(row = 1, column=2)
		
		
	def exercice_kata(self):
		reponse=self.entr1.get()
		if len(reponse) != 0: #si on a entré une réponse
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse)) #envoie de la réponse au serveur pour qu'il la corrige
			thread_reponse.start()
			thread_reponse.join()
			correction = self.REPONSE #Stock la dernière valeur de REPONSE
			thread_correction = threading.Thread(target = self.Recv, args = (connection,)) #réception de la correction
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'): #traitement graphique de la correction
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
			self.nouveau_kata() #demande d'un nouveau katakana pour continuer l'entrainement
	
	def jeu_solo_kata(self):
		self.bout1.destroy()
		try : #supprimer les réponses précédentes
			self.txt3.delete(0.0, tk.END)
			self.txt33.delete(0.0, tk.END)
		except :
			print("Premier jeu : pas de réponses à effacer.")
		self.vrai = 0 #nombre de réponses justes/fausses
		self.faux = 0
		self.nouveau_kata() #printer l'interface
		self.endTime = time.time() + 10 #le jeu dure 10 secondes
		self.entr1.event_add('<<Return>>', '<KeyPress - Return>') #vérifie la réponse quand on tape sur 'entrée'
		self.entr1.bind('<<Return>>', self.nouveau_kata_jeu)
	
	def nouveau_kata_jeu(self, event):
		reponse = self.entr1.get()
		#Demande de correction au serveur
		if len(reponse) != 0 and time.time()<self.endTime : #self.repondre==True:
			thread_reponse=threading.Thread(target = self.Send, args = (connection,reponse))
			thread_reponse.start()
			thread_reponse.join()
			correction = self.REPONSE #Stock la caractère katakana (à traduire) envoyé par le serveur
			thread_correction = threading.Thread(target = self.Recv, args = (connection,))
			thread_correction.start()
			thread_correction.join()
			if (self.REPONSE=='VRAI'):
				self.vrai += 1
			else :
				self.faux += 1
			print ("vrai : ", self.vrai, "      faux : ", self.faux)
			self.nouveau_kata() 
		else :
			print('Fin du temps')
			self.txt33 = tk.Label(self.root, text ="Fin du temps !", fg='red')
			self.txt33.grid(row =4, column=2, pady=10)
			info_serveur = threading.Thread( target = self.Send, args = (connection,"STOP")) #permet de débloquer le serveur en attente de la réponse du joueur
			info_serveur.start()
			info_serveur.join()
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeu_solo_kata) #remet le bouton 'commencer'
			self.bout1.grid(row=2, column=3)
			thread_correction = threading.Thread(target = self.Recv, args = (connection,)) #stockage inutile de la correction que le serveur envoie même si on a fini le jeu
			thread_correction.start()
			thread_correction.join()			
		txt = "Score : " + str(self.vrai) + "/" + str(self.vrai+self.faux) #affichage du score
		self.txt3 = tk.Label(self.root, text =txt)
		self.txt3.grid(row =3, column=2, pady=10)
		
		
	def jeu_multi_kata(self):
		"""
		Mini jeu à deux joueurs
		Le serveur attend d'avoir deux clients qui se connectent pour leur donner le top départ.
		Les deux joueurs ont 10 sec pour traduire un maximum de hiragana
		A la fin du temps chaque joueur envoie son score (nombre de bonnes réponses)
		Le serveur envoie le résultat ('gagant' ou 'perdant')
		"""
		#Prévient le serveur qu'on va jouer en ligne au jeu hiragana
		demande_serveur = threading.Thread(target = self.Send, args = (connection,'multi_kata'))
		demande_serveur.start()
		demande_serveur.join()
		#envoi du pseudo
		self.pseudo = self.entr1.get()
		if len(self.pseudo)!=0 : #Si le pseudo a été renseigné
			demande_serveur = threading.Thread(target = self.Send, args = (connection,self.pseudo))
			demande_serveur.start()
			demande_serveur.join()
			print("Pseudo envoyé")
			thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'ordre (attendre ou commencer)
			thread_recv.start()
			thread_recv.join()
			if self.REPONSE == 'commencer': #si il y avait déjà un advairsaire 
				print('Commencer le jeu')
				self.jeu_multi_kata_interface()
			elif self.REPONSE == 'attendre': #on doit attendre l'arrivée d'un adversaire
				print('Attente de joueur')
				for c in self.root.winfo_children(): #nettoie la fenetre
					c.destroy()
				self.txt1 = tk.Label(self.root, text ='En attente d\'un adversaire...')
				self.txt1.grid(row =1, column=1, pady=50)
				self.menu()
				thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'ordre (attendre ou commencer)
				thread_recv.start()
				thread_recv.join()
				if self.REPONSE == 'commencer': #si un nouvel adversaire se connecte
					print('Commencer le jeu')
					self.jeu_multi_kata_interface()
			elif self.REPONSE =='serveur_plein': #si il y a déjà deux adversaire qui attendent dans la liste du serveur (et jouent)
				for c in self.root.winfo_children(): #nettoie la fenetre
					c.destroy()
				self.menu()
				self.txt1 = tk.Label(self.root, text ='Le serveur est occupé, veuillez réessayer plus tard.')
				self.txt1.grid(row =1, column=1, pady=50)
				
	def jeu_multi_kata_interface(self):
		for c in self.root.winfo_children(): #nettoie la fenetre
			c.destroy()
		self.menu()
		self.txt1 = tk.Label(self.root, text ='Convertir le katakana suivant :') #inerface initiale
		self.txt2 = tk.Label(self.root, text='Votre réponse :')
		self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
		self.caractere = tk.StringVar()
		self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
		self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeu_solo_kata)
		self.txt1.grid(row =1, column=1, pady=50)
		self.txt2.grid(row =2, column=1)
		self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
		self.entr1.grid(row=2, column=2)
		self.bout1.grid(row=2, column=3)
		self.jeu_solo_kata() #utilisation de la même fonction que le jeux en solitaire
		if time.time() > self.endTime : #à la fin du temps
			score = self.vrai #envoie du score
			demande_serveur = threading.Thread(target = self.Send, args = (connection,'score')) 
			demande_serveur.start()
			demande_serveur.join()
			demande_serveur = threading.Thread(target = self.Send, args = (connection,str(score)))
			demande_serveur.start()
			demande_serveur.join()
			thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #réception du résultat
			thread_recv.start()
			thread_recv.join()
			if self.REPONSE == 'Winner': #traiement du résultat
				self.txt33.config(text ="Gagné !", fg='green')
			else :
				self.txt33.config(text ="Perdu...", fg='red')
			

 

#=============================================================#
#                         Main                                #
#=============================================================#
	
 
if __name__ == "__main__":
	#création du socket
	connection = socket(AF_INET,SOCK_STREAM)
	connection.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	try :
		host = sys.argv[1]
		port = int(sys.argv[2])
	except :
		host = "localhost"
		port = 8000
	#connection au serveur
	connection.connect((host,port))
	print ("Connecte au serveur !")
	try : #lancement de l'application
		app=interface()
	except : #affichage des erreurs
		print ("Unexpected error in main :", sys.exc_info()[0])
	finally :  #déconnection 
		print("Fermeture de l'application, à bientôt !")	
		connection.send("DECONNECTION".encode()) 
		connection.shutdown(1)
		connection.close()
