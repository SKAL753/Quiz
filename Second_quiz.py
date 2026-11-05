questions = [
    {
        "question": "Vilken huvudstad har Sverige?",
        "options": ["Oslo", "Stockholm", "Köpenhamn"],
        "correct": 2
    },
    {
        "question": "Vilket år började andra världskriget?",
        "options": ["1914", "1939", "1945"],
        "correct": 2
    },
    {
        "question": "Vilken planet är störst i vårt solsystem?",
        "options": ["Jorden", "Saturnus", "Jupiter"],
        "correct": 3
    },
    {
        "question": "Vilket grundämne har den kemiska beteckningen O?",
        "options": ["Guld", "Syre", "Silver"],
        "correct": 2
    },
    {
        "question": "Hur många bitar består en byte av?",
        "options": ["4", "8", "16"],
        "correct": 2
    }
]

correct_answers = 0

for current_question in questions:
    print(current_question["question"])
    for i, option in enumerate(current_question["options"], start=1):
        print(f"{i}. {option}")

    answer = int(input("Ditt val: "))

    if answer == current_question["correct"]:
        print("Rätt")
        correct_answers += 1
    else:
        print("Fel")
print(f"Du fick {correct_answers} av {len(questions)} rätt.")