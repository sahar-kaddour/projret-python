class Code:
    def __init__(self):
        self.code=''
    def enregistrer_code(self):
        print("\n***enregistrement du code***")
        self.code=input("donner un code\t")
            
    def modifier_code(self):
        print("\n***modification du code*** ")
        self.code=input("inserer un nouveau code: \t")
        print ("\n le code sera \t",self.code)
   
    def isCorrect(self):
         print("\n***saisie du code***")
         test_code=input("\n saisie votre code\t")
         i=0
         state = False 
         while(i==0):
             if (test_code==self.code):
                 i=1
                 print("\nvrai")
                 state = True
             else:
                 test_code=input("\nfaut !! \nsaisie a nouveau votre code\t") 
                 state = False
         return state

    def retour_code(self):
        return(self.code)
from datetime import datetime
class Porte:
    def __init__(self):
        self.o=0
        self.f=-1
        print("initialisation: porte fermée\n")
        f_h1=open('f_h_o','w')
        f_h1.close()
        f_h2=open('f_h_f','w')
        f_h2.close()
    def ouverture (self):
       pin_du_porte=1
       print("porte ouvrée")
       self.o=self.o+1  
       f_h1=open('f_h_o','a')
       f_h1.write(str(datetime.now()))
       f_h1.write('\n')
       f_h1.close()
    def fermiture (self):
        pin_du_porte=0
        print("porte fermée")
        self.f=self.f+1
        f_h2=open('f_h_f','a')
        f_h2.write(str(datetime.now()))
        f_h2.write('\n')
        f_h2.close()
    def historique (self):       
        if(self.o!=0):
            f_h1=open('f_h_o','r')
            print("date d'ouverture :\t",f_h1.read())
            f_h1.close()
        if (self.f!=0):
            f_h2=open('f_h_f','r')
            print("date de fermiture :\t",f_h2.read())
            f_h2.close()
        print("nombre d'ouverture : \t",self.o)
        print("nombre de fermiture : \t",self.f)

c=Code()
c.enregistrer_code()
alea=int(input("\ntaper :\n1 si vous voulez modifier votre mot de passe\n else si non\t "))
if (alea==1):
    c.modifier_code()
p=Porte()
sortie=False
while(sortie==False):
    of=int(input("\ntaper\n1: ouvre la porte \n2: ferme la porte\n3: pour exiter: \t"))
    if (c.isCorrect()):
        if (of==1):
           p.ouverture()
        elif(of==2):
           p.fermiture()
        else:
            sortie=True
            

choix=int(input("\n1: modier le code\n2: historique du porte\t"))
if ( choix==1):
     c.modifier_code(str)
if (choix==2):
    print("\nl'historique du porte est :\t")
    print(p.historique())