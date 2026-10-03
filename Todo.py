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
    if not to_do:
        print("You have no tasks yet. Add one to get started.")
        return

    for num, task in enumerate(to_do, start = 1):
        if task["done"]:
            print (num, task["text"], '[x]')
        else:
            print (num, task["text"], '[ ]')
add_task()
add_task()
print()
view_task()

def main_menu():
    while True:
        print("1. Add a task")
        print("2. View tasks")
        print("3. Quit")
        options = input("Choose an option: ") 

        if options == "1":
            add_task()
        elif options == "2":
            view_task()
        elif options == "3":
            print("Quiting...")
            break
        else:
            print("Invalid choice, try again")
#print(to_do)