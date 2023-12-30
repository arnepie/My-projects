import random
import pygame
import time

Possible_Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Total_Coins_Won_Or_Lost = 0

def Slot_Machine(Possible_Numbers):
    Outcome = []
    
    for i in range(3):
        Outcome.append(Possible_Numbers[random.randint(0, 9)])
    
    return Outcome

def User_Game_Text(Total_Coins_Won_Or_Lost):
    print("------------------------------------------------------------------------------------------")
    print("Welcome to the SLOT MACHINE!")
    print("Every one coin you spent you get one spin!")     
    print("If you get 3 numbers that are the same you get 75 coins")    
    print("------------------------------------------------------------------------------------------")
    Number_Of_Coins = int(input("How many coins do you want to spend? "))
    
    for i in range(Number_Of_Coins):
        Outcome = Slot_Machine(Possible_Numbers)
        
        if Outcome[0] == Outcome[1] == Outcome[2]:
            print(Outcome)
            print("You got 75 coins!")
            Total_Coins_Won_Or_Lost += 75
        else:
            Total_Coins_Won_Or_Lost -= 1
            print(Outcome)
    
    print(" ")
    
    if Total_Coins_Won_Or_Lost < 0:
        print(f"In total you lost {abs(Total_Coins_Won_Or_Lost)} coins!")
    elif Total_Coins_Won_Or_Lost > 0:
        print(f"In total you gained {Total_Coins_Won_Or_Lost} coins!")
    elif Total_Coins_Won_Or_Lost == 0:
        print("In total you gained 0 coins!")

def Make_Screen():
    pygame.init()
    
    Outcome = Slot_Machine(Possible_Numbers)
    background_color = (255, 255, 255)
    red = (255,0,0)
    green = (0, 255, 0)
    blue = (0, 255, 255)
    screen = pygame.display.set_mode((1000, 1000))
    
    pygame.display.set_caption('Slot Machine!')
    screen.fill(background_color)
    
    pygame.draw.rect(screen, red, pygame.Rect(83, 350, 200, 400))
    pygame.draw.rect(screen, red, pygame.Rect(416, 350, 200, 400))
    pygame.draw.rect(screen, red, pygame.Rect(749, 350, 200, 400))
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render(str(Outcome[0]), True, green, red)
    text2 = font.render(str(Outcome[1]), True, green, red)
    text3 = font.render(str(Outcome[2]), True, green, red)
    screen.blit(text1, (183, 550))
    screen.blit(text2, (516, 550))
    screen.blit(text3, (849, 550))

    pygame.display.flip()
    
    time.sleep(5)
    font2 = font = pygame.font.Font('freesansbold.ttf', 128) 
    
    if Outcome[0] == Outcome[1] == Outcome[2]:
        Winning_Text = font2.render(("You won"), True, green, blue)
        screen.blit(Winning_Text, (270, 500))
    else: 
        Losing_Text = font2.render(("You lost"), True, green, blue)
        screen.blit(Losing_Text, (270, 500))
    
    pygame.display.flip()
    
    running = True
    
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
    
    
    
        
def Computer_Tester(Total_Coins_Won_Or_Lost):
    Number_Of_Coins = int(input("How many coins do you want to spend per trie? "))
    Number_Of_Tries = int(input("How many tries do you want to do? "))
    Total_Coins = 0
    #Average_Coins = 0
    
    for i in range(Number_Of_Tries):
        for i in range(Number_Of_Coins):
            Outcome = Slot_Machine(Possible_Numbers)
            
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


#User_Game_Text(Total_Coins_Won_Or_Lost)  
#Computer_Tester(Total_Coins_Won_Or_Lost)
Make_Screen()
