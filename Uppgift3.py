import random
import math

REAKTIONER = [": håller på att somna",": tyckte det var bland det roligaste!!",": tycker det var helt okej",": vill aldrig göra det igen",": är nära på att spy",": vill åka igen!!", ": blev helt chockad",": tuppade av",": kommer berätta till alla sina vänner",": tyckte det var meeh"];
HAVERI = 10; #Hur troligt det är att attraktionen går sönder

#Klasserna

class Gaest:
	def __init__(self, namn, laengd):
			self.namn = namn
			self.laengd = laengd

class Saellskap:
	def __init__(self):
		self.gaester = []
		
	def __iter__(self):
		return iter(self.gaester)
		
	def laeggTillGaest(self,namn,laengd):
		self.gaester.append(Gaest(namn, laengd))
		
class Attraktion:
	def __init__(self, namn, minLaengd, pirrfaktor):
		self.namn = namn
		self.minLaengd = minLaengd
		self.pirrfaktor = pirrfaktor
		self.que = []  #Lista för kö
		self.trasig = False
		

	def start(self):
		if len(self.que) != 0: #Om kön inte är noll != 0
			print("Nu körs ", self.namn, " igång")
			slumpHaveri = math.floor(random.random()*HAVERI) #Med random kollar vi om den blir haveri (1/10)
			if not slumpHaveri:
				print(self.namn," gick sönder")
				self.trasig = True
			else:
				for i in range(len(self.que)):
					tempGaest = self.que.pop()  #Lista med alla gäster utan att behöva "flytta" dom
					slumppirrfaktor = math.floor(random.random()*self.pirrfaktor)
					reaktion = REAKTIONER[slumppirrfaktor]
					print(tempGaest.namn,reaktion)
					
	def KollaMinLaengd(self, Gaest):
		if gaest.laengd < self.minLaengd:
			print(gaest.namn,"måste tyvärr vara minst ",self.minLaengd," cm för att åka ",self.namn)
		else:
			self.que.append(gaest)   #Gästen läggs till i kön (appendad)
			print(gaest.namn," står ni i kön till ",self.namn)
			
	def __iter__(self): #retunerar
		return self	

	def getNamn(self): 
		return self.namn
		
	def getpirrfaktor(self):
		return self.pirrfaktor
		


		
class Park:
	def __init__(self,namn):	
		self.namn = namn
		self.attraktioner = []
		
	def __iter__(self):
			return iter(self.attraktioner)
			
	def __getitem__(self,key):
		return self.attraktioner[key-1]
		
	def __len__(self):
		return len(self.attraktioner)
		
	def laeggTillattraktion(self,namn,minLaengd,pirrfaktor):
		self.attraktioner.append(Attraktion(namn,minLaengd,pirrfaktor))
		

		

# Dags för loopar för leklander


parkObjekt = Park("Superskojiga lekalandet")
saellskapObjekt = Saellskap()

#Attraktioner, namn, längd, pirrhetfaktor
parkObjekt.laeggTillattraktion("Fritt fall", 150, 10)
parkObjekt.laeggTillattraktion("Nyckelpigan", 90, 2)
parkObjekt.laeggTillattraktion("Blå Tåget", 105, 5)
parkObjekt.laeggTillattraktion("Balder", 140, 7)


print("Välkommen till", parkObjekt.namn)

#Hur många dom är och längden. Stannar i loopen tills man har svarat korrekt
korrektinmatning = False
while  not korrektinmatning:
	n = input("Hur många är ni? ")
	if n.isnumeric():
		n = int(n)
		korrektinmatning = True
		for i in range(n):
			korrektLaengd = False
			print("Skriv in namnet på gäst", i+1,":",end=" ")
			namn = input()
			while not korrektLaengd:
				print("Skriv in längden på", namn, "i CM:",end=" ")
				laengd = input()
				if laengd.isnumeric():
					saellskapObjekt.laeggTillGaest(namn,int(laengd))
					korrektLaengd = True
				else:
					print("Du måste skriva in korrekt längd i siffror, testa igen")
	else:
		print("Du måste skriva in ett korrekt tal, testa igen")
		
# Programmet
koer = True
while koer:
	print("\nAttraktrioner ni kan åka är:")
	print("\n")
	i = 1;
	print(0, "Exit");
	for aektur in parkObjekt:
		if aektur.trasig:
			print(i,aektur.getNamn()," är tyvärr trasig )") #fortsätter vara trasig
		else:
			print(i,aektur.getNamn(),"(pirrhetsfaktor: ",aektur.pirrfaktor,")")
		i += 1
	print("\n")
	n = input("Välj: ")
	print()
	
	if n.isnumeric():
		n = int(n)
		if n == 0:
			koer = False
		elif n <= len(parkObjekt):
			if parkObjekt[n].trasig:
				print("Sorry, the", parkObjekt[n].namn,"är trasig")
			else:
				for gaest in saellskapObjekt:
					parkObjekt[n].KollaMinLaengd(gaest)
				parkObjekt[n].start()
		else:
			print("Du måste välja något ur listan")
	else:
		print("Du kan bara skriva siffror")
		
#Exit programmet
print("Hoppas du hade det roligt!!")