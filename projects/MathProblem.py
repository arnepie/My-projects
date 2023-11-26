import time
import matplotlib.pyplot as plt
from timeit import default_timer as timer

tries = int(input("How many numbers do you want to test?"))
correctNumbers = 0
start = timer()
numbersList = []
stepsList = []
stepsHighestNumber = 0

def plotMaker1(numbersList, stepsList):   
    left_coordinates=numbersList
    heights=stepsList
    bar_labels=numbersList
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.5,color=['green'])
    plt.xlabel('Nummer')
    plt.ylabel('Stappen')
    plt.title("Hoeveel stappen om tot 1 te komen?")
    plt.show()
    
def plotMaker2(numbersList, stepsList):
    x=numbersList
    y=stepsList
    plt.plot(x,y)
    plt.xlabel('Nummer')
    plt.ylabel('Stappen')
    plt.title("Hoeveel stappen om tot 1 te komen?")
    plt.show()

def findHighestNumber(stepsList, numbersList):
    indexHighestStepsNumber = stepsList.index(max(stepsList))
    stepsHighestStepsNumber = max(stepsList)
    highestStepsNumber = numbersList[indexHighestStepsNumber]
    
    print(f"The number with the most steps was {highestStepsNumber}, it had {stepsHighestStepsNumber} steps!")
    

for iTries in range(tries):
    steps = 0
    numberTested = iTries
    numbersList.append(numberTested)
    #print(numberTested)
    
    while numberTested != 1:
        if numberTested % 2 == 0 and numberTested != 0:
            numberTested = numberTested / 2
            #print(numberTested)
        else:
            numberTested = numberTested * 3 + 1
            #print(numberTested)
        steps += 1
        
    correctNumbers += 1
    stepsList.append(steps)
        
    print(f"Succes {iTries} in {steps} steps.")

#plotMaker1(numbersList, stepsList)
#plotMaker2(numbersList, stepsList)
findHighestNumber(stepsList, numbersList)

#print(numbersList)
#print(stepsList)
#print(correctNumbers)
#print(tries)
end = timer()
timer = end - start

if correctNumbers == tries:
    print("All numbers follow the rule!")
print(f"Done in {timer} seconds!")

