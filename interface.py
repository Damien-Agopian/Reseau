import tkinter as tk

from PIL import Image
from PIL import ImageTk
from kana_py3 import *
from signes import *
import time
from socket import*
import threading



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
        self.connexion = conn           # réf. du socket de connexion
 
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
            self.bout1 = tk.Button(self.root, text="Valider", command=self.exerciceLDS)
            self.bout2 = tk.Button(self.root, text="Nouveau", command=self.nouveauSigne)
            self.txt1.grid(row =1, column=1, pady=50)
            self.txt2.grid(row =2, column=1)
            self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
            self.entr1.grid(row=2, column=2)
            self.bout1.grid(row=2, column=3)
            self.bout2.grid(row=1, column=3)
            print('Exercice de langue des signes')
        elif name == 'LDS_entrainement':
            self.txt1 = tk.Label(self.root, text ='Trouver la lettre correspondant au signe suivant :')
            self.txt2 = tk.Label(self.root, text='Votre réponse :')
            self.txt3 = tk.Label(self.root, text ='Si vous n\'y arrivez pas, référez-vous au cours. Bisous')
            self.caractere = tk.StringVar()
            self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
            self.bout1 = tk.Button(self.root, text="Commencer", command=self.jeuLDS)
            self.txt1.grid(row =1, column=1, pady=50)
            self.txt2.grid(row=2, column=1)
            self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
            self.entr1.grid(row=2, column=2)
            self.bout1.grid(row=2, column=3, padx =20)
            print('Jeu en solo de langue des signes')
        elif name=='japonnais_hiragana':
            self.txt1 = tk.Label(self.root, text ='Convertir le caractère romaji suivant :')
            self.txt2 = tk.Label(self.root, text='Votre réponse :')
            self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
            self.caractere = tk.StringVar()
            self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
            self.bout1 = tk.Button(self.root, text="Valider", command=self.jeuHiragana)
            #self.bout2 = tk.Button(self.root, text="Nouveau", command=self.nouveauHiragana)
            self.txt1.grid(row =1, column=1, pady=50)
            self.txt2.grid(row =2, column=1)
            self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
            self.entr1.grid(row=2, column=2)
            self.bout1.grid(row=2, column=3)
            #self.bout2.grid(row=1, column=3)
            print('Exercice 1 : convertir les romaji.')
            self.nouveauHiragana()
        elif name=='japonnais_katakana':
            self.txt1 = tk.Label(self.root, text ='Convertir le katakana suivant :')
            self.txt2 = tk.Label(self.root, text='Votre réponse :')
            self.txt3 = tk.Label(self.root, text ='Pour toute réclamation veuillez contacter le service après vente : damien.agopian@insa-lyon.fr')
            self.caractere = tk.StringVar()
            self.entr1 = tk.Entry(self.root, textvariable=self.caractere)
            self.bout1 = tk.Button(self.root, text="Valider", command=self.jeuKatakana)
            self.bout2 = tk.Button(self.root, text="Nouveau", command=self.nouveauKatakana)
            self.txt1.grid(row =1, column=1, pady=50)
            self.txt2.grid(row =2, column=1)
            self.txt3.grid(row = 5, column=1, columnspan=4, pady=50)
            self.entr1.grid(row=2, column=2)
            self.bout1.grid(row=2, column=3)
            self.bout2.grid(row=1, column=3)
            print('Exercice 2 : convertir les katakana.')	
        else :
            self.txt=tk.Text(self.root,bg='red')
            self.txt.insert("0.0",'Une erreur est survenue...')
            self.txt.grid(padx=1,pady=1)
            print('Erreur. Texte = ', name)
            
    
    def Send(self,connexion,msg):
        connexion.send(msg.encode())
    
    
    
    def Recv(self,connexion):
        print("entré thread")
        self.REPONSE = connexion.recv(1024).decode()
        print("sortie")
        
    
	
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
        #calcul du score
        if (self.caractere==self.lettre):
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
        self.lettre = choice(lettre_)
        self.signe = lettre_to_signe[self.lettre]
        self.can = tk.Canvas(self.root, width =360, height =440, bg ='white')
        image = Image.open(self.signe) 
        photo = ImageTk.PhotoImage(image) 
        lab = tk.Label(image=photo)
        lab.image = photo
        lab.grid(row=1, column=2)
        try :
            self.text5.config('')
        except :
            print('PROBLEME AVEC LE CHANGEMENT DE TXT')
			
    def exerciceLDS(self):
        self.caractere=self.entr1.get()
        if (self.caractere==self.lettre):
            try :
                self.txt5.config(text='Vrai !', fg='green')
            except :
                self.txt5 = tk.Label(self.root, text='Vrai !', fg='green')
                self.txt5.grid(row=4, column =2)
        else :
            rep = 'Faux, la réponse était : ' + self.lettre 
            try :
                self.txt5.config(text=rep, fg='red')
            except :
                self.txt5 = tk.Label(self.root, text=rep, fg='red')
                self.txt5.grid(row=4, column =2)
		
    def nouveauHiragana(self):
        #demande_serveur = ThreadSend(connection,"nouveauHiragana")
        demande_serveur = threading.Thread( target = self.Send, args = (connection,"nouveauHiragana"))
        demande_serveur.start()
        demande_serveur.join()
        print("Hello")
        #connection.send(demande_serveur) #demande d'un nouveau hiragana au serveur
        thread_recv = threading.Thread(target = self.Recv, args = (connection,)) #reception de l'hiragana
        thread_recv.start()
        thread_recv.join()
        print("done")
        self.txt4 = tk.Label(self.root, text = self.REPONSE)
        self.txt4.grid(row = 1, column=2)
		
    def jeuHiragana(self):
        reponse=self.entr1.get()
        print(reponse)
        #if reponse =
         #   reponse = "vide"
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
        demande_serveur = str(input("nouveauHiragana"))
        connection.send(demande_serveur) #demande d'un nouveau hiragana au serveur
        self.kata_encode = connection.recv(1024) #reception de l'hiragana
        self.txt4 = tk.Label(self.root, text = self.kata_encode)
        self.txt4.grid(row = 1, column=2)
		
    def jeuKatakana(self):
        reponse=self.entr1.get()
        reponse=self.entr1.get()
        connection.send(reponse)
        correction = connection.recv(1024)
        if (correction=='VRAI'):
            try :
                self.txt5.config(text='Vrai !', fg='green')
            except :
                self.txt5 = tk.Label(self.root, text='Vrai !', fg='green')
                self.txt5.grid(row=4, column =2)
        else :
            rep = 'Faux, la réponse était : ' + self.kata_encode + ' = ' + correction 
            try :
                self.txt5.config(text=rep, fg='red')
            except :
                self.txt5 = tk.Label(self.root, text=rep, fg='red')
                self.txt5.grid(row=4, column =2)
        self.nouveauKatakana()

		
    def change(self,text):
        self.fenetre(text)
        self.menu()
        """try:
            self.fenetre(text)
            self.menu()

        except:
            print('L\'appplication a renconté un erreur, nous vous redirigeons vers la page d\'accueil')
            self.fenetre('accueil')
            self.menu()	"""	
	
			
    def nettoyer_fenetre(self):		
        for c in self.root.winfo_children():
            c.destroy()
		
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
