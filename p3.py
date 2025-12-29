quiz_questions={
    "1":{
        "question":"Which of the following Character comments in Python?",
        "options":{
            "A":"#",
            "B":"//",
            "C":"/* */",
            "D":"<!-- -->"
        },
        "Correct_answer":"A"
    },
    "2":{
        "question":"Which of the following statements is used to create an empty set in Python?",
        "options":{
            "A":"()",
            "B":"[]",
            "C":"{}",
            "D":"set()"
        },
        "Correct_answer":"D"
    },
    "3":{
        "question":"Which method is used to add an element to a list?",
        "options":{
            "A":"add()",
            "B":"addlist()",
            "C":"update()",
            "D":"append()"
        },
        "Correct_answer":"D"
    }
}
score=0
for key in quiz_questions:
    print("\n"+quiz_questions[key]["question"])
    for option, value in quiz_questions[key]["options"].items():
        print(f"{option}.{value}")
    user_answer=input("Enter your answer(A/B/C/D):").upper()
    if user_answer==quiz_questions[key]["Correct_answer"]:
        score+=1
print("\nQuiz Completed")
print(f"Your final score is: {score}/{len(quiz_questions)}")