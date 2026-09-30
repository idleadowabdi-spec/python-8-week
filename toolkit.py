# Personal Mini-Toolkit
# PLP Week 8 Final Project
# Student Name: IDLE ADOW ABDI


# Tool 1: Simple Calculator
# This tool performs basic mathematical calculations.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter your choice: ")

        if operation == "1":
            result = first_number + second_number
            print(f"Result: {first_number} + {second_number} = {result}")

        elif operation == "2":
            result = first_number - second_number
            print(f"Result: {first_number} - {second_number} = {result}")

        elif operation == "3":
            result = first_number * second_number
            print(f"Result: {first_number} x {second_number} = {result}")

        elif operation == "4":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                result = first_number / second_number
                print(f"Result: {first_number} / {second_number} = {result}")

        else:
            print(f"Sorry, '{operation}' is not a valid operation.")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: To-Do List
# This tool lets the user add, view, and remove tasks.
def todo_list(tasks):
    print("\n--- To-Do List ---")

    while True:
        print("\nTo-Do List Options:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")

            if task.strip() == "":
                print("Please enter a task.")
            else:
                tasks.append(task)
                print(f"Task added: {task}")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour Tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                print("\nYour Tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid task number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


# Tool 3: Number Guessing Game
# This tool asks the user to guess a secret number.
def guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I have chosen a secret number between 1 and 10.")
    print("Try to guess it!")

    secret_number = 7
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(
                    f"Congratulations! You guessed the number "
                    f"{secret_number} in {attempts} attempts."
                )
                break

        except ValueError:
            print("Please enter a whole number.")


# Main menu
# This function controls the whole Personal Mini-Toolkit.
def main():
    tasks = []

    print("\n========================================")
    print("       WELCOME TO MY MINI-TOOLKIT")
    print("========================================")
    print("Useful tools made with Python!")

    while True:
        print("\n========================================")
        print("       PERSONAL MINI-TOOLKIT")
        print("========================================")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            todo_list(tasks)

        elif choice == "3":
            guessing_game()

        elif choice == "4":
            print("\nThank you for using my Personal Mini-Toolkit!")
            print("Goodbye! Have a great day!")
            break

        else:
            print(f"Sorry, '{choice}' is not on the menu.")
            print("Please choose an option from 1 to 4.")


# Start the program
if __name__ == "__main__":
    main()