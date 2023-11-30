import time
import random

def calculate_typing_speed(sentence_to_type, best_attempt):
    start_time = time.time()
    typed_text = input(f"Type the following sentence:\n{sentence_to_type} \n")
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    characters_per_minute = 60 / elapsed_time * len(sentence_to_type)
    characters_wrong = 0
    
    for a, b in zip(sentence_to_type, typed_text):
        if not a == b:
            characters_wrong += 1
    
    if characters_per_minute > best_attempt and characters_wrong == 0:
        best_attempt = characters_per_minute
        print("\n------------------------------")
        print("\nThis was your best attempt so far!")
    
    print(f"\nYour time: {str(elapsed_time)}")
    print(f"Characters per minute: {str(characters_per_minute)}")
    print(f"You had {str(characters_wrong)} characters wrong.")
    
    return best_attempt
    
    

if __name__ == "__main__":
    sentences_to_type = [
        "This is a very cool typing test!",
        "She made a long shopping list.",
        "We need a complete list of all the people who are attending the event.",
        "He had an endless list of excuses.",
        "We're on the waiting list for the class.",
        "Studying is on the top of my to-do list.",
        "My daughter gave me her wish list for Christmas.",
        "It was an impressive guest list.",
        "Let's make a guest list for the party.",
        "The bookstore released the best-seller list.",
        "She put bread on the shopping list.",
        "The guest list included friends of family members.",
        "My to-do list is growing.",
        "I didn't see my name on the list.",
        "There is a waiting list for golf membership.",
        "We have a guest list of 300 people."
        ]
    sentence_to_type = sentences_to_type[random.randint(0, 15)]
    attempts = 0
    best_attempt = 0
    
    print("Welcome to the typing test!")
    total_attempts = input("How many attempts do you want to do?")
    print("")
    try:
        while int(total_attempts) > attempts:
            input("Press enter when you're ready to start")
            print("\n------------------------------")
            print("\nStart typing...")
            time.sleep(1)
            best_attempt = calculate_typing_speed(sentence_to_type, best_attempt)
            attempts += 1
            sentence_to_type = sentences_to_type[random.randint(0, 15)]
    except:
        print("That's not a valid number.")
        
    print(f"\n You're best attempt was {best_attempt} characters per minute.)


        

        

