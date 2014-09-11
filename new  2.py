import random

# En klass som beskriver en attraktion.
# Attribut:
#    namn - 
#    minlaengd - minsta längden som krävs för att åka 
#    antal passagerare 
#    magpirrfaktor
#    starta - 0/1, där 1 är den igång
#    haveri - 0 om den har havererat
#    ljud - ljud från attraktionen
class Attraktion:

    # Konstruktorn, initierar attributen namn, minlängd,
    # antal passagerare och magpirrfaktor
    def __init__(self, attraktionsnamn, minlaengd, pirr,  antal =1,ljud=""):
        self.namn = attraktionsnamn
        self.minlaengd = minlaengd
        self.antal = antal
        self.pirrfaktor = pirr
        self.startad = 0
        self.haveri=1
        self.ljud=ljud
        

    # För utskrift av ett objekt med print
    def __str__(self):
        return self._namn + ", en attraktion med pirrfaktor "+ str(self._pirrfaktor)+ " !!"

    # Slumpa fram haveri, ett tal som är 0,1,eller 2.
    # om det är 0 -> Skriv ut meddelande, stoppa och återställ
    # maskinen (_haveri=1)
    def haverera(self):
        self._haveri = random.randrange(0,3)
        if self._haveri == 0:
            self._haveri=1
            print self._namn + " har havererat! :("
            self.stoppa()
            print "Ambulans tillkallas..."
            
    def skrivStart(self):
        print self
        print "Nu bär det iväg med " + self._namn + ". Håll i era hattar alla "+ str(self._antal) + "! :)"
        print self._ljud + "!"

    # Kolla om man redan har startat
    # Om svar Ja: Gör inget , men meddela att man har redan åkt
    # Om svar Nej: Skriv meddelande. Sätt om startstatus,
    # och simulera fram haveri 
    def starta(self):
        if self._startad == 0:
            self.skrivStart()
            self._startad=1
            self.haverera()
        else:
            print "Startförsök: "+self._namn + " har redan åkt. Ni får vänta :("

    # Om man inte har startat än: skrive meddelande
    # Annars: meddela att man stoppar och sätt om startstatus till 0.
    def stoppa(self):
        if self._startad <> 0:
            print "Nu stoppas " + self._namn + ". Hoppa av alla "+ str(self._antal) + "! :)"
            self._startad=0
        else:
            print "Stoppförsök:"+self._namn + " är redan stoppad!"
    
############### Huvudprogrammet ############
berg=Attraktion("Bergodalbana", 160, 100, 10, "Iiiih")
lust=Attraktion("Lustiga huset", 110, 50, 12, "Hahaha")
paris=Attraktion("Pariserhjul", 0, 10, 20, "Ooooh, så vackert")

print "VÄLKOMMEN TILL GRÖNA LUND!"
val=1
while val:
    print ""
    print    "Välj mellan följande tre attraktioner (1/2/3):"
    print "1: "+ str(berg)
    print "2: " +str( lust)
    print "3: " + str(paris)
    val=raw_input("Ditt val ->")
    print "************************************************************"
    if val=="1":
        berg.starta()
        berg.stoppa()
    elif val=="2":
        lust.starta()
        lust.stoppa()
    elif val=="3":
        paris.starta()
        paris.stoppa()
    else:
        val =0
    print "************************************************************"
        
slump= raw_input("Fortsatt test: vill du slumpa fram 20 start/stop med bergodalbanan eller vill du alternera start och stopp 20 ggr? (0/1)")
if slump =="0":
    for i in range(20):
        test = random.randrange(0,2)
        if test==0:
            berg.starta()
        else:
            berg.stoppa()
elif slump=="1":
    for i in range(10):
        berg.starta()
        berg.stoppa()
        print "---------------------"
else:
    print "Hej då."