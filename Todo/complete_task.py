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