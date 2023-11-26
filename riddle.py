import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

#nrOfPrisoners = int(input("With how many prisoners do you want to run the experiment? "))
nrOfPrisoners = 1
nrOfTries = int(input("How many times do you want to run the experiment? "))
nrOfTimesAllPrisonersFree = 0
start = timer()
nrOfPrisonersFreeList = []
occurencesList = []
changesList = []

def printResults(nrOfTimesAllPrisonersFree, nrOfTries, end, start):
    percentage = nrOfTimesAllPrisonersFree / nrOfTries * 100
    timer = end - start
    print(f"All prisoners got out {nrOfTimesAllPrisonersFree} of the {nrOfTries} attempts!")
    print(f"Thats {percentage}% of the times!")
    print(f"It took {timer} seconds!")

def plotMaker1(nrOfPrisoners, nrOfPrisonersFreeList):
    for iValue in list(range(1, nrOfPrisoners + 1)) :
        occurences = nrOfPrisonersFreeList.count(iValue)
        occurencesList.append(occurences)
        #print(f"{iValue} {occurences}")
        #print(" ")
    
    left_coordinates= list(range(1, nrOfPrisoners + 1))
    heights=occurencesList
    bar_labels=list(range(1, nrOfPrisoners + 1)) 
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.5,color=['green'])
    plt.xlabel('Aantal keer')
    plt.ylabel('Aantal gevangen ontsnapt')
    plt.title("Hoeveel gevangen ontsnapten?")
    plt.show()

def plotMaker2(changesList):
    x=list(range(1, 1001, 10))
    y=changesList
    plt.plot(x,y)
    plt.xlabel('Aantal gevangenen')
    plt.ylabel('Kansen')
    plt.title("Hoeveel kans om eruit te geraken met aantal gevangen?")
    plt.show()

while nrOfPrisoners <= 1000:
    nrOfTimesAllPrisonersFree = 0
    for iTries in range(nrOfTries):
    
        boxes = list(range(nrOfPrisoners)) 
        #print(boxes)
        random.shuffle(boxes)
        
        nrOfPrisonersFree = 0
        
        for iPrisoner in range(nrOfPrisoners):
            nrOfBoxesOpened = 0 
            found = 0
            numberToFind = iPrisoner
            boxToOpen = iPrisoner
            while found == 0 and nrOfBoxesOpened <= (nrOfPrisoners/2):
                boxToOpen = (boxes[boxToOpen])
                #print(boxToOpen)
                nrOfBoxesOpened += 1
                
                if boxToOpen == numberToFind:
                    found = 1
                    nrOfPrisonersFree += 1
                    #print("Succes")
                
            
        if nrOfPrisonersFree == nrOfPrisoners:
            #print("WOOHOO") 
            nrOfTimesAllPrisonersFree += 1 
        nrOfPrisonersFreeList.append(nrOfPrisonersFree)
    
    changesList.append(nrOfTimesAllPrisonersFree / nrOfTries * 100)
    nrOfPrisoners += 10

#print(nrOfPrisonersFreeList)
end = timer()

printResults(nrOfTimesAllPrisonersFree, nrOfTries, end, start)
plotMaker1(nrOfPrisoners, nrOfPrisonersFreeList)
plotMaker2(changesList)
print("done")
        
