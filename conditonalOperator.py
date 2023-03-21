user_text = "Enter a todo: "

todos = []
while True:
    todo = input(user_text)
    print(todo.capitalize())
    todos.append(todo)
    print(todos)

