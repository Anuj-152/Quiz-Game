print("!---welcome to quiz game---!")
print(" ")

def question_series():
    return [
        {"question": "Ques 1. What is the capital of Bihar?", "choices": ["A. Patna", "B. Siwan", "C. Chhapra", "D. Gaya"], "answer": "A"},
        {"question": "Ques 2. What is 2 + 2?", "choices": ["A. 3", "B. 4", "C. 5", "D. 6"], "answer": "B"},
        {"question": "Ques 3. When was Mahatma Gandhi born?", "choices": ["A. 1969", "B. 1869", "C. 1996", "D. 1896"], "answer": "B"}
    ]

def asked_question(question):
    print(question["question"])
    for choices in question["choices"]:
        print(choices)
    answer = input("Your answer: ")
    if answer.upper() == question["answer"]:
        return True
    else:
        print(f"Wrong! The correct answer is option {question['answer']}")
        return False

def quiz_game():
    questions = question_series()
    score = 0

    for question in questions:
        if asked_question(question):
            print("Correct!")
            score += 1

    print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
