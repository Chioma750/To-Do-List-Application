to_do = []
def add_task():
    answer = input("What is your task for today: ")

    task = {
        "text": answer,
        "done": False,
    }
    to_do.append(task)
    print("Added")

def view_task():
    for task in to_do:
        print()
add_task()
add_task()

print(to_do)