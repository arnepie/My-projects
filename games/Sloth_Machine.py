import random

Possible_Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Total_Coins_Won_Or_Lost = 0

def Sloth_Machine(Possible_Numbers):
    Outcome = []
    
    for i in range(3):
        Outcome.append(Possible_Numbers[random.randint(0, 9)])
    
    return Outcome

def User_Game(Total_Coins_Won_Or_Lost):
    print("------------------------------------------------------------------------------------------")
    print("Welcome to the SLOTH MACHINE!")
    print("Every one coin you spent you get one spin!")     
    print("If you get 3 numbers that are the same you get 75 coins")    
    print("------------------------------------------------------------------------------------------")
    Number_Of_Coins = int(input("How many coins do you want to spend? "))
    
    for i in range(Number_Of_Coins):
        Outcome = Sloth_Machine(Possible_Numbers)
        
        if Outcome[0] == Outcome[1] == Outcome[2]:
            print(Outcome)
            print("You got 75 coins!")
            Total_Coins_Won_Or_Lost += 75
        else:
            Total_Coins_Won_Or_Lost -= 1
    
    print(" ")
    
    if Total_Coins_Won_Or_Lost < 0:
        print(f"In total you lost {abs(Total_Coins_Won_Or_Lost)} coins!")
    elif Total_Coins_Won_Or_Lost > 0:
        print(f"In total you gained {Total_Coins_Won_Or_Lost} coins!")
    elif Total_Coins_Won_Or_Lost == 0:
        print("In total you gained 0 coins!")
        
def Computer_Tester(Total_Coins_Won_Or_Lost):
    Number_Of_Coins = int(input("How many coins do you want to spend per trie? "))
    Number_Of_Tries = int(input("How many tries do you want to do? "))
    Total_Coins = 0
    #Average_Coins = 0
    
    for i in range(Number_Of_Tries):
        for i in range(Number_Of_Coins):
            Outcome = Sloth_Machine(Possible_Numbers)
            
            if Outcome[0] == Outcome[1] == Outcome[2]:
                #print(Outcome)
                #print("You got 75 coins!")
                Total_Coins_Won_Or_Lost += 75
            else:
                Total_Coins_Won_Or_Lost -= 1
            
            Total_Coins += Total_Coins_Won_Or_Lost
            Total_Coins_Won_Or_Lost = 0
        #Average_Coins = Total_Coins / Number_Of_Coins
    
    #print(Average_Coins)
    print(f"On average you made {Total_Coins / Number_Of_Tries} per {Number_Of_Coins} coins!")


#User_Game(Total_Coins_Won_Or_Lost)  
Computer_Tester(Total_Coins_Won_Or_Lost)
    
