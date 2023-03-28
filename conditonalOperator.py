todos = []

while True:
    user_action = input("Type add, edit, show, exit or complete: ")
    user_action = user_action.strip()

    match user_action:

        case 'add':
            todo = input("Enter a todo: ") + "\n"
            # Reading a file
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            # Appending Data into Todos
            todos.append(todo)
            # Writing A File
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index +1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number-1
            new_todo = input("Enter your new todo to add: ")
            todos[number] = new_todo

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)

        case 'exit':
            break

        case _:
            print("Please select a valid option")

print("Bye!")



