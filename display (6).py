import random

print("Welcome to professor assistant version 1.0")

Name = input("Enter your name: ")

if Name.lower() == "ibrahim musa":
    print(f"Hello Professor {Name}, I am here to help you create exams from a question bank.")
else:
    print(f"Hello Professor {Name}, I am here to assist you.")

question = input("Do you want me to create a question? (yes/no): ").lower()

if question == "yes":
    file_path = input("Enter full path of your question bank file: ")

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        exit()

    # Each pair = 2 lines
    total_pairs = len(lines) // 2

    print(f"\nFile loaded successfully. Total available pairs: {total_pairs}")

    question_2 = int(input("How many random question–answer pairs do you want? "))

    if question_2 > total_pairs:
        print(f"Sorry! Only {total_pairs} pairs available. Please reduce the number.")
        exit()

    print("\nYour Random Exam Questions:\n")

    selected_pairs = []
    used_indices = set()

    while len(selected_pairs) < question_2:
        # Each question starts at even index 0,2,4,...
        i = random.randint(0, total_pairs - 1) * 2

        if i not in used_indices:
            used_indices.add(i)
            question_text = lines[i].strip()
            answer_text = lines[i + 1].strip()

            selected_pairs.append((question_text, answer_text))

            print(f"Q: {question_text}")
            print(f"A: {answer_text}\n")

    save_path = input("Enter filename to save exam (e.g., midterm.txt): ")

    with open(save_path, 'w') as output_file:
        for q, a in selected_pairs:
            output_file.write(f"Q: {q}\n")
            output_file.write(f"A: {a}\n\n")

    print(f"\nCongratulations Professor {Name}. Your exam is saved as '{save_path}'.")
else:
    print("Okay, I am here whenever you need help.")
