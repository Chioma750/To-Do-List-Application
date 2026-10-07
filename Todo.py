to_do = []
def add_task():
    answer = input("What is your task for today: ")

    task = {
        "text": answer,
        "done": False,
    }
    to_do.append(task)
    print("Added")
    print()

def view_task():
    if not to_do:
        print("You have no tasks yet. Add one to get started.")
        return

    for num, task in enumerate(to_do, start = 1):
        if task["done"]:
            print (num, task["text"], '[x]')
        else:
            print (num, task["text"], '[]')

def complete_task():
    if not to_do:
        print("You have no tasks yet. Add one to get started.")
        return

    view_task()
    try:
        task_number = int(input("Which number of task did you just finish: "))
    except ValueError:
        print("Please enter a number")
        return

    if task_number < 1 or task_number > len(to_do):
        print("This task number doesn't exist.")
        return

    position = task_number - 1 
    card = to_do[position]
    card["done"] = True
    print("The task is marked done")       
    print()    

def delete_task():
    if not to_do:
        print("Your to-do list is empty")
        return
    view_task()
    try:
        task_number = int(input("Which number of task did want to delete: "))
    except ValueError:
        print("please enter a number")
        return

def main_menu():
    while True:
        print("1. Add a task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Quit")
        options = input("Choose an option: ") 

        if options == "1":
            add_task()
        elif options == "2":
            view_task()
            print()
        elif options == "3":
            complete_task()
            print()
        elif options == "4":
            print("Quitting...")
            break
        else:
            print("Invalid choice, try again")
            print()

main_menu()
