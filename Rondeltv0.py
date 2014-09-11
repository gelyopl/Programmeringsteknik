# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# Axel Qvarfordt
# 18/5-2014
# Rondelet

# <Programkod>

def inmatning():
	mening = 5 * [None]
	i = 1
	print("Skriv in fyra meningar och få ut en rondelet! \n")

	while i < 5:
		mening[i] = input("Skriv mening nr " + str(i) + ": ")
		i += 1
	return mening


def split(meningSplit): #Splitar mening[1] till en list med varje ord försig
	list = meningSplit.split()

	return list
	
def upper(mening): #Gör första 4 ord i första mening stora
	ny_mening = mening.upper()
	return ny_mening
    
def dikt(): #Skriver ut hela dikten
	print(FirstFourUpper)
	print()
	print(JoinFirstFour)
	print(RestSentence)
	print(mening[2])
	print(mening[3])
	print(mening[4])
	print(JoinFirstFour)


inmatning()
#Anropar split på första meningen
SplitFirstMening = split(mening[1])
#Joinar fyra första och fyra första med stora bokstäver
JoinFirstFour = " ".join(SplitFirstMening[:4])
FirstFourUpper = upper(JoinFirstFour)
#Joinar resten av meningen
RestSentence = " ".join(SplitFirstMening[4:])
dikt()