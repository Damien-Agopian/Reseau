import tkinter as tk

from PIL import Image
from PIL import ImageTk
from dico import *
import time
from socket import*
import threading
import sys

"""
AMELIORATIONS : 
- regrouper les fonction jeuHira et jeuKata
- mettre des exceptions
- faire des commentaires propres
- faire les mini jeux
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
		elif name=='LDS_alphabet_exercice':
			self.txt1 = tk.Label(self.root, text ='Trouver la lettre correspondant au signe suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Si vous n\'y arrivez pas, référez-vous au cours. Bisous')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.jeuSigne)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 6, column=2, columnspan=4)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			self.txt22 = tk.Label(self.root, text='Veuillez répondre en lettres minuscules.')
			self.txt22.grid(row = 5, column=2, columnspan=4, pady=40)
			print('Exercice de langue des signes')
			self.nouveauSigne()
		elif name == 'LDS_entrainement':
			self.txt1 = tk.Label(self.root, text ='Trouver la lettre correspondant au signe suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt22 = tk.Label(self.root, text='Veuillez répondre en lettres minuscules.')
			self.txt3 = tk.Label(self.root, text ='Si vous n\'y arrivez pas, référez-vous au cours.')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeuLDS)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt22.grid(row = 4, column=2, columnspan=4, pady=40)
			self.txt2.grid(row=2, column=1)
			self.txt3.grid(row = 5, column=2, columnspan=4)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3, padx =20)
			print('Jeu en solo de langue des signes')
		elif name=='japonnais_hiragana':
			self.txt1 = tk.Label(self.root, text ='Convertir le hiragana suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.jeuHiragana)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			print('Exercice 1 : convertir les hiragana.')
			self.nouveauHiragana()
		elif name=='japonnais_katakana':
			self.txt1 = tk.Label(self.root, text ='Convertir le katakana suivant :')
			self.txt2 = tk.Label(self.root, text='Votre réponse :')
			self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
			self.caractere = tk.StringVar()
			self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
			self.bout1 = tk.Button(self.root, text="Valider", command=self.jeuKatakana)
			self.txt1.grid(row =1, column=1, pady=50)
			self.txt2.grid(row =2, column=1)
			self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
			self.entr1.grid(row=2, column=2)
			self.bout1.grid(row=2, column=3)
			print('Exercice 2 : convertir les katakana.')	
			self.nouveauKatakana()
		else :
			self.txt=tk.Text(self.root,bg='red')
			self.txt.insert("0.0",'Cette page n\'existe pas encore. Merci de votre compréhension.')
			self.txt.grid(padx=1,pady=1)
			print('Page non codée. Nom = ', name)
			
	
	def Send(self,connexion,msg):
		connexion.send(msg.encode())
	

	def Recv(self,connexion):
		self.REPONSE = connexion.recv(1024).decode()	
	
	
	def jeuLDS(self):
		#printer l'interface
		#on a 30 sec pour entrer des réponses
		vrai = 0 #juste, faux
		faux = 0
		self.nouveauSigne()
		endTime = time.time() + 10 #le jeu dure 10 secondes
		self.entr1.event_add('<<Return>>', '<KeyPress - Return>')
		self.entr1.bind('<<Return>>', self.g)
		"""while(time.time() < endTime):
			#self.debut = False
			if(self.entr1.bind('<<Return>>', self.g)): #entrée => on change de signe
				self.nouveauSigneJeu() 
				self.debut = False
				if self.debut==True :
					self.caractere=self.entr1.get()
					#calcul du score
					if (self.caractere==self.lettre):
						vrai += 1
					else :
						faux += 1
			time.sleep(1) #en secondes
		print('Fin du temps')"""
	   
		
	def g(self, event):
		self.nouveauSigneJeu()
		if (self.caractere==self.lettre): #calcul du score
			vrai += 1
		else :
			faux += 1
		print('Score = ', vrai, "/", vrai+faux)
		self.entr1.config('')   
		#self.debut = True
		
	def nouveauSigneJeu(self):
		self.lettre = choice(lettre_)
		self.signe = lettre_to_signe[self.lettre]
		self.can = tk.Canvas(self.root, width =360, height =440, bg ='white')
		image = Image.open(self.signe) 
		photo = ImageTk.PhotoImage(image) 
		lab = tk.Label(image=photo)
		lab.image = photo
		lab.grid(row=1, column=2)
		self.entr1.config('')

				
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
			print ("Unexpected error:", sys.exc_info()[0])
		nomImage = self.REPONSE
		image = Image.open(nomImage) 
		photo = ImageTk.PhotoImage(image) 
		self.lab = tk.Label(image=photo)
		self.lab.image = photo
		self.lab.grid(row=1, column=2)
		
		
	def jeuSigne(self):
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
		
	def nouveauHiragana(self):
		demande_serveur = threading.Thread( target = self.Send, args = (connection,"nouveauHiragana"))
		demande_serveur.start()
		demande_serveur.join()
		print("Hello")
		thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'hiragana
		thread_recv.start()
		thread_recv.join()
		print("done")
		self.txt4 = tk.Label(self.root, text = self.REPONSE)
		self.txt4.grid(row = 1, column=2)
		
	def jeuHiragana(self):
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
		
	def nouveauKatakana(self):
		demande_serveur = threading.Thread( target = self.Send, args = (connection,"nouveauKatakana"))
		demande_serveur.start()
		demande_serveur.join()
		print("Fonction nvx kata")
		thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'hiragana
		thread_recv.start()
		thread_recv.join()
		print("Nvx Kata recu")
		self.txt4 = tk.Label(self.root, text = self.REPONSE)
		self.txt4.grid(row = 1, column=2)
		
		
	def jeuKatakana(self):
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
			print ("Unexpected error:", sys.exc_info()[0])
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
		menu1.add_command(label="Exercice 1 : Hiragana", command=lambda text='japonnais_hiragana': self.change(text))
		menu1.add_command(label="Exercice 2 : Katakana", command=lambda text='japonnais_katakana': self.change(text))
		menu1.add_separator()
		menu1.add_command(label="Mini jeu", command=lambda text='japonnais_jeu': self.change(text))
		menubar.add_cascade(label="Japonnais", menu=menu1)

		menu2 = tk.Menu(menubar, tearoff=0)
		menu2.add_command(label="Alphabet", command=lambda text='LDS_alphabet_cours': self.change(text))
		menu2.add_command(label="Signes", command=lambda text='LDS_alphabet_exercice': self.change(text))
		menu2.add_separator()
		menu2.add_command(label="Entrainement", command=lambda text='LDS_entrainement': self.change(text))
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
	app=interface()
