score = 0

questions = [
    {
        "question": "What is the capital of India?",
        "answer": "delhi"
    },
    {
        "question": "Which language is used for web development?",
        "answer": "html"
    },
    {
        "question": "What is 5 + 5?",
        "answer": "10"
    }
]

print("🎯 Welcome to Quiz Game")

for q in questions:
    user_answer = input(q["question"] + " ").lower()
    
    if user_answer == q["answer"]:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")

print("\nYour Score:", score, "/", len(questions))