questions = [
    {
        "prompt": "What is the capital of Nigeria",
        "options": ["A. Paris", "B. Lagos", "C. Dubai"],
        "answer": "B"
    },

    {
        "prompt": "Which language is most spoken in Algeria",
        "options": ["A. French", "B. Spanish", "C. Arabic"],
        "answer": "C"
    },

    {
        "prompt": "Who is the leader of a family",
        "options": ["A. Sister", "B. Father", "C. Ayman"],
        "answer": "B"
    }

]

def start_quiz(questions):
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter the answer (A, B, C): ").upper()
        if answer == question["answer"]:
            print("You are correct")
        else:
            print("You are wrong")

start_quiz(questions)
