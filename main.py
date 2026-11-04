import random as rand
name = input("Vad heter du?\n> ")
print(f"Hej {name} och välkommen till spelet!")

for i in range(3):
    random_number = rand.randint(1,10)
    num_guess = int(input("Gissa ett tal mellan 1 och 10\n> "))

    if num_guess == random_number:
        print("Rätt gissat!")
        break
    else:
        print("Fel gissat!")
