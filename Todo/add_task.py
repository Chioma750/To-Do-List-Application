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