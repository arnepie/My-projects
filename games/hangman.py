import random

PlayerWon = False
PlayerLost = False
PlayersProgress = []
Fails = 0

def Choose_word(PlayersProgress):
    WordList = ["cat", "sun", "cup", "ghost", "flower", "pie", "cow", "banana", "snowflake", "bug",
                "book", "jar", "snake", "light", "tree", "lips", "apple", "slide", "socks", "smile",
                "swing", "coat", "shoe", "water", "heart", "hat", "ocean", "kite", "dog",  "mouth",
                "milk", "duck", "eyes", "skateboard", "bird", "boy", "apple", "person", "girl",
                "mouse", "ball", "house", "star", "nose", "bed", "whale", "jacket", "shirt", "hippo",
                "beach", "egg", "face", "cookie", "cheese", "cone", "drum", "circle", "spoon", "worm"]
    Word = WordList[random.randint(0, len(WordList) - 1)]
    
    print(f"The word is {len(Word)} characters long!")
    
    for letter in Word:
        PlayersProgress.append("_")
        
    return Word, PlayersProgress
    # print(Word)
    
def Guess_letter(Word, PlayerWon, Fails, PlayersProgress):
    WordLetters = []
    LetterInWord = False
    
    for letter in Word:
        WordLetters.append(letter)
        
    LetterOrWord = input("Do you want to guess a letter or a word? (letter / word) ")
    
    if LetterOrWord == "letter":
        LetterGuessed = input("What letter do you want to guess? ")
        for letter in WordLetters:
            if LetterGuessed == letter:
                print(f"{LetterGuessed} is in the word!")
                LetterInWord = True
                indexnumber = 0
                for letter in WordLetters:
                    if letter == LetterGuessed:
                        PlayersProgress[indexnumber] = LetterGuessed
                    indexnumber += 1
        if LetterInWord != True:
            print(f"{LetterGuessed} is not in the word!")
            Fails += 1
            
    if LetterOrWord == "word":
        WordGuessed = input("What word do you want to guess? ")
        if WordGuessed == Word:
            print("Congrats! You won!")
            PlayerWon = True
            
        else:
            print("That's not the correct word!")
            Fails += 1
    
    else:
        print("That's not a valid option!")
        
    if PlayerWon == True:
        return True, Fails, PlayersProgress
    else: 
        return False, Fails, PlayersProgress

def Check_Fails(Fails, PlayerLost, Word):
    HangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    if Fails == 7:
        print("You lost!")
        print(f"The word was {Word}")
        PlayerLost = True
    else: 
        print(f"You have {7 - Fails} lives left!")
        print(HangmanPics[Fails])
    
    return PlayerLost
        
print("Welcome to Hangman!") 
Word, PlayersProgress = Choose_word(PlayersProgress)
#print(Word)
print("Start guessing...") 
#print(PlayersProgress)

while PlayerWon == False and PlayerLost == False:
    PlayerWon, Fails, PlayersProgress = Guess_letter(Word, PlayerWon, Fails, PlayersProgress)
    PlayerLost = Check_Fails(Fails, PlayerLost, Word)
    print(" ")
    print(PlayersProgress)
