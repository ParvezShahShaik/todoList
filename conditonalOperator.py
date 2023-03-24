todos = []

while True:
    user_action = input("Type add, edit, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show' | 'display':
            for item in todos:
                # CAPITALIZE THE WORD IN THE LIST
                item = item.title()
                print(item)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number-1
            new_todo = input("Enter your new todo to add: ")
            todos[number] = new_todo

        case 'exit':
            break

        case _:
            print("Please select a valid option")

print("Bye!")



