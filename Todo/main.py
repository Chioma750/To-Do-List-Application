from storage import load_tasks
from tasks import add_task, view_task, complete_task, delete_task
load_tasks()

def main_menu():
    while True:
        print("1. Add a task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Quit")
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
            delete_task()
            print()
        elif options == "5":
            print("Quitting...")
            break
        else:
            print("Invalid choice, try again")
            print()

main_menu()
