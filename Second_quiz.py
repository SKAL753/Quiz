question_1 = "Vilken huvudstad har Sverige?\n1. Oslo\n2. Stockholm\n3. Köpenhamn"
question_2 = "Vilket år började andra världskriget?\n1. 1914\n2. 1939\n3. 1945"
question_3 = "Vilken planet är störst i vårt solsystem?\n1. Jorden\n2. Saturnus\n3. Jupiter"
question_4 = "Vilket grundämne har den kemiska beteckningen O?\n1. Guld\n2. Syre\n3. Silver"
question_5 = "Hur många bitar består en byte av?\n1. 4\n2. 8\n3. 16"

questions = [question_1, question_2, question_3, question_4, question_5]

answers = {
    question_1: 2,
    question_2: 2,
    question_3: 3,
    question_4: 2,
    question_5: 2,
}

correct_answers = 0

for current_question in questions:
    print(current_question)
    answer = int(input("Ditt val: "))

    if answer == answers[current_question]:
        print("Rätt")
        correct_answers += 1
    else:
        print("Fel")
print(f"Du fick {correct_answers} av {len(questions)} rätt.")