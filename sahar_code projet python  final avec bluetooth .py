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
         while(i==0):
             if (test_code==self.code):
                 i=1
                 print("\nvrai")
             else:
                 test_code=input("\nfaut !! \nsaisie a nouveau votre code\t") 
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
import bluez
class Act_bluetooth():
    def __init__(self):
        target_name=None
        target_adress=None

    def connecte(self,code):
        target_name="the door"
        nearby_devices=bluez.discover_devices()
        for x in nearby_devices:
            if target_name==bluez.lookup_name(x):
                target_adress=x
            break
        if target_adress is not None :
            print("found target bluetooth device with adress",target_adress)
            res=True
        else:
            print("could not find target bleutooth device")
            res=False
        return(res)
    def saisir_code():
        print("entrer votre code")
    def envoit_cle(self):
        sock=bluez.BluetoothSocket( bluez.RFCOMM )
        port=12
        device_adr=self.target_adress
        sock.connect((device_adr, port))
        sock.send(Code.retour_code)
        sock.close()
c=Code()
cpb=Act_bluetooth()
c.enregistrer_code()
presence_porte=cpb.connecte(str) #return true si il trouve mon appareil  / faux si non
if(presence_porte):
    cpb.envoit_cle # premier code envoyer
alea=int(input("\ntaper :\n1 si vous voulez modifier votre mot de passe\n else si non\t "))
if (alea==1):
    c.modifier_code()
    cpb.envoit_cle #envoyer le code modifier
p=Porte()
sortie=0
while(sortie==0):
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
     cpb.envoit_cle
if (choix==2):
    print("\nl'historique du porte est :\t")
    print(p.historique())
