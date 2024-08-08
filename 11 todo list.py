"""
Generates a todo list in which user can add, edit, complete, show and exit the program.

"""

while True:
    action = input("To add, show, edit, complete, exit?: ").strip()

    match action:
        case 'add':
            todo = input("enter a todo: ") + "\n"

            # Open, read (if necessary), and update todos list
            try:
                with open('todos.txt', 'r+') as file:
                    todos = file.readlines()
                    todos.append(todo)
                    file.seek(0)                                # Move to the beginning before writing
                    file.writelines(todos)
            except FileNotFoundError:
                with open('todos.txt', 'w') as file:            # Create if not found
                    file.write(todo)

        case 'show':
            for index, item in enumerate(todos):
                print(f"{index+1}. {item}")

        case 'edit':
            try:
                num = int(input("number of the todo to edit: "))
                if 0 <= num - 1 < len(todos):
                    new_todo = input("enter the new todo: ")
                    todos[num - 1] = new_todo
                else:
                    print("Error: Invalid todo number.")
            except ValueError:
                print("Error: Invalid input. Please enter a number.")

        case 'complete':
            try:
                num = int(input("which one did you complete? "))
                del todos[num - 1]                              # Consider using del for efficiency
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
            except IndexError:
                print("Error: Invalid todo number.")

        case 'exit':
            break

        case _:                                                 # Handle unexpected input
            print("Invalid action. Please try again.")
