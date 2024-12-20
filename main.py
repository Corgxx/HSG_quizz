import json

def load_quiz(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []

def run_quiz(quiz_data):
    score = 0
    total_questions = len(quiz_data)

    if total_questions == 0:
        print("No questions available in this quiz.")
        return

    # Ask the player to choose the number of questions
    while True:
        try:
            num_questions = int(input(f"Choose the number of questions (1-{total_questions}): "))
            if 1 <= num_questions <= total_questions:
                break
            else:
                print(f"Please enter a number between 1 and {total_questions}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Select the desired number of questions
    selected_questions = quiz_data[:num_questions]

    for i, question in enumerate(selected_questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for j, option in enumerate(question["options"], start=1):
            print(f"{j}. {option}")

        # Get user input
        try:
            user_choice = int(input("Enter your answer (1, 2, etc.): "))
            user_answer = question["options"][user_choice - 1]
            question['user_answer'] = user_answer  # Store user's answer
            if user_answer == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['answer']}")
        except (ValueError, IndexError):
            print("Invalid input. Skipping this question.")
            question['user_answer'] = "No Answer"

    # Display the final score
    print(f"\nQuiz completed! Your score: {score}/{num_questions}")

    # Display summary
    print("\nSummary:")
    for i, question in enumerate(selected_questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")
        print(f"Your Answer: {question.get('user_answer', 'No Answer')}")
        print(f"Correct Answer: {question['answer']}")

def main():
    while True:
        print("\nWelcome to the Quiz Game!")
        print("1. Easy")
        print("2. Medium")

        # Let the player choose the difficulty level
        while True:
            difficulty_choice = input("Choose your difficulty (1 for Easy, 2 for Medium): ")
            if difficulty_choice == "1":
                quiz_file = 'easy.json'
                break
            elif difficulty_choice == "2":
                quiz_file = 'medium.json'
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

        # Load the selected quiz and run it
        quiz_data = load_quiz(quiz_file)
        run_quiz(quiz_data)

        # replay  
        replay_choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay_choice not in ['yes', 'y']:
            print("Thank you for playing! Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()

