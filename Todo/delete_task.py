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
    
    if task_number < 1 or task_number > len(to_do):
        print("This task number does not exist.")
        return

    position = task_number - 1
    to_do.pop(position)
    print("Deleted!")
    save_tasks()
    print()