import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print("it is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)


    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)


    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1   # user doesn't know about python idex system so we have to adjust by taking away 1

            todos = functions.get_todos()

            new_todo = input("Enter the edited version of this todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue


    elif user_action.startswith("complete"):
        try:
            completed_todo_number = int(user_action[9:]) - 1

            todos = functions.get_todos()

            todo_being_removed = todos[completed_todo_number].strip("\n")

            todos.pop(completed_todo_number)

            functions.write_todos(todos)

            print(f"{todo_being_removed} has been removed")

        except IndexError:
            print("There is no todo with that number")
            continue


    elif user_action.startswith("exit"):
        break


    else:
        print("command is not valid")


print("Bye!")
