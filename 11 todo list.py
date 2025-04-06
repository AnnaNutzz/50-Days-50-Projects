"""
Generates a todo list CLI application
    user can add, edit, complete, show, and exit the program.
    It makes a .txt file in my file path to save the todo list.
"""

"""
variables for my own understanding and future references:
    todos -> is the file 
    todo -> is the item in the file above  
    file_path -> path to the file in my device
    item -> the content in the file
    index -> index of every item
    user_action -> the action the user needs to do to use the application

"""

file_path = "D:/Coding/Python/50 days 50 projects/files for codes/todos.txt"      # Path to save the to-do list


import functioning as func
"""
different new file
"""

# Main -----------------------------------------------------------

while True:
    user_action = input("To add, show, edit, complete, exit?: ").strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:].strip() + "\n"

        todos = func.read_todo()
        todos.append(todo)

        func.write_todo(file_path, todos)
        print(f"Added: {todo.strip()}")

    elif user_action == "show":
        todos = func.read_todo()

        if todos:
            for index, item in enumerate(todos, start=1):
                print(f"{index}. {item.strip()}")
        else:
            print("The todo list is empty!")

    elif user_action.startswith("edit"):
        try:
            todos = func.read_todo()

            num = int(user_action[5:])                                            # Extract the number
            index = num - 1

            if 0 <= index < len(todos):
                new_todo = input("Enter the new todo: ").strip() + "\n"
                todos[index] = new_todo

                func.write_todo(file_path, todos)
                print("Todo updated successfully.")
            else:
                print("Error: Invalid todo number.")

        except ValueError:
            print("Error: Please enter a valid number.")
        except FileNotFoundError:
            print("Error: Todo list not found.")

    elif user_action.startswith("complete"):
        try:
            todos = func.read_todo()

            num = int(user_action[9:])                                             # Extract the number
            index = num - 1

            if 0 <= index < len(todos):
                todo_to_remove = todos.pop(index).strip()

                func.write_todo(file_path, todos)

                print(f"Congrats! 🎉 You finished: {todo_to_remove}")
            else:
                print("Error: Invalid todo number.")

        except ValueError:
            print("Error: Please enter a valid number.")
        except IndexError:
            print("Error: Todo number does not exist.")
        except FileNotFoundError:
            print("Error: Todo list not found.")

    elif user_action == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid command! Please enter add, show, edit, complete, or exit.")
