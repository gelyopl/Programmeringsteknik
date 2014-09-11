
import random
import math

REACTIONS = [": Zzzzz",": Boring...",": Meh..",": Woho!",": Iiih!",": Ooooh!",": WHOOA!!",": HOLY ****!!!",": I'M GONNA DIE!!!!","is passed out"];
DASHED_LINE = "---------------------------------------"
QUALITY = 5; # The probability of an attraction breaking is 1/QUALITY.

class Visitor:
    def __init__(self,name,height):
        self.name = name
        self.height = height

class Attraction:
    def __init__(self,name,minHeight,scariness):
        self.name = name
        self.minHeight = minHeight
        self.scariness = scariness
        self.queue = []
        self.broken = False
                
    def addToQueue(self, visitor):
        if visitor.height < self.minHeight:
            print("Sorry",visitor.name,"! You must be at least",self.minHeight,"cm to ride the",self.name)
        else:
            self.queue.append(visitor)
            print(visitor.name,"got in line at the",self.name)

    def start(self):
        if len(self.queue) != 0:
            print("The",self.name,"is starting!")
            lucky = math.floor(random.random()*QUALITY)
            if not lucky:
                print("Something went wrong! The",self.name,"is broken!")
                self.broken = True
            else:
                for i in range(len(self.queue)):
                    tmpVisitor = self.queue.pop()
                    fright = math.floor(random.random()*self.scariness)
                    reaction = REACTIONS[fright]
                    print(tmpVisitor.name,reaction)
                    
    def getName(self):
        return self.name

    def getScariness(self):
        return self.scariness

    def __iter__(self):
        return self

# I've chosen to use container objects in order to get more elegant code down the line.
# This could have been achived with lists holding objects.

class Party:
    def __init__(self):
        self.visitors = []

    def __iter__(self):
        return iter(self.visitors)

    def addVisitor(self,name, height):
        self.visitors.append(Visitor(name, height))

class Park:
    def __init__(self,name):
        self.name = name
        self.attractions = []

    def __iter__(self):
        return iter(self.attractions)

    def __getitem__(self,key):
        # Matching indices with menu options
        return self.attractions[key-1]

    def __len__(self):
        return len(self.attractions)
        
    def addAttraction(self,name,minHeight,scariness):
        self.attractions.append(Attraction(name,minHeight,scariness))

# -------------------------------------------------------------------

parkObject = Park("The Funland")
partyObject = Party()

parkObject.addAttraction("Super Scary Rollercoaster",140,10)
parkObject.addAttraction("Kinda Scary Carousel",130,5)
parkObject.addAttraction("Horse Carousel",110,2)

# Hello world
print("\t\tAMUSEMENT PARK\n")
print("Welcome to",parkObject.name)

# Making sure we don't leave this phase without valid input
gotValidNumber = False
while not gotValidNumber:
    n = input("How many tickets would you like? ")
    if n.isnumeric():
        n = int(n)
        gotValidNumber = True
        for i in range(n):
            gotValidHeight = False
            print("Please enter the name of visitor nr.",i+1,":",end=" ")
            name = input()
            while not gotValidHeight:
                print("Please enter",name,"'s height in centimeters:",end=" ")
                height = input()
                if height.isnumeric():
                    partyObject.addVisitor(name,int(height))
                    gotValidHeight = True
                else:
                    print("You must enter a valid height, numbers only. Please try again...")
    else:
        print("You must enter a valid number. Please try again...")
    
# Main loop    
running = True
while running:
    print("\nHere is a list of our available rides:")
    print(DASHED_LINE)
    i = 1;
    print(0,"Exit");
    for ride in parkObject:
        if ride.broken:
            print(i,ride.getName(),"( BROKEN )")
        else:
            print(i,ride.getName(),"( Scariness level:",ride.scariness,")")
        i += 1
    print(DASHED_LINE)
    n = input("Please select: ")
    print()
    
    if n.isnumeric():
        n = int(n)
        if n == 0:
            running = False
        elif n <= len(parkObject):
            if parkObject[n].broken:
                print("Sorry, the",parkObject[n].name,"is broken!")
            else:
                for visitor in partyObject:
                    parkObject[n].addToQueue(visitor)
                parkObject[n].start()
        else:
            print("You must select something from the list!")
    else:
        print("You can only write numbers")

# Goodbye world
print("Hope you had a great time. Come back soon!")