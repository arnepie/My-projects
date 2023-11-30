import matplotlib.pyplot as plt

primeNumbersToSearch = int(input("How many numbers do you want to search? "))
primeNumbersFound = 0
primeNumbersFoundList = []
listOfPrimeNumbers = []
allNumbersList = []

def plotMaker(allNumbersList, primeNumbersFoundList):
    y=primeNumbersFoundList
    x=allNumbersList
    plt.plot(x,y)
    plt.xlabel('Aantal nummers')
    plt.ylabel('Primegetallen gevonden')
    plt.title("Hoeveel priemgetallen zijn er over een aantal getallen?")
    plt.show()

for iNumber in range(100000000, primeNumbersToSearch):
    flag = False
    allNumbersList.append(iNumber)
    
    if iNumber == 1:
        flag = True
    else:
        for iDivider in range(2, iNumber):
            if iNumber % iDivider == 0:
                flag = True
                #print(f"Flag for {iDivider}")
                break

    if flag == True:
        #print(f"{iNumber} is not a prime number.")
        pass
    else:
        #print(f"{iNumber} is a prime number.")
        listOfPrimeNumbers.append(iNumber)
        primeNumbersFound += 1
    
    primeNumbersFoundList.append(primeNumbersFound)
    
#print(allNumbersList)
#print(primeNumbersFoundList)
#plotMaker(allNumbersList, primeNumbersFoundList)        

print(" ")
print("Done!")
print(f"Heres a list the {primeNumbersFound} prime numbers found!")
print(listOfPrimeNumbers)