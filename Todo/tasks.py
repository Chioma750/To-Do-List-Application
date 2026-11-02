from storage import to_do, save_tasks
def add_task():
    answer = input("What is your task for today: ")

    task = {
        "text": answer,
        "done": False,
    }
    to_do.append(task)
    print("Added!")
    save_tasks()
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
    save_tasks()   
    print()  

def delete_task():
    if not to_do:
        print("Your to-do list is empty")
        return
    view_task()
    try:
        task_number = int(input("Which number of task did you want to delete: "))
    except ValueError:
        print("Please enter a number")
        return
    
    if task_number < 1 or task_number > len(to_do):
        print("This task number does not exist.")
        return

    position = task_number - 1
    to_do.pop(position)
    print("Deleted!")
    save_tasks()
    print()  