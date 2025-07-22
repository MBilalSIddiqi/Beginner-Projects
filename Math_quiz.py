import random
import operator

# Dictionary of operations
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv  # Integer (floor) division
}

# Function to generate a question
def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op_symbol = random.choice(list(operations.keys()))

    # Avoid division by zero
    if op_symbol == '/' and num2 == 0:
        num2 = random.randint(1, 20)

    question = f"{num1} {op_symbol} {num2}"
    answer = operations[op_symbol](num1, num2)
    return question, answer

# Function to ask multiple questions
def ask_questions():
    total_questions = 5
    score = 0

    for i in range(total_questions):
        question, correct_answer = generate_question()
        print(f"\n{i + 1}. What is {question}?")

        try:
            user_input = int(input("Your answer: "))
            if user_input == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong. The correct answer is {correct_answer}.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

    print(f"\nYour Score: {score} out of {total_questions}")

# Start the quiz
ask_questions()
