def inputmening1():
    mening1 = "Det finns ingen fil när jag handlade på Konsum."
	mening2 = "Bananerna var också slut."
	mening3 = "Jag köpte bröd istället."
	mening4 = "Nån sorts limpa med mycket fiber."
    return mening1

def split(meningen):
    meningen2 = meningen.split()

    return meningen2

def splitstora(mening):
     mening2 = mening.upper()
     mening3 = mening2.split()

     return mening3

def fyraforsta(lista):
    x = lista[0]+" "
    x += lista[1]+" "
    x += lista[2]+" "
    x += lista[3]+" "
    return x

def resten(mening):
  return mening[4:]

def resten(mening):
  mening[:4] = []
  return mening 

def dikt():
    print(k)
    print()
    print(l)
    print(n, end=" ")

meningV1 = inputmening1() #För första meningen

meningV2 = splitstora(meningV1) #Första meningens fyra första ord, stora
k = fyraforsta(meningV2)

meningenV3 = split(meningV1) #Första meningen fyra första ord, små
l = fyraforsta(meningenV3)

meningV4 = split(meningV1) #Första meningens sista ord.
n = resten(meningV4)


dikt()