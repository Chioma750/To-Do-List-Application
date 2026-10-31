def view_task():
    if not to_do:
        print("You have no tasks yet. Add one to get started.")
        return

    for num, task in enumerate(to_do, start = 1):
        if task["done"]:
            print (num, task["text"], '[x]')
        else:
            print (num, task["text"], '[]')