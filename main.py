import random as rand
name = input("Vad heter du?\n> ")
print(f"Hej {name} och välkommen till spelet!")

random_number = rand.randint(1,10)
num_guess = int(input("Gissa ett tal mellan 1 och 10\n> "))

if num_guess == random_number:
    print("Rätt gissat!")
else:
    print(f"Tyvärr, det var {random_number}")