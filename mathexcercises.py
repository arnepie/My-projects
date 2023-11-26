import random
import time

answer = " "
user_answer = " "

def excercise_maker():
    pass

def excercise_checker(answer, user_answer):
    if answer == int(user_answer):
        print("That's correct!")
    else:
        print("That's incorrect!")
        print(f"The right answer was {answer}")

    
print("Welcome to the ultimate math game!")
print(" ")
print("- Made by Arne Pissoort")
amount_of_excercises = input("How many excercises do you want to do? ")
sort_of_excercises = input("Wich excercises do you want to do? (multiplication / division / addition / subtraction) ")
print("In wich range can the numbers be?")
lowest_number = input("Lowest number: ")
highest_number = input("Highest number: ")

start = time.time()

for i in range(int(amount_of_excercises)):
    if sort_of_excercises == "multiplication":
        excercise_number_1 = random.randint(int(lowest_number), int(highest_number))
        excercise_number_2 = random.randint(int(lowest_number), int(highest_number))
        user_answer = input(f"{excercise_number_1} * {excercise_number_2} = ")
        answer = excercise_number_1 * excercise_number_2
        
    elif sort_of_excercises == "division":
        excercise_number_1 = random.randint(int(lowest_number), int(highest_number))
        excercise_number_2 = random.randint(int(lowest_number), int(highest_number))
        user_answer = input(f"{excercise_number_1} / {excercise_number_2} = ")
        answer = excercise_number_1 / excercise_number_2
        
    elif sort_of_excercises == "addition":
        excercise_number_1 = random.randint(int(lowest_number), int(highest_number))
        excercise_number_2 = random.randint(int(lowest_number), int(highest_number))
        user_answer = input(f"{excercise_number_1} + {excercise_number_2} = ")
        answer = excercise_number_1 + excercise_number_2
    
    elif sort_of_excercises == "subtraction":
        excercise_number_1 = random.randint(int(lowest_number), int(highest_number))
        excercise_number_2 = random.randint(int(lowest_number), int(highest_number))
        user_answer = input(f"{excercise_number_1} - {excercise_number_2} = ")
        answer = excercise_number_1 - excercise_number_2
    
    excercise_checker(answer, user_answer)

end = time.time()
final_time = end - start

print(f"You did it in {final_time} seconds!")